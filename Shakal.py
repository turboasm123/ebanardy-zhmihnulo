import os,subprocess, random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFilter
import PIL.ImageOps
import PIL

root_path=os.getcwd()
in_path=str(root_path+"/in/")
out_path=str(root_path+"/out/")
db_path = os.path.abspath(root_path+"/images_db/")

os.chdir(root_path)

for i,f in enumerate(os.listdir(db_path)):
	source = os.path.join(db_path, f)
	destination = os.path.join(in_path,(str("in.jpg")))
	os.rename(source, destination)
	if i == 1:
		break
			
os.chdir(in_path)

img=Image.open("in.jpg")
width, height = img.size

use_emboss = random.randint(0,3)

use_contour = random.randint(0,3)

use_unsharp = random.randint(0,1)

use_invert = random.randint(0,3)

use_contrast = random.randint(0,3)

use_color = random.randint(0,3)

use_posterize = random.randint(0,4)

use_shakal = random.randint(0,3)

use_noise = random.randint(0,2)

use_solarize = random.randint(0,3)

if use_emboss == 1:
        img = img.filter(ImageFilter.EMBOSS)

if use_contour == 1:
	img = img.filter(ImageFilter.CONTOUR)
	img = img.filter(ImageFilter.SMOOTH_MORE)

if use_unsharp == 1:
	randradius=random.randint(10,50)
	randperc=random.randint(200,1000)
	randthreshold=random.randint(50,100)
	img = img.filter(ImageFilter.UnsharpMask(radius=randradius, percent=randperc, threshold=randthreshold))
	
if use_contrast != 0:
        img_contrast_enhanced = PIL.ImageEnhance.Contrast(img)
        contrast_factor=random.randint(5,20)
        img = img_contrast_enhanced.enhance(contrast_factor)

if use_color != 0:
        img_color_enhanced = PIL.ImageEnhance.Color(img)
        color_factor=random.randint(5,100)
        img = img_color_enhanced.enhance(color_factor)


if use_invert != 0:
        img = PIL.ImageOps.invert(img)


if use_posterize != 0:
	img = PIL.ImageOps.posterize(img,1)


if use_solarize !=0:
	solar_rand=random.randint(30,120)
	img=PIL.ImageOps.solarize(img,threshold=solar_rand)

if (use_noise != 0 and use_emboss !=1 and use_contour != 1):
	img_pixels = img.load()
	noise_factor = random.randint(10,20)
	draw = ImageDraw.Draw(img)
	for noise_x in range(width):
		for noise_y in range(height):
			noise_random = random.randint(-noise_factor,noise_factor )
			noise_r = img_pixels[noise_x, noise_y][0] + noise_random
			noise_g = img_pixels[noise_x, noise_y][1] + noise_random
			noise_b = img_pixels[noise_x, noise_y][2] + noise_random
			if (noise_r < 0):
				noise_r = 0
			if (noise_g < 0):
				noise_g = 0
			if (noise_b < 0):
				noise_g = 0
			if (noise_r > 255):
				noise_r = 255
			if (noise_g > 255):
				noise_g = 255
			if (noise_b > 255):
				 noise_b = 255
			draw.point((noise_x, noise_y), (noise_r, noise_g, noise_b))

os.chdir(out_path)

img = PIL.ImageOps.equalize(img, mask=None)

if use_shakal != 0:
	img.save("out.temp.jpg","JPEG", quality=2)
else:
	img.save("out.temp.jpg", "JPEG", quality=100)

img1=Image.open("out.temp.jpg")

width1, height1 = img1.size
width_half=int(width/2)

if (width1 < 500 & height1<500):
	font_size_ebat = 32
	font_size_water = 12
	textheight=height1-48
	middle=width_half-128

elif (width1 <=1000 | height1 > 500):
	font_size_ebat = 64
	font_size_water = 18
	textheight=height1-80
	middle=width_half-256

elif width1 <= 2000:
	font_size_ebat = 128
	font_size_water = 48
	textheight=height1-160
	middle=width_half-512
else:
	font_size_ebat = 256
	font_size_water = 96
	textheight=height1-1152
	middle=width_half-1024

rgb_img = img1.convert('RGB')
r_w, g_w, b_w = rgb_img.getpixel((10,10))

font_ebat_color_rsum = 0
font_ebat_color_gsum = 0
font_ebat_color_bsum = 0
pixel_ebat_count=0
img1_pixels = img1.load()

for font_ebat_color_x in range(width1):
	for font_ebat_color_y in range (textheight,height):

		font_ebat_color_r = img1_pixels[font_ebat_color_x, font_ebat_color_y][0]
		font_ebat_color_g = img1_pixels[font_ebat_color_x, font_ebat_color_y][1]
		font_ebat_color_b = img1_pixels[font_ebat_color_x, font_ebat_color_y][2]
		pixel_ebat_count += 1
		font_ebat_color_rsum += font_ebat_color_r
		font_ebat_color_gsum += font_ebat_color_g
		font_ebat_color_bsum += font_ebat_color_b

font_ebat_color_rmean = int(font_ebat_color_rsum/pixel_ebat_count)
font_ebat_color_gmean = int(font_ebat_color_gsum/pixel_ebat_count)
font_ebat_color_bmean = int(font_ebat_color_bsum/pixel_ebat_count)

if(font_ebat_color_rmean < 90 and font_ebat_color_gmean < 90 and font_ebat_color_bmean < 90):
        font_color_ebat=(255,255,255)
elif (font_ebat_color_rmean > 100 or font_ebat_color_gmean > 100 or font_ebat_color_bmean > 100):
        font_color_ebat=(0,0,0)
else:
	font_color_ebat=(100,100,100)

font_water_color_rsum = 0
font_water_color_gsum = 0
font_water_color_bsum = 0
pixel_water_count=100

for font_water_color_x in range(width1):
        for font_water_color_y in range (0,100):
                font_water_color_r = img1_pixels[font_water_color_x, font_water_color_y][0]
                font_water_color_g = img1_pixels[font_water_color_x, font_water_color_y][1]
                font_water_color_b = img1_pixels[font_water_color_x, font_water_color_y][2]
                pixel_water_count += 1
                font_water_color_rsum += font_water_color_r
                font_water_color_gsum += font_water_color_g
                font_water_color_bsum += font_water_color_b

font_water_color_rmean = int(font_water_color_rsum/pixel_water_count)
font_water_color_gmean = int(font_water_color_gsum/pixel_water_count)
font_water_color_bmean = int(font_water_color_bsum/pixel_water_count)

if(font_water_color_rmean < 90 and font_water_color_gmean < 90 and font_water_color_bmean < 90):
        font_color_water=(128,128,128)
elif (font_water_color_rmean > 100 or font_water_color_gmean > 100 or font_water_color_bmean > 100):  
        font_color_water=(64,64,64)	
else:
	font_color_water=(32,32,32)
random_a_x=random.randint(0,width1-100)
random_a_y=random.randint(0,textheight)
rgb_a = img1.convert('RGB')
r_a,g_a,b_a = rgb_a.getpixel((random_a_x,random_a_y))

if ((r_a < 80 and g_a < 80 and b_a < 80)):
	font_color_a = (255,255,255)
else:
	font_color_a = (0,0,0)

os.chdir(root_path)

font = "font.ttf"
unicode_font_ebat = ImageFont.truetype(font, font_size_ebat)
unicode_font_water = ImageFont.truetype(font, font_size_water)
unicode_font_a = ImageFont.truetype(font, font_size_water)

os.chdir(out_path)

draw  =  ImageDraw.Draw (img1)

zhmih_roulette = random.randint(1,10)
if zhmih_roulette == 1:
	draw.text ((middle,textheight), "iбатб жмыхнуло", font=unicode_font_ebat,fill=font_color_ebat)
else:
	draw.text ((middle,textheight), "ебать жмыхнуло", font=unicode_font_ebat,fill=font_color_ebat)

draw.text ((0,0), "https://vk.com/ebat_zhmihnulo", font=unicode_font_water,fill=font_color_water)
draw.text ((random_a_x,random_a_y),"а", font=unicode_font_a, fill=font_color_a)
img1.save("out.jpg", "JPEG", quality=100)

print("EXTRA FRIED!Check",out_path+"out.jpg!")
