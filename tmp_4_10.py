# /usr/bin/python
# coding: utf-8


import os

for file in os.listdir("."):
    if file.endswith(""):
        # print(file, file.zfill(3))
        os.rename(file,file.zfill(3))