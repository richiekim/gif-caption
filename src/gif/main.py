# Source: https://github.com/python-pillow/Pillow/issues/3128
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import io

my_text = 'Where\'s dowon'
my_font = ImageFont.truetype(font='./fonts/OpenSans-Bold.ttf', size=50)

im = Image.open('./mod-check.gif')

# Image width and height
W, H = (im.width, im.height)

# Text width and height
w, h = ImageDraw.Draw(im).textsize(text=my_text, font=my_font)

frames = []
for frame in ImageSequence.Iterator(im):
	# Add text
	d = ImageDraw.Draw(frame)
	d.text(xy=((W-w)/2, 20), text=my_text, fill=0, font=my_font)
	del d
	
	b = io.BytesIO()
	frame.save(b, format="GIF")
	frame = Image.open(b)

	frames.append(frame)
# Save as GIF
frames[0].save('./mod-check-out.gif', save_all=True, append_images=frames[1:])
