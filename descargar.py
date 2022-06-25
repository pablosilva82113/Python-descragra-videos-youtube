from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

#funciones para descargar
def slect_path():
    #seleccionar ruta descarga
    path= filedialog.askdirectory()
    path_lable.config(text=path)

def descargar():
    get_link = link_file.get()
    user_path = path_lable.cget("text")
    screen.title('Descargando....')
    #descargar video
    mp4_video =YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(mp4_video)
    vid_clip.close()

    shutil.move(mp4_video, user_path)
    screen.title('Descarga completa')




screen = Tk()
title = screen.title('YOUTUBE descragas')
canvas = Canvas(screen,width=500,height=500)
canvas.pack()

#cargar logo 
logo_img = PhotoImage(file='logo.png')
#ajustar logo
logo_img = logo_img.subsample(2,2)
canvas.create_image(250,80,image=logo_img)

#link para descargar
link_file =  Entry(screen,width=50)
link_lable = Label(screen,text="Ingresa el link para descargar" , font=('Arial',15))

#ruta para guradar los videos
path_lable = Label(screen,text="Selecciona la ruta para guradar los videos",font=('Arial',15))
slect_btn = Button(screen,text="Seleccionar",command=slect_path)

#ventana para ruta
canvas.create_window(250,280,window=path_lable)
canvas.create_window(250,330,window=slect_btn)


canvas.create_window(250,170,window=link_lable)
canvas.create_window(250,220,window=link_file)

#botones para descragar 

dwonload_btn = Button(screen,text="Descargar video",command=descargar)

#agreara al canvas los botones
canvas.create_window(250,390,window=dwonload_btn)

screen.mainloop()