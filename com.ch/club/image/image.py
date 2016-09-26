#!/usr/bin/env python
# coding:utf-8


from PIL import Image
import glob ,os
import numpy as np
'''
图像识别1 预处理
函数changeformat1这里将图片替换为128*128*3的RGB格式的图片，并对图片做对称变换，以增加样本量
函数changeformat2将  测试集里的图片转换成128*128*3的RGB格式的图片
'''
rgb1 = 128
rgb2 = 128
rgb3 = 3

# 训练集数据 预处理
def changeformat1(folder1,folder2):
  folder_path=glob.glob(folder1+"/*.jpg")
  for files in folder_path:
    filepath,filename = os.path.split(files)
    filterame,exts = os.path.splitext(filename)
    if (os.path.isdir(folder2) == False):
      os.mkdir(folder2)
    im = Image.open(files)
    image_array = np.array(im)
    if image_array.shape != (rgb1,rgb2,rgb3):
      print "change format"
      im_RGB = im.convert('RGB')
    im_return = im_RGB.resize((rgb1,rgb2))
    im_return.save(folder2+'/'+filterame+'.jpg')
    # 对 图片进行翻转处理 增加训练集数据
    #im_return2 = im_return.transpose(Image.FLIP_LEFT_RIGHT)
    #im_return2.save(folder2+'/'+'a'+filterame+'.jpg')

# 测试数据集处理
def changeformat2(folder1,folder2):
  folder_path = glob.glob(folder1+'/*.jpg')
  for files in folder_path:
    filepath,filename = os.path.split(files)
    filterame,exts = os.path.splitext(filename)
    if(os.path.isdir(folder2) == False):
      os.mkdir(folder2)
    im = Image.open(files)
    image_array = np.array(im)
    if image_array.shape != (rgb1,rgb2,rgb3):
      print "change format"
      im_RGB = im.convert('RGB')
    im_return = im_RGB.resize((rgb1,rgb2))
    im_return.save(folder2+'/'+filterame+'.jpg')
    # im_return2 = im_return.transpose(Image.FLIP_LEFT_RIGHT)
    # im_return2.save(folder2+'/'+'a'+filterame+'.jpg')

if __name__=='__main__':
  train_path1 = '/home/s-13/image/train/'
  train_path2 = '/home/s-13/image/train_data/'
  folderList = os.listdir(train_path1)
  for folder in folderList:
    folder_path1 = os.path.join(train_path1,folder)
    folder_path2 = os.path.join(train_path2,folder)
    changeformat1(folder_path1,folder_path2)
  print 'train data set format have changed'
  test_path1 = '/home/s-13/image/test/'
  test_path2 = '/home/s-13/image/test_data/'
  changeformat2(test_path1,test_path2)
  print 'test data set format have changed'


