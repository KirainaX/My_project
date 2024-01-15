from pytube import YouTube
import sys

c = 0

url_input = input("Enter your URL: ")
all_streams = YouTube(url_input).streams.all()

for i in all_streams:
    print(str(c) + ") " + str(i))
    c += 1

stm_input = int(input("Choose the suitable stream: "))
print("Enter the directory path to save:")
folder_name = input()

try:
    choice = all_streams[stm_input].download(folder_name)
    print("Download complete... :)")
except Exception as e:
    print("An error occurred:", str(e))































'''from pytube import YouTube
from tkinter import filedialog

c = 0

url_imput = input("Enter your URL: ")
all_streams = YouTube(url_imput).streams.all()

for i in all_streams:
    print(str(c)+") "+str(i))
    c+=1

stm_input = int(input("Chose the suitable stream: "))
print("Chose directory to save :) ")
folder_name = filedialog.askdirectory()
choice = all_streams[stm_input].download(folder_name)
print("Download complete...:)")'''
