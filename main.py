import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re


def strip_ansi(s):
    """Usuwa sekwencje ANSI (np. kolory z terminala)"""
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', s)


def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': save_path,
        'format': 'bv*+ba/b',
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        },
        'downloader_args': {
            'http': ['--impersonate', 'chrome'],
        },
        'nocolor': True  # opcjonalnie, by wyłączyć kolory ANSI
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_message.set("Finalizing...")
        progress_bar['value'] = 100
        root.update_idletasks()
        status_message.set("Download completed!")
        close_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        close_button.config(state=tk.NORMAL)


def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0.00%')
        percent_clean = strip_ansi(percent_str).strip('%')
        try:
            progress_bar['value'] = float(percent_clean)
        except ValueError:
            progress_bar['value'] = 0

        speed = strip_ansi(d.get('_speed_str', 'N/A'))
        eta = strip_ansi(d.get('_eta_str', 'N/A'))
        status_message.set(f"Downloading: {percent_clean}% at {speed}, ETA: {eta}")
        root.update_idletasks()

    elif d['status'] == 'finished':
        status_message.set("Merging video and audio...")


def select_path():
    save_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp4")
    if save_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, save_path)


def start_download():
    url = url_entry.get()
    save_path = path_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a video URL")
        return

    if not save_path:
        messagebox.showerror("Error", "Please select a save path")
        return

    status_message.set("Starting download...")
    close_button.config(state=tk.DISABLED)
    progress_bar['value'] = 0
    root.after(100, download_video, url, save_path)


def main():
    global root, status_message, progress_bar, url_entry, path_entry, close_button

    root = tk.Tk()
    root.title("📥 Video Downloader")
    root.geometry("600x350")

    tk.Label(root, text="Enter the video URL:").pack(pady=10)
    url_entry = tk.Entry(root, width=60)
    url_entry.pack(pady=5)

    tk.Label(root, text="Select save path:").pack(pady=10)
    path_frame = tk.Frame(root)
    path_frame.pack(pady=5)
    path_entry = tk.Entry(path_frame, width=50)
    path_entry.pack(side=tk.LEFT, padx=5)
    path_button = tk.Button(path_frame, text="Browse", command=select_path)
    path_button.pack(side=tk.LEFT)

    download_button = tk.Button(root, text="Download", command=start_download)
    download_button.pack(pady=10)

    progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
    progress_bar.pack(pady=10)

    status_message = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_message, wraplength=500)
    status_label.pack(pady=20)

    close_button = tk.Button(root, text="Close", command=root.quit, state=tk.DISABLED)
    close_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()