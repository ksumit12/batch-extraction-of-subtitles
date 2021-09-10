'''
Filename: e:\ubuntu\cnn\batch extraction.py
Path: e:\ubuntu\cnn
Created Date: Sunday, September 5th 2021, 12:52:17 pm
Author: sumit

Copyright (c) 2021 DREAM innovators
'''


# !/usr/bin/python
import subprocess
import argparse
import os
import time
import sys

start_time = time.time()
jst=[]




def get_subtitle(input_path ,output_path):
    name_list = []
    srt_name = []
    path = os.listdir(input_path)
    for file in path:
        if file.endswith(('.mp4' ,'.MP4' ,'mkv')):
            name = file[:file.rfind(".")]
            name_list.append(name)
            final = name + '[Unprocessed]' + '.srt'
            srt_name.append(final)
            # print(final)
            cm = f'ffmpeg -i ' + '"' + input_path + "\\" + file + '"' + " " + '"' + output_path + "\\" + final + '"'
            # print(cm)
            pt = subprocess.run(cm, shell=True)
        else:
            print("***************it's not a video so can't be converted********" ,file)

    if pt.returncode == 0:
        print('command successfully executed!')
    else:
        print(' command failed')

    return name_list ,srt_name


def srt(path):
    lst=[]
    directory = "Processed-SRT"
    final_dir = os.path.join(out_path, directory)
    # print("path", path)
    try:
        os.mkdir(final_dir)
    except:
        pass

    for p in path:
        if p.endswith(('.srt','.SRT')):
            input = f"{out_path}\{p}"
            # print("input", input)
            output = f"{final_dir}\{p[:len(p) - 4]}-PROCESSED.SRT"

            print("output", output)

            a = open(input, "r")
            b = open(output, "w")
            lst.append(output)

            k = a.readlines()
            global jst
            jst=lst


            for line in k:
                if line[0] == "F":
                    d = line.find("GPS")
                    b.write("LAT " + line[d + 5:d + 12] + "\n")
                    b.write("LON " + line[d + 14:d + 21] + "\n")
                else:
                    b.write(line)

            a.close()
            b.close()
            print(f"{p} Successfully done!")
        else:
            print("it's not a srt file")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", help="full path of input file")
    parser.add_argument("--output_path", help="full path of desired output folder")
    args = parser.parse_args()

    in_path = args.input_path
    out_path =args.output_path

    name, SRT_name = get_subtitle(in_path, out_path)
    time.sleep(5)

    # for s in range(1,length): print("no of iter",s)
    final = srt( SRT_name)


   
    print("--- %s seconds ---" % (time.time() - start_time))
