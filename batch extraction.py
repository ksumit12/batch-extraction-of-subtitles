'''
Filename: e:\ubuntu\cnn\batch extraction.py
Path: e:\ubuntu\cnn
Created Date: Sunday, September 5th 2021, 12:52:17 pm
Author: sumit

Copyright (c) 2021 DREAM innovators
'''



#!/usr/bin/python
import subprocess
import argparse
import os
import time

start_time = time.time()

def get_subtitle(input_path,output_path):
    name_list = []
    srt_name = []
    path = os.listdir(input_path)
    for file in path[1:]:

        name = file[:file.rfind(".")]
        name_list.append(name)
        final = name + '[cleaned]' + '.srt'
        srt_name.append(final)
        # print(final)
        cm = f'ffmpeg -i ' + '"' + input_path + "\\" + file + '"' + " " + '"' + output_path + "\\" + final + '"'
        # print(cm)
        pt = subprocess.run(cm, shell=True)

    if pt.returncode == 0:
        print('command successfully executed!')
    else:
        print(' command failed')

    return name_list,srt_name


def srt(file_name, srt_name):

    for x in srt_name:

      cleaned_srt = out_path + "\\" + x
      print('cleaned srt',cleaned_srt)
      a = open(cleaned_srt, "r")
      k = a.readlines()
    for z in file_name:
       srt_name = out_path+"\\"+"final"+"\\"+z+"[final]"+".srt"
       print('srt name',srt_name)
       b = open(srt_name, "a")
       print('a',a)
       print('b',b)


    for line in k:
        if line[0] == "F":
            d = line.find("GPS")
            b.write("LAT " + line[d + 5:d + 12] + "\n")
            # print("LAT " + line[d + 5:d + 12] + "\n")
            b.write("LON " + line[d + 14:d + 21] + "\n")
            # print("LON " + line[d + 14:d + 21] + "\n")
        else:
            b.write(line)
            # print(line)

    a.close()
    b.close()


if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("--input_path", help="full path of input file")
   parser.add_argument("--output_path", help="full path of desired output folder")
   args = parser.parse_args()

   in_path = args.input_path
   out_path =args.output_path

   name,SRT_name = get_subtitle(in_path,out_path)
   time.sleep(20)
   srt(name,SRT_name)



   print("--- %s seconds ---" % (time.time() - start_time))