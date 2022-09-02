# ARTSCII
#### Video Demo:  https://youtu.be/brrVfLyODd4
#### Description:
I wanted to create a python program that could convert images to ASCII Art for my final project for Harvard's CS50. I prototyped alot of different ideas but the execuations failed because of alot of bugs plus the output results were too **boring**. So then I stumbled across this amazing library called [ascii_magic](https://pypi.org/project/ascii-magic/). And I created this CLI program for using this library.
#### Requirements:
'pip install ascii-magic'   ###### The main Library that does all the work
'pip install argparse'      ###### For Parsing Arguments
'pip install PIL'           ###### Python Imaging Library (PIL) for handling a few errors related to images
#### Usage:
'python ascii_magic.py -f <path to file>  -c <number of columns> -m <mode> -o <output file name>'
###### OR 
'python ascii_magic.py -l <link to image> -s <size> -c <number of columns> -m <mode> -o <output file name>'
##### The Image File -f|--file **OR** The Link To Image -l|--link:
This will be the path to the image or the URL to the image and they are mutually exclusive.
##### The number of columns -c|--columns:
This represents the number of columns or Ascii Charcaters in a row, the more number of columns the more wider and good resolution the image.
But to avoid crashes of system, the number of columns have been limited to a preset value because more columns take more rendering time and more CPU power.
##### The Mode -m|--mode [h|t]:
This will be either an HTML(h) mode or terminal (t) mode. The HTML mode saves the output in an HTML file and the Terminal mode renders it to the terminal.
##### The Output File -o|--output:
This is by default set as output.html but can be changed by using -o <output name goes here>. However, any output name not an html file will not be accepted such as *wrongfile.jpg*
##### Errors:
Most of the errors I came across are well handled and displays a prompt before exiting which can give a good idea about what's wrong.