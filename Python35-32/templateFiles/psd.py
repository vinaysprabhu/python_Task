from PIL import Image, ImageSequence
im = Image.open("AP0681 Back Template.psd")
layers = [frame.copy() for frame in ImageSequence.Iterator(im)]
hello = Image.open("qrcode.jpg")
layers[0] =  hello
im.show('new1.png')
