from PIL import Image
import linecache
import ast
import random
filename = "image.jpg"

def loadImage(filename):
  img = Image.open(filename)
  width, height = img.size
  img = img.convert("RGB")
  pixel = img.load()
  return width, height, pixel

def combineImage(file1, file2, file3):
  text = ""
  oct_text_list = {}
  bin_text_list = {}
  hex_text_list = {}
  str_text_list = {}
  w1, h1, p1 = loadImage(file1)
  # f1 = open("demofile2.txt", "a")
  f = open("message.txt", 'r')
  i = 0
  for i in range(400000):
    text = text + f.readline()
    i = i + 1
  #text = text.replace(' ', '')
  #text = ''.join(text.split())
  text_list = text.split()
  i = 0
  for j in range(len(text_list)):
    str_text_list[i] = "0x" + text_list[j][:2]
    # print(str_text_list[i])
    i = i + 1
    str_text_list[i] = "0x" + text_list[j][2:]
    # print(str_text_list[i])
    i = i + 1
    j = j + 1
  # print(len(str_text_list))
  for l in range(len(str_text_list)):
    oct_text_list[l] = int(str_text_list[l], 16)
    hex_text_list[l] = hex(oct_text_list[l])
    bin_text_list[l] = bin(oct_text_list[l])
    l = l + 1
    
    # print(bin_text_list[i][2:])
    # print("\n")
  # print(hex_text_list)
  # print(oct_text_list)
  # print(bin_text_list)
  # f1.write(bin_text_list)
  # f1.close()
  width = w1        #1920
  height = h1       #1080
  a = 0
  img = Image.new("RGB", (width, height))
  pix = img.load()
  for y in range(0, height):
    for x in range(0, width):
      r1, g1, b1 = p1[x, y]
      # r2, g2, b2 = oct_text_list[a], oct_text_list[a + 1], oct_text_list[a + 2]
      r2, g2, b2 = random.randrange(1000), random.randrange(1000), random.randrange(1000)
      a = a + 3
      pix[x, y] = r1^r2, g1^g2, b1^b2
      
  img.save(file3)

if __name__ == "__main__":
  combineImage("image.jpg", "message.txt", "fake_image1000.png")


