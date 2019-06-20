import os
import shutil
import zipfile

# code for zipping from https://stackoverflow.com/questions/14568647/create-zip-in-python
def zip(src, dst):
	zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
	abs_src = os.path.abspath(src)
	for dirname, subdirs, files in os.walk(src):
		for filename in files:
			absname = os.path.abspath(os.path.join(dirname, filename))
			arcname = absname[len(abs_src) + 1:]
			print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
			zf.write(absname, arcname)
	zf.close()

def publish():
	dist_folder = './dist'
	# remove dist folder and recreate it
	shutil.rmtree(dist_folder, ignore_errors=True)
	
	os.makedirs(dist_folder)
	print 'Create folder '+dist_folder

	# also publish example thesis
	print 'copy files of example thesis'
	shutil.copytree(src='./example-thesis', dst=dist_folder+'/bin-we',
		ignore=shutil.ignore_patterns('*.aux', '*.bbl', '*.bcf', '*.blg', '*.fdb_latexmk', '*.fls', '*.lof', '*.log', '*.lol', '*.lot', '*.out', '*.xml', '*.gz', '*.toc', '.sty'))

	# create doc folder
	os.makedirs(dist_folder+'/bin/doc')
	print 'Create folder '+dist_folder+'/bin/doc'
	os.makedirs(dist_folder+'/bin-we/doc')
	print 'Create folder '+dist_folder+'/bin-we/doc'

	files = [
		('./CHANGELOG.md', 'CHANGELOG.md'),
		('./cleanthesis.sty', 'cleanthesis.sty'),
		('./MANIFEST.md', 'MANIFEST.md'),
		('./README.md', 'README.md'),
		('./VERSION', 'VERSION'),
		('./doc/cleanthesis-doc.tex', 'doc/cleanthesis-doc.tex'),
		('./doc/cleanthesis-doc.pdf', 'doc/cleanthesis-doc.pdf')
	]

	for file in files:
		print 'copy {} to {}'.format(file[0], dist_folder+'/bin/'+file[1])
		shutil.copyfile(file[0], dist_folder+'/bin/'+file[1])
		print 'copy {} to {}'.format(file[0], dist_folder+'/bin-we/'+file[1])
		shutil.copyfile(file[0], dist_folder+'/bin-we/'+file[1])

	# get the current version
	f = open('VERSION')
	current_version = f.readline()
	f.close()

	# zip the release of the style (without example thesis)
	zip(dist_folder+'/bin', dist_folder+'/cleanthesis_v'+current_version)
	# zip the release of the style including example thesis
	zip(dist_folder+'/bin-we', dist_folder+'/cleanthesis-incl-example_v'+current_version)

if __name__ == "__main__":
	publish()