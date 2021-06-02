"""
This is a program to download any youtube video with the video link
Made with Tkinter and Pytube
"""
import sys
import tkinter
import pytube

# Variables
root_hei = 350
root_wid = 500

# The window initialized in a variable 'root'
root = tkinter.Tk()

# Window configurations
root.geometry(f"{root_wid}x{root_hei}")
root.minsize(root_wid, root_hei)
root.tk.call()
root.iconphoto(False, tkinter.PhotoImage(file="py_icon.png"))
root.config(bg='yellow')
root.title("Youtube Video Downloader")


# ERROR WINDOW
def error():
    win = tkinter.Tk()
    win.geometry(f"{root_wid}x{root_hei}")
    win.minsize(root_wid, root_hei)

    root.title("Youtube Video Downloader...ERROR")

    l1 = tkinter.Label(win, text="Error", font="Verdana 18 bold", pady=10, fg='red')
    l1.pack(side=tkinter.TOP)

    win.mainloop()


# Variables
link_value = tkinter.StringVar()
radiobutton_variable = tkinter.IntVar()

# Label initialized
label1 = tkinter.Label(root, text="YOUTUBE DOWNLOADER", font="Verdana 18 bold", pady=10, fg='red', bg='yellow')
label1.pack(side=tkinter.TOP)
label2 = tkinter.Label(root, text="DOWNLOAD ANY YOUTUBE VIDEO:", font="Verdana 12 bold", pady=10, fg='light blue',
                       bg='yellow')
label2.pack()
label2 = tkinter.Label(root, text="Copy and Paste Your Youtube Link Here:", font="Verdana 9 bold underline", pady=10,
                       fg='black', bg='yellow')
label2.pack()

# Entry button
E1 = tkinter.Entry(root, textvariable=link_value, borderwidth=6, relief=tkinter.SUNKEN, width=60).pack(pady=30)

# Radio_buttons

b_low_p = tkinter.Radiobutton(root, text="low/medium resolution", variable=radiobutton_variable, value=0, bg='yellow') \
    .pack(anchor='sw')

b_high_p = tkinter.Radiobutton(root, text="high resolution", variable=radiobutton_variable, value=1, bg='yellow') \
    .pack(anchor='sw')


# Functions
def download_mp4():
    try:
        yt = pytube.YouTube(str(link_value.get()))
        if radiobutton_variable == 0:
            stream = yt.streams.filter(progressive=True, resolution="360p").first()
        else:
            stream = yt.streams.filter(progressive=True, resolution="720p").first()

        stream.download()
        print('Task Completed!')
    except:
        error()

    link_value.set("")
    sys.exit()


def download_mp3():
    try:
        yt = pytube.YouTube(str(link_value.get()))
        if radiobutton_variable == 0:
            stream = yt.streams.filter(only_audio=True, abr="160kbps").first()
        else:
            stream = yt.streams.filter(only_audio=True, abr="128kbps").first()

        stream.download()
        print('Task Completed!')
    except:
        error()

    link_value.set("")
    sys.exit()


# Download button:
b1 = tkinter.Button(root, text="download AUDIO+VIDEO", fg='red', bg='blue', borderwidth=7, relief=tkinter.GROOVE,
                    command=download_mp4)
b1.pack()

b1 = tkinter.Button(root, text="download JUST AUDIO", fg='red', bg='blue', borderwidth=7, relief=tkinter.GROOVE,
                    command=download_mp3)
b1.pack()

# Main loop initialised
root.mainloop()
