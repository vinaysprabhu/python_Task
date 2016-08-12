from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode

import math

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)
img = qr.make_image()

# fontsize=75;
# font = ImageFont.truetype("fonts/Dosis-Regular.otf", fontsize)


def AddLogo(mfname, lfname,qrname, outfname):

    new_im = Image.open("AP0578 Front Template (Input).jpg")
      
    new_im1 = Image.open("Logo File.png")
    new_im.paste(new_im1, (100,100))
    new_im.save('final.png',dpi=(300, 300),quality=100)

    # right bottom corner 3,3,1,1
      

    new_im.show()
   
    

AddLogo("AP0578 Front Template (Input).jpg", "Logo File1.png","download.png", "molecule_logo.png")

def AddQR(mfname,qrname, outfname):

    mimage = Image.open(mfname)
    qrname=Image.open(qrname)
    mbox = mimage.getbbox()
    qbox=qrname.getbbox()

    # right bottom corner 3,3,1,1
     
    box = (mbox[3] + qbox[3], mbox[1] + qbox[2])
    mimage.paste(qrname, box)

    mimage.show(outfname)
    
   
