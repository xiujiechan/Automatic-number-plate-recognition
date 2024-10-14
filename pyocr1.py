from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"test.jpg"))
print(type(text), "   ", text)