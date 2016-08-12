from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import qrcode
from PIL import Image
import urllib2 as urllib
import io
import qrcode

def createQrCode(url):
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
        qr.add_data(url)
        img = qr.make_image()
        img.save("qrcode.png")
        

def copyQrCode(bitlUrl, password):
        front = Image.open('front.png') #input file
        template = Image.open('qrcode.png')
        template = template.resize((420, 420), Image.ANTIALIAS)
        front.paste(template, (3350, 770))
        draw = ImageDraw.Draw(front)
        fontsize = 50;
        font = ImageFont.truetype("../Dosis-Regular/dosis/Dosis-Regular.ttf", fontsize)
        draw.text((3380, 1180),bitlUrl, font=font, fill=(0,0,0,0) )
        draw.text((3380, 1235),"password: "+password, font=font, fill=(0,0,0,0) )
        front.save('new.png',dpi=(300,300),quality=100)


def copyLogo(url):
        front = Image.open('new.png')
        fd = urllib.urlopen(url)
        image_file = io.BytesIO(fd.read())
        im = Image.open(image_file)
        front.paste(im, (400, 600), im)
        front.save('new1.png',dpi=(300,300),quality=100)


def downloadLogo():
        file_id = '1ZdR3L3qP4Bkq8noWLJHSr_iBau0DNT4Kli4SxNc2YEo'
        request = drive_service.files().export_media(fileId=file_id,mimeType='application/pdf')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        print (("Download %d%%."),int(status.progress() * 100) )
copyLogo("https://www.googledrive.com/host/0B1rL6XantNVxUWxrc01yb0UzbG8")
