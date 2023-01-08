from create_instagram_image import create_instagram_image
from upload_freeimage import upload_freeimage
from insta import post_article_summary


img_url = "https://onecms-res.cloudinary.com/image/upload/s--JpcYvP-h--/c_fill,g_auto,h_468,w_830/fl_relative,g_south_east,l_one-cms:core:watermark:afp_watermark,w_0.1/f_auto,q_auto/v1/one-cms/core/54c87dec3f6ffca05d225434c4f65897b02a5fff.jpg?itok=srLoboOA"
text = "Happy flow " * 40

image_path = create_instagram_image(img_url, 'images', text)

image_url = upload_freeimage(image_path)

post_article_summary(image_url)