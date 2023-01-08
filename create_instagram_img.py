import requests
from PIL import Image, ImageDraw, ImageOps
import textwrap3

# download image using url from mongodb into images
# crop image into a square
# apply white transparency over image
# add text

def getImageFileName(img_url):
    return (img_url.split("/")[-1]).split("?")[0]

def download_image(img_url, img_saved_folder):
    img_data = requests.get(img_url).content
    img_file_name = getImageFileName(img_url)
    img_file_path = '{}/{}'.format(img_saved_folder, img_file_name)
    with open(img_file_path, 'wb') as handler:
        handler.write(img_data)
    return img_file_path

def pad_image(img_file_path):
    tint_colour = (255,255,255)
    transparency = 0.65
    opacity = int(255 * transparency)
    with Image.open(img_file_path) as img: 
        img = img.convert("RGBA")
    
    overlay = Image.new('RGBA', img.size, tint_colour + (0,))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle( [(0,0), img.size] , fill=tint_colour+(opacity,))
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB") # Remove alpha for saving in jpg format.
    longest_side = max(img.size)
    img = ImageOps.pad(img, (longest_side, longest_side), color='grey')
    img.save(img_file_path)

def add_text(img_file_path, text):
    lines = textwrap3.wrap(text, width=40)
    y_text = h
    with Image.open(img_file_path) as img: 
        img = img.convert("RGBA")

    draw = ImageDraw.Draw(img)
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((w - width) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height
    img.show()

img_url = "https://onecms-res.cloudinary.com/image/upload/s--JpcYvP-h--/c_fill,g_auto,h_468,w_830/fl_relative,g_south_east,l_one-cms:core:watermark:afp_watermark,w_0.1/f_auto,q_auto/v1/one-cms/core/54c87dec3f6ffca05d225434c4f65897b02a5fff.jpg?itok=srLoboOA"

#img_file_path = download_image(img_url, "images")
#pad_image(img_file_path)
