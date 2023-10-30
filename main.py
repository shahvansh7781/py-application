from tkinter import *
from PIL import ImageTk,Image
import os
from pygame import mixer

#colors
col="#ffffff"
co2="#3C1DC6"
co3="#333333"
co4="#CC5DE8"

window=Tk()
window.title("Music Player")
window.geometry('352x255')
window.configure(background=col)
window.resizable(width=FALSE,height=FALSE)

#events
def play_music():
   runnning = listbox.get(ACTIVE) #get song from list which is active
   running_song['text'] = runnning #change text of currently active song from 
   mixer.music.load(runnning) #load that song
   mixer.music.play() #play that song

def pause_music():
   mixer.music.pause()

def resume_music():
   mixer.music.unpause()

def stop_music():
   mixer.music.stop()

def next_music():
   playing = running_song['text'] #get text of current song
   index = songs.index(playing) #get index of current song playing
   new_index = index+1 #jump to next index of current song
   playing = songs[new_index] #get song name of that jumped index i.e next song
   mixer.music.load(playing) #load that next song
   mixer.music.play() #play that next song

   listbox.delete(0,END) #clear the list as again same set of songs will be loaded
   show()
   listbox.select_set(new_index)

   running_song['text'] = playing #change text

def previous_music():
   playing = running_song['text'] #get text of current song
   index = songs.index(playing) #get index of current song playing
   new_index = index-1 #jump to next index of current song
   playing = songs[new_index] #get song name of that jumped index i.e next song
   mixer.music.load(playing) #load that next song
   mixer.music.play() #play that next song

   listbox.delete(0,END) #clear the list as again same set of songs will be loaded
   show()
   listbox.select_set(new_index)

   running_song['text'] = playing #change text

#frames
left_frame = Frame(window,width=150,height=150,bg=col)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame = Frame(window,width=250,height=150,bg=co3)
right_frame.grid(row=0,column=1,padx=0)

button_frame = Frame(window,width=400,height=100,bg=co4)
button_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

#right frame
listbox=Listbox(right_frame,selectmode=SINGLE,font=("Arial 9 bold"),width=22,bg=co3,fg=col)
listbox.grid(row=0,column=0)

w=Scrollbar(right_frame,bg=col)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)
#images
img_1 = Image.open('icons/music.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1) #load image
app_image = Label(left_frame,height=130,image=img_1,padx=10,bg=col) # where to keep
app_image.place(x=10,y=15)

img_2 = Image.open('icons/previous.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2) #load image
previous_button = Button(button_frame,width=40,height=40,image=img_2,padx=10,bg=col,command=previous_music) # where to keep
previous_button.place(x=10+28,y=35)

img_3 = Image.open('icons/play.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3) #load image
play_button = Button(button_frame,width=40,height=40,image=img_3,padx=10,bg=col,command=play_music) # where to keep
play_button.place(x=56+28,y=35)

img_4 = Image.open('icons/next.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4) #load image
next_button = Button(button_frame,width=40,height=40,image=img_4,padx=10,bg=col,command=next_music) # where to keep
next_button.place(x=102+28,y=35)

img_5 = Image.open('icons/pause.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5) #load image
pause_button = Button(button_frame,width=40,height=40,image=img_5,padx=10,bg=col,command=pause_music) # where to keep
pause_button.place(x=148+28,y=35)

img_6 = Image.open('icons/resume.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6) #load image
resume_button = Button(button_frame,width=40,height=40,image=img_6,padx=10,bg=col,command=resume_music) # where to keep
resume_button.place(x=194+28,y=35)

img_7 = Image.open('icons/stop.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7) #load image
stop_button = Button(button_frame,width=40,height=40,image=img_7,padx=10,bg=col,command=stop_music) # where to keep
stop_button.place(x=240+28,y=35)

line = Label(left_frame,width=200,height=1,padx=10,bg=co3)
line.place(x=0,y=1)

line = Label(left_frame,width=200,height=1,padx=10,bg=col)
line.place(x=0,y=3)

running_song = Label(button_frame,text="Choose a Song",font=("Ivy 10"),width=44,height=1,padx=10,bg=col,fg=co3,anchor=NW)
running_song.place(x=0,y=1)


os.chdir(r'D:\Python\MusicPlayer\music') #load music directory using os module
songs = os.listdir() #convert directory in form of list
def show():
    for i in songs:
     listbox.insert(END,i) #insert song to list
show()

mixer.init()
music_state = StringVar()
music_state.set("Choose One")

window.mainloop()