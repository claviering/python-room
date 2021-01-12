#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import getopt
from PIL import Image


argv = sys.argv[1:]
opts = []
inputFileName = ""
outFileName = ""
help = "usage: python3 main.py -i <input iamge file>"

def tips():
    print(help)
    sys.exit(2)

try:
    opts, args = getopt.getopt(argv, "hi:o:")  # 短选项模式
except:
    tips()

for opt, arg in opts:
    if opt == '-h':
      tips()
    elif opt in ['-i']:
        inputFileName = arg
    elif opt in ['-o']:
        outFileName = arg

if len(outFileName) == 0:
    outFileName = os.path.splitext(inputFileName)[0] + ".gif"

if len(inputFileName) == 0:
    tips()
image1 = Image.open(inputFileName)
im1 = image1.convert('RGB')
im1.save(outFileName)
