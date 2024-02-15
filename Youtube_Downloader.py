import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

root = tk.Tk()

root.title("Youtube Downloader")
root.geometry("600x460")
root.resizable(False, False)  # Use lowercase 'false' for non-resizable

def browse():
    directory = filedialog.askdirectory(title="Save Video")
    folderLink.delete(0, "end")
    folderLink.insert(0, directory)

def down_yt():
    link = ytLink.get()
    folder = folderLink.get()
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        if stream:
            stream.download(folder)
            print("Download completed successfully.")
        else:
            print("No stream available for the provided link.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Logo
ytLogo = tk.PhotoImage(file="img/Logo.png").subsample(1)
ytTitle = tk.Label(root, image=ytLogo)
ytTitle.place(relx=0.5, rely=0.25, anchor="center")

# Youtube Link
ytLabel = tk.Label(root, text="Youtube Link")  
ytLabel.place(x=25, y=310)

ytLink = tk.Entry(root, width=60)
ytLink.place(x=140, y=310)

# Download Folder
folderLabel = tk.Label(root, text="Download Folder")
folderLabel.place(x=25, y=343)

folderLink = tk.Entry(root, width=50)
folderLink.place(x=140, y=343)

# Browse Button
browseButton = tk.Button(root, text="Browse", command=browse)  # Renamed button variable to avoid conflict
browseButton.place(x=455, y=340)

downloadButton = tk.Button(root, command=down_yt, text="Download")
downloadButton.place(x=280, y=380)

root.mainloop()
