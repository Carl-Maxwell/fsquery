from os import walk, path
import argparse
from fnmatch import fnmatch

parser = argparse.ArgumentParser(description='Query your filesystem to find a file')

parser.add_argument(
	'terms',
	metavar='term',
	help='the filename(s) to look for',
	nargs='+'
)

parser.add_argument(
	'--first',
	dest="first",
	action="store_const",
	const=True,
	default=False,
	help='only find the first result'
)

args = parser.parse_args()

is_dir = args.terms[-1][-1] == '/'

if is_dir:
	args.terms[-1] = args.terms[-1][0:-1]

def match(term, l):
	for e in l:
		if fnmatch(e, term):
			return e
	return False

def query(start_path, terms):
	for current_path, directories, files in walk(start_path):
		if len(terms) == 1:
			if is_dir:
				thing = match(terms[0], directories)
			else:
				thing = match(terms[0], files)
			if thing:
				print path.join(current_path, terms[0])
				if args.first:
					exit()
		elif len(terms) > 1 and match(terms[0], directories):
			query(path.join(current_path, terms[0]), terms[1:])

query('./', args.terms)
