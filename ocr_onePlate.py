import cv2
from PIL import Image
import sys
# import pyocr
# import pyocr.builders
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image = cv2.imread('assember.jpg')
#OCR辨識車牌
result = pytesseract.image_to_string(Image.open(r"assember.jpg"))

# 將 ocr 辨識結果優化
txt=result.replace("!","1") # 如果是 ! 字元，更改為字元 1
real_txt=re.findall(r'[A-Z]+|[\d]+',txt) #只取數字和大寫英文字母

#組合真正的車牌
txt_Plate = "".join(real_txt)
print("OCR辨識結果：", result)
print("優化後辨識結果：", txt_Plate)

cv2.imshow('image', image)     #顯示原始圖形
cv2.moveWindow("image",500,250)#將視窗移到指定位置   
key = cv2.waitKey(0)           #按任意鍵結束
cv2.destroyAllWindows()