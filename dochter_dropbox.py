# Generate a Dochter "availabity report" programmatically which should save them alot of time
# over whatever manual process they are using now.
# This code creates a local svg file as its output.  View SVG files in a browser.
# Hopefully the SVG can be imported into InDesign.  Or, I can print to a pdf file from the 
# browser and then Logan can insert the pdf in a report?  Ask her.
# Better approach.  Use dropbox images, but only in a LOCAL folder that is synced to Dropbox.
# That way, the images are still available to the team, but I don't have to figure out what
# crazy filename is used on the dropbox server, and I don't have to auth or anything else with
# their API, just read the files locally with Python

import svgwrite
import csv
from svgwrite.image import Image
from svgwrite import cm

BOX_SIZE = (7.6,1.9)
BOX_SPACING = (8.2, 2.0)
ORIGIN = (1,1)
IMAGE_OFFSET = (-0.4,0)
LOGO_SIZE = (2,2)
LOGO_OFFSET = (4.0, 0.2)
TEXT1_OFFSET = (5.7,0.55)
TEXT2_OFFSET = (5.7,0.75)
TEXT3_OFFSET = (4.1,1.8)
IMAGE_SIZE = (4.0,1.9)

STYLES = """
    .textbox_style {stroke-width:1.0; stroke:lightgray; fill:none}
    .text_style    {font-size:5px; font-family:'Palatino Linotype'}
"""

dwg = svgwrite.Drawing('svgwrite-example.svg')
dwg.defs.add(dwg.style(STYLES))
g = dwg.g()
dwg.add(g)


def read_csv(filename):
	f = open(filename, newline='', encoding='utf-8-sig')
	return csv.DictReader(f)

data = [{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'athleta', 'locale': 'Washington, DC Region', 'industry': 'Int\'l Financial Institution', 'sf': '1,000 -2,000 SF'}, 
		{'company': 'b', 'locale': 'Washington, DC Region', 'industry': 'Specialty Cycling Retailer', 'sf': '2,500 - 3,000 SF'},
		{'company': 'c', 'locale': 'Washington, DC Region', 'industry': 'Indoor Climbing Gyms for Adults and Kids', 'sf': '2,500 - 3,000 SF'},
		{'company': 'd', 'locale': 'DC/Baltimore Region', 	'industry': 'Luxury Designer Lingerie and Accessories', 'sf': '4,000 SF'}]

x = ORIGIN[0]
y = ORIGIN[1]
i = 0
for d in read_csv('data.csv'):
	mod = i % 3
	if i > 0:
		if mod > 0:
			x = x + BOX_SPACING[0]
		else:
			y = y + BOX_SPACING[1]
			x = ORIGIN[0]
	group = dwg.add(dwg.g(id=i))
	group.add(dwg.rect(insert=(x*cm,y*cm), size=(BOX_SIZE[0]*cm, BOX_SIZE[1]*cm), stroke='red', fill='white'))
	image_x = x + IMAGE_OFFSET[0]
	image_y = y + IMAGE_OFFSET[1]
	group.add(Image("images/athleta.png", insert=(image_x*cm, image_y*cm), size=(IMAGE_SIZE[0]*cm,  IMAGE_SIZE[1]*cm)))

	logo_x = x + LOGO_OFFSET[0]
	logo_y = y + LOGO_OFFSET[1]
	group.add(Image("images/athleta_logo_260x180.png", insert=(logo_x*cm, logo_y*cm), size=(LOGO_SIZE[0]*cm, LOGO_SIZE[1]*cm)))

	text1_x = x + TEXT1_OFFSET[0]
	text1_y = y + TEXT1_OFFSET[1]
	group.add(svgwrite.text.Text(d['sf'].upper(), (text1_x*cm, text1_y*cm), class_="text_style", id="text1"))

	text2_x = x + TEXT2_OFFSET[0]
	text2_y = y + TEXT2_OFFSET[1]
	group.add(svgwrite.text.Text(d['locale'].upper(), (text2_x*cm, text2_y*cm), class_="text_style", id="text2"))

	text3_x = x + TEXT3_OFFSET[0]
	text3_y = y + TEXT3_OFFSET[1]
	group.add(svgwrite.text.Text(d['industry'].upper(), (text3_x*cm, text3_y*cm), class_="text_style", id="text3"))
	i += 1



# output our svg image as raw xml
# print(dwg.tostring())

# write svg file to disk
dwg.save()

