# batch-extraction-of-subtitles

#THIS CODE ASSUMES THAT FFMPEG IS ALREADY INSTALLED

This code is specifically made for DJI phantom drone or drone mapper and surveyor
format to use this code:

1)suppose you have a folder consisting of n number of video taken from DJI phantom drone for example :-  D:\datatest\test2 where test2 contains all your video

2)create a new folder in that file name srt and inside that folder create another empty folder called final(this is important to name second folder as final you can anytime edit the code as you like)

3)code uses two arguments first is the --input_path which is the orginal path of supposedly folder for example :-  D:\datatest\test2 

4)second argument is --output_path which takes path of your supposedly folder plus cleaned foler for example :-  D:\datatest\test2\cleaned

5)cleaned folder will contain srt with all metadata like camera settings and gps with altitude

6)final folder will contain srt with onlt LAT LONG
