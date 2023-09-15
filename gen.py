from os import listdir
import string

# Reads template.html and html files in a folder called pages
# Replaces the string "<!-- TEMPLATE BODY -->" with the contents of each HTML
# file stored in the pages folder, then outputs the new file to the current
# directory

with open('template.html', 'r') as content_file:
    template = content_file.read()

for fname in listdir('pages'):
	if fname != 'template.html':
		with open('pages/' + fname, 'r') as content_file:
			content = content_file.read()
		content = string.replace(template, "<!-- TEMPLATE BODY -->", content)
		with open(fname, 'w+') as output_file:
			output_file.write(content)
			output_file.truncate()
		print content