# get image filenames from dropbox 
# Dropbox has an excellent API Explorer interface to test API calls:
# https://dropbox.github.io/dropbox-api-v2-explorer/#file_requests_list

#  my question to forums:
# https://www.dropboxforum.com/t5/API-Support-Feedback/Using-API-to-get-a-list-of-direct-url-s-to-images-in-a-folder/m-p/389583#M21585

import svgwrite
from svgwrite.image import Image
from svgwrite import cm

BOX_SIZE = (5,1)
BOX_SPACING = (5.1, 1.1)
ORIGIN = (1,1)
IMAGE_OFFSET = (0,0)
TEXT_OFFSET = (1,.5)
IMAGE_SIZE = (1,1)

STYLES = """
    .textbox_style {stroke-width:1.0; stroke:lightgray; fill:none}
    .text_style    {font-size:14px; font-family:'Palatino Linotype'}
"""

dwg = svgwrite.Drawing('svgwrite-example.svg')
dwg.defs.add(dwg.style(STYLES))
g = dwg.g()

#g.add(svgwrite.text.Text("here is a bunch of text", (22,22), class_="text_style", id="text1"))
dwg.add(g)

#dwg.add(dwg.rect(insert=(5,5), size=(BOX_SIZE[0],BOX_SIZE[1]), stroke='blue', fill='white'))
#dwg.add(Image("test_tiny.jpg", insert=(50,50), size=(100,200)))

data = [{'company': 'a', 'locale': 'Washington, DC Region', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'sf': '2,500 - 3,000 SF'},
		{'company': 'd', 'locale': 'DC/Baltimore Region', 'sf': '4,000 SF'}]

x = ORIGIN[0]
y = ORIGIN[1]
i = 0
for d in data:
	mod = i % 3
	print(mod)
	if i > 0:
		if mod > 0:
			x = x + BOX_SPACING[0]
		else:
			y = y + BOX_SPACING[1]
			x = ORIGIN[0]
	print(x, ' ', y) 
	group = dwg.add(dwg.g(id=i))
	group.add(dwg.rect(insert=(x*cm,y*cm), size=(BOX_SIZE[0]*cm, BOX_SIZE[1]*cm), stroke='blue', fill='white'))
	image_x = x + IMAGE_OFFSET[0]
	image_y = y + IMAGE_OFFSET[1]
	group.add(Image("test_tiny.jpg", insert=(image_x*cm, image_y*cm), size=(IMAGE_SIZE[0]*cm,  IMAGE_SIZE[1]*cm)))
	text_x = x + TEXT_OFFSET[0]
	text_y = y + TEXT_OFFSET[1]
	group.add(svgwrite.text.Text("here is a bunch of text", (text_x*cm, text_y*cm), class_="text_style", id="text1"))
	i += 1



# output our svg image as raw xml
# print(dwg.tostring())

# write svg file to disk
dwg.save()

