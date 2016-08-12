from flask import Flask
import flask
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import qrcode


app = Flask(__name__)

@app.route('/template')
def creteBack():


	url = flask.request.args.get("url")
	qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
	qr.add_data(url)
	#qr.make(fit=True)
	img = qr.make_image()
	img.save("qrcode.jpg")
	qr_code = ImageReader('qrcode.jpg')
	canvas = Canvas('output.pdf')
	canvas.setPageSize((5374, 3602))
	canvas.drawImage(qr_code, 3000, 1000)
	canvas.showPage()
	canvas.save()

	return "1"


@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)
    
if __name__ == '__main__':
   app.run(port=8080, debug = True)