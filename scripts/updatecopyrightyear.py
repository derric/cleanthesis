import re
from datetime import datetime

def update_copyright_year():
	# header of all files (occurrences)
	files = ['CHANGELOG.md','cleanthesis.sty','MANIFEST.md','README.md','doc/cleanthesis-doc.tex']
	for filename in files:
		with open(filename, 'r') as f:
			content = f.read()
		regex = re.compile('Copyright\s\d{4}\sR.\sLangner')
		if (len(re.findall(regex, content)) > 0):
			repl = 'Copyright {} R. Langner'.format(datetime.now().strftime('%Y'))
			content = re.sub(regex, repl, content)
			with open(filename, 'w') as f:
				f.write(content)

	# in the docs
	filename = 'doc/cleanthesis-doc.tex'
	with open(filename, 'r') as f:
		content = f.read()
	regex = re.compile('Copyright\s.textcopyright.\s\d{4}\sR.\sLangner')
	repl = 'Copyright \\\\textcopyright\ '+datetime.now().strftime('%Y')+' R. Langner'
	content = re.sub(regex, repl, content)
	with open(filename, 'w') as f:
		f.write(content)

if __name__ == "__main__":
	update_copyright_year()