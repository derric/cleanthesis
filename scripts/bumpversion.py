import sys
import re
from datetime import datetime

def bump(args):
	if ( len(args) != 1 ):
		print('Usage: python bumpversion.py [major|minor|patch]')
		return

	# get the current version
	f = open('VERSION')
	current_version = f.readline()
	f.close()

	# extract the version parts
	parts = current_version.split('.')
	major = parts[0]
	minor = parts[1]
	patch = parts[2]

	# bump the version
	cmd_arg = args[0]
	if (cmd_arg=='major'):
		major = int(major)+1
		minor = 0
		patch = 0
	if (cmd_arg=='minor'):
		minor = int(minor)+1
		patch = 0
	if (cmd_arg=='patch'):
		patch = int(patch)+1
	new_version = '{}.{}.{}'.format(major, minor, patch)

	bump_version_file(current_version, new_version)
	bump_sty_file(current_version, new_version)
	bump_docs_file(current_version, new_version)

def bump_version_file(curr_version, new_version):
	filename = 'VERSION'

	with open(filename, 'r') as f:
		content = f.read()
	content = content.replace(curr_version, new_version)
	with open(filename, 'w') as f:
		f.write(content)

def bump_sty_file(curr_version, new_version):
	filename = 'cleanthesis.sty'

	with open(filename, 'r') as f:
		content = f.read()
	regex = re.compile('\d{4}/\d{2}/\d{2}\sv'+curr_version)
	content = re.sub(regex, datetime.now().strftime('%Y/%m/%d')+' v'+new_version, content)
	with open(filename, 'w') as f:
		f.write(content)

def bump_docs_file(curr_version, new_version):
	filename = 'doc/cleanthesis-doc.tex'

	with open(filename, 'r') as f:
		content = f.read()
	
	regex = re.compile('revision={'+curr_version+'}')
	repl = 'revision={'+new_version+'}'
	content = re.sub(regex, repl, content)

	regex = re.compile('date={\d{4}/\d{2}/\d{2}}')
	repl = 'date={'+datetime.now().strftime('%Y/%m/%d')+'}'
	content = re.sub(regex, repl, content)

	with open(filename, 'w') as f:
		f.write(content)

if __name__ == "__main__":
	bump(sys.argv[1:])