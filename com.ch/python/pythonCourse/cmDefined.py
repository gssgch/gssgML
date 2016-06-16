# coding:utf-8

class VOW(object):
  def __init__(self,text):
    self.text= text
  def __enter__(self):
    self.text = "enter: " + self.text #添加前缀
    return self  # 这里返回对象
  def __exit__(self,exc_type,exc_value,traceback):
    self.text=self.text + " now __exit__!" #添加后缀

with VOW("你好") as myvow:
  print(myvow.text)

print(myvow.text)
