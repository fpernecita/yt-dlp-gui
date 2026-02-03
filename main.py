import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from downloader import Downloader
from config import DEFAULT_DOWNLOAD_PATH

class YtDlpGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("yt-dlp Audio Downloader")
        self.root.geometry("600x400")
        # initialise downloader
        self.downloader = Downloader()
        self.downloader.set_progress_callback(self.update_progress)
        # call widget creation
        self.create_widgets()

    def create_widgets():
        # create all the widgets
                # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
                # URL input
        ttk.Label(main_frame, text="Video URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        
    def browse_folder():
    
    def update_progress():

    def start_download(self):


def main():
    
if __name__ == "__main__":
    main()