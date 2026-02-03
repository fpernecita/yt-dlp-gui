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

    def create_widgets(self):
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
        
        # Download path
        ttk.Label(main_frame, text="Save to:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.path_entry = ttk.Entry(main_frame, width=40)
        self.path_entry.insert(0, DEFAULT_DOWNLOAD_PATH)
        self.path_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        browse_btn = ttk.Button(main_frame, text="Browse", command=self.browse_folder)
        browse_btn.grid(row=1, column=2, padx=(5, 0), pady=5)
        
        # Audio format selection
        ttk.Label(main_frame, text="Format:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.format_var = tk.StringVar(value="mp3")
        format_combo = ttk.Combobox(main_frame, textvariable=self.format_var, 
                                     values=["mp3", "m4a", "wav", "flac"], 
                                     state="readonly", width=10)
        format_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
    
                # Download button
        self.download_btn = ttk.Button(main_frame, text="Download", 
                                       command=self.start_download)
        self.download_btn.grid(row=3, column=0, columnspan=3, pady=20)
        
                # Progress bar
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate', length=400)
        self.progress_bar.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready", foreground="blue")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # Info text
        info_text = tk.Text(main_frame, height=6, width=60, wrap=tk.WORD)
        info_text.grid(row=6, column=0, columnspan=3, pady=10)
        info_text.insert(tk.END, 
            "Instructions:\n"
            "1. Paste the video URL\n"
            "2. Choose where to save the file\n"
            "3. Select audio format\n"
            "4. Click Download\n"
            "\nNote: Make sure yt-dlp is installed (pip install yt-dlp)")
        info_text.config(state=tk.DISABLED)


    def browse_folder(self):
        """Open folder browser dialog"""
        folder = filedialog.askdirectory(initialdir=self.path_entry.get())
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
    
    def update_progress():

    def start_download(self):


def main():
    
if __name__ == "__main__":
    main()