import os
import argparse

parser = argparse.ArgumentParser(description='Query your filesystem to find a file')

parser.add_argument(
	'terms',
	metavar='term',
	help='the filename(s) to look for',
	nargs='+'
)

args = parser.parse_args()

def query(start_path, terms):
	for path, directories, files in os.walk(start_path):
		if len(terms) == 1 and terms[0] in files:
			print os.path.join(path, terms[0])
		elif terms[0] in directories:
			if len(terms) > 1:
				query(os.path.join(path, terms[0]), terms[1:])
			elif terms[0] in directories:
				print os.path.join(path, terms[0])
				
query('./', args.terms)

