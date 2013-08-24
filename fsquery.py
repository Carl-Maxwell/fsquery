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

def query(start_path, terms):
	for current_path, directories, files in walk(start_path):
		l = directories if (len(terms) > 1 or is_dir) else files

		for e in l:
			if fnmatch(e, terms[0]):
				if len(terms) > 1:
					query(path.join(current_path, e), terms[1:])
				else:
					print path.join(current_path, e)
					if args.first:
						exit()

query('./', args.terms)
