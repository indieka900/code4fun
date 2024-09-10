import tkinter
import customtkinter
from pytube import YouTube

def downloadV():
    try:
        finishedLabel.configure(text="")
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color = "white")
        video.download()
    except:
        finishedLabel.configure(text="Download Error!", text_color="red")
        return
    finishedLabel.configure(text="Downloaded!")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complition = bytes_downloaded / total_size * 100
    per = str(int(percentage_complition))
    pPercentage.configure(text=per+'%')
    pPercentage.update()
    
    #update progress bar
    progressBar.set(float(percentage_complition) / 100)
    progressBar.update()
    

#Systems Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link", text_color="brown")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#download button
downloadB = customtkinter.CTkButton(app, text="Download", command=downloadV)
downloadB.pack(padx=10, pady=10)

#progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack(pady=20)

#progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.0)
progressBar.pack(pady=10)

#finished downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack(pady=10)

#run app
app.mainloop()