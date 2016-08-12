from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
 
from pyqrcode import pyqrcode

url=pyqrcode.create('jbjbjb')
url.png('Logo File.png', scale=8)
print(url.terminal(quiet_zone=1))

new_im = Image.open("AP0578 Front Template (Input).jpg")
      
    # right bottom corner 3,3,1,1
      
new_im1 = Image.open("Logo File.png")
new_im2 = Image.open("Logo File.png")
new_im3 = Image.open("pyqrcode.png")
new_im.paste(new_im1, (50,500))
new_im.paste(new_im2, (1500,2200))
new_im.paste(new_im3, (3500,800))
#new_im = Image.new('RGB',( 1200, 1200),color=(255,255,255))
draw = ImageDraw.Draw(new_im)
fontsize=35
fontsize1=200
f = open("Variable Data.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "Link" in line: 
        for l in searchlines[i+1:i+2]:
            mytext=l
            print
for j, line in enumerate(searchlines):
            if "Link" in line:
                for g in searchlines[j+1:j+3]:
                    mytext2=g
                    print
                    mytext3="Rahul Samitha"
font = ImageFont.truetype("font/Coval-Regular.ttf", fontsize)
font1 = ImageFont.truetype("font/Champignon Script.ttf", fontsize1)
draw.text((3400,1000),mytext,('Black'),font=font)
draw.text((3400,1050),mytext2,('Black'),font=font)
draw.text((2100,3100),mytext3,('Black'),font=font1)
new_im.show()

   
