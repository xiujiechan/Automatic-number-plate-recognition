def emptydir(dirname):         #清空資料夾
    if os.path.isdir(dirname): #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)       #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

def dirResize(src, dst):
    myfiles = glob.glob(src + '/*.JPG') #讀取資料夾全部jpg檔案
    emptydir(dst)
    print(src + ' 資料夾：')
    print('開始轉換圖形尺寸！')
    for f in myfiles:
        fname = f.split("\\")[-1]
        img = Image.open(f)
        img_new = img.resize((300, 225), Image.Resampling.LANCZOS)  # 轉換尺寸為140x40
        img_new.save(dst + '/' + fname)
    print('轉換圖形尺寸完成！\n')

import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

dirResize('predictPlate_sr', 'predictPlate')