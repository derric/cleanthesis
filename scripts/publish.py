import os
import shutil
import zipfile
import subprocess

# code for zipping from https://stackoverflow.com/questions/14568647/create-zip-in-python
def zip(src, dst):
	print '    create zip archive '+dst+'.zip'
	zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
	abs_src = os.path.abspath(src)
	for dirname, subdirs, files in os.walk(src):
		for filename in files:
			absname = os.path.abspath(os.path.join(dirname, filename))
			arcname = absname[len(abs_src) + 1:]
			#print '        zipping %s as %s' % (os.path.join(dirname, filename), arcname)
			zf.write(absname, arcname)
	zf.close()

def publish():
	print 'PUBLISH cleanthesis --> started'

	dist_folder = './dist'
	folder_plain = dist_folder+'/plain/cleanthesis'
	folder_withexample = dist_folder+'/withexample/cleanthesis'

	# remove dist folder and recreate it
	print '    delete dist folder '+dist_folder
	shutil.rmtree(dist_folder, ignore_errors=True)
	os.makedirs(dist_folder)
	print '    create folder '+dist_folder

	# publish example thesis files
	print '    copy files of example thesis'
	shutil.copytree(src='./example-thesis', dst=folder_withexample,
		ignore=shutil.ignore_patterns('*.aux', '*.bbl', '*.bcf', '*.blg', '*.fdb_latexmk', '*.fls', '*.lof', '*.log', '*.lol', '*.lot', '*.out', '*.xml', '*.gz', '*.toc', '.sty'))

	# create doc folder
	os.makedirs(folder_plain+'/doc')
	print '    create folder '+folder_plain+'/doc'
	os.makedirs(folder_withexample+'/doc')
	print '    create folder '+folder_withexample+'/doc'

	files = [
		('./CHANGELOG.md', 'CHANGELOG.md'),
		('./cleanthesis.sty', 'cleanthesis.sty'),
		('./MANIFEST.md', 'MANIFEST.md'),
		('./README.md', 'README.md'),
		('./VERSION', 'VERSION'),
		('./doc/cleanthesis-doc.tex', 'doc/cleanthesis-doc.tex'),
		('./doc/cleanthesis-doc.pdf', 'doc/cleanthesis-doc.pdf')
	]

	print '    copy cleanthesis to dist folder'
	for file in files:
		#print '        copy {} to {}'.format(file[0], folder_plain+'/'+file[1])
		shutil.copyfile(file[0], folder_plain+'/'+file[1])
		#print '        copy {} to {}'.format(file[0], folder_withexample+'/'+file[1])
		shutil.copyfile(file[0], folder_withexample+'/'+file[1])

	# get the current version
	f = open('VERSION')
	current_version = f.readline()
	f.close()

	# fix file permissions
	print '    fix file permissions for CTAN ...'
	for f in [folder_plain,folder_withexample]:
		for dir, subdirs, files in os.walk(f):
			for file in files:
				#print os.path.join(dir, file)
				os.chmod(os.path.join(dir, file), 0664)
			#for d in subdirs:
			#	print os.path.join(dir, d)
			#	os.chmod(os.path.join(dir, d), 0775)

	# zip the release of the style (without example thesis)
	zip(folder_plain+'/..', dist_folder+'/cleanthesis_v'+current_version)
	# zip the release of the style including example thesis
	zip(folder_withexample+'/..', dist_folder+'/cleanthesis-incl-example_v'+current_version)

	print 'PUBLISH cleanthesis --> finished'

if __name__ == "__main__":
	publish()