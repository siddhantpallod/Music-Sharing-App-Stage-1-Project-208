import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None
song_counter = 0

def musicWindow():
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
    
    window = Tk()
    window.title('Music Share')
    window.geometry('300x300')
    window.configure(bg = 'LightSkyBlue')
    
    selectlabel = Label(window, text = 'Select Song', bg = 'LightSkyBlue', font = ('Calibri', 8))
    selectlabel.place(x = 2, y = 1)
    
    listbox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'LightSkyBlue', borderwidth = 2, font = ("Calibri",10))
    listbox.place(x = 10, y = 18)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton = Button(window, text = 'Play', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri",10))
    PlayButton.place(x = 30, y = 200)
    
    StopButton = Button(window, text = 'Stop', bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri",10))
    StopButton.place(x = 200, y = 200)
    
    UploadButton = Button(window, text = 'Upload', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri",10))
    UploadButton.place(x = 30, y = 250)
    
    DownloadButton = Button(window, text = 'Download', bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri",10))
    DownloadButton.place(x = 200, y = 250)
    
    infoLabel = Label(window, text = '', fg = 'blue', bg = 'SkyBlue', font = ("Calibri",10))
    infoLabel.place(x = 4, y = 280)
    
    window.mainloop()
    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()

setup()