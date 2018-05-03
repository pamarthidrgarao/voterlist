import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import re

pdf = wi(filename = "/home/durgarao/Downloads/PDFGeneration-10-11.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []
voterList = []
fatherList = []
for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')

	for s in text.splitlines():
		if(s.strip()):
			if(re.match('^([0-9]{1,} I)',s)):
				n= s.split('I')
				print(n[0].strip())
				print(n[1].strip())
			if(s.find("Elector's Name:")!=-1):
				name = s[15:]
				voterList.append(name.upper())
			if (s.find("Husband's Name:") != -1 or s.find("Father's Name:") != -1 ):
				fatherName = s[15:]
				fatherList.append(fatherName.upper())
			# print(s)
	#recognized_text.append(text)

#print(recognized_text)
print(voterList)
print(fatherList)