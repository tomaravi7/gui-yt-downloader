import tkinter
from tkinter.constants import FALSE 
from pytube import YouTube

m=tkinter.Tk(screenName='YT Downloader')
m.title("Yt Downloader")
m.geometry("700x300")
# m.iconphoto(False, tkinter.PhotoImage(file='yticon.png')) //error everytime i start it without changing name
flag=0
def single_video():
    YouTube(yt_entry.get()).streams.get_highest_resolution().download(save.get())
    flag=1
    if(flag==0):
        tkinter.Label(m, text='Error').grid(row=6)
    else:
        tkinter.Label(m, text='DOWNLOADED').grid(row=6)
    
tkinter.Label(m, text='Enter URL : ').grid(row=0)
yt_entry=tkinter.Entry(m)
yt_entry.grid(row=0,column=1)
b=tkinter.Button(m,text='Download',bg="cyan",command=single_video)
b.grid(row=2,column=1)
tkinter.Label(m, text='Enter download folder address : ').grid(row=0,column=3)
tkinter.Label(m, text='(If no folder is entered your file will be saved in the installation folder)').grid(row=1,column=3)
save=tkinter.Entry(m)
save.grid(row=0,column=4)
m.mainloop()
