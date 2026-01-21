import os
import platform
import getpass
import psutil
import datetime
import socket
import requests
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkFont

# 🎨 Color Scheme
BG_COLOR = "#1e1e2e"
FG_COLOR = "#ffffff"
BUTTON_COLOR = "#0078d4"
BUTTON_HOVER = "#1084d7"
ACCENT_COLOR = "#00d9ff"
HEADER_COLOR = "#0d47a1"

# 🖥️ Function to Handle Commands and Display Results
def display_output(command, output):
    output_text.config(state=tk.NORMAL)  # Enable text editing
    output_text.insert(tk.END, f"\n> {command}\n{output}\n")
    output_text.see(tk.END)  # Auto-scroll to bottom
    output_text.config(state=tk.DISABLED)  # Disable editing

def on_button_enter(button):
    button.config(bg=BUTTON_HOVER)

def on_button_leave(button):
    button.config(bg=BUTTON_COLOR)

def sysinfo():
    system_info = f"System: {platform.system()} {platform.release()}\n"
    system_info += f"Processor: {platform.processor()}\n"
    system_info += f"Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB\n"
    display_output("sysinfo", system_info)

def userinfo():
    user_info = f"User: {getpass.getuser()}\nHome Directory: {os.path.expanduser('~')}\n"
    display_output("userinfo", user_info)

def datetime_info():
    current_datetime = f"Current Date & Time: {datetime.datetime.now()}\n"
    display_output("datetime", current_datetime)

def local_ip():
    ip = socket.gethostbyname(socket.gethostname())
    display_output("ip", f"Local IP Address: {ip}\n")

def public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        display_output("public_ip", f"Public IP Address: {response.json()['ip']}\n")
    except:
        display_output("public_ip", "Unable to fetch public IP.\n")

def list_files():
    files = "\n".join(os.listdir(".")) + "\n"
    display_output("ls", files)

def create_directory():
    dir_name = "test_dir"
    os.makedirs(dir_name, exist_ok=True)
    display_output("mkdir", f"Directory '{dir_name}' created.\n")

def exit_program():
    root.quit()

def create_button(parent, text, command, row, column, columnspan=1):
    """Helper function to create styled buttons"""
    btn = tk.Button(
        ext,
        command=cparent,
        text=tommand,
        bg=BUTTON_COLOR,
        fg=FG_COLOR,
        font=("Arial", 11, "bold"),
        relief=tk.FLAT,
        padx=15,
        pady=12,
        cursor="hand2",
        activebackground=BUTTON_HOVER,
        activeforeground=FG_COLOR
    )
    btn.grid(row=row, column=column, columnspan=columnspan, padx=8, pady=8, sticky="ew")
    btn.bind("<Enter>", lambda e: on_button_enter(btn))
    btn.bind("<Leave>", lambda e: on_button_leave(btn))
    return btn

# 🎨 Create GUI Window
root = tk.Tk()
root.title("🖥️ Xenos OS - System Utility GUI")
root.geometry("700x600")
root.config(bg=BG_COLOR)
root.resizable(True, True)

# 🎯 Header Frame
header_frame = tk.Frame(root, bg=HEADER_COLOR, height=80)
header_frame.pack(fill=tk.X, pady=(0, 0))
header_frame.pack_propagate(False)

title_font = tkFont.Font(family="Arial", size=16, weight="bold")
title_label = tk.Label(
    header_frame,
    text="🖥️ XENOS OS - System Information Hub",
    font=title_font,
    bg=HEADER_COLOR,
    fg=ACCENT_COLOR
)
title_label.pack(pady=10)

subtitle_font = tkFont.Font(family="Arial", size=9)
subtitle_label = tk.Label(
    header_frame,
    text="Retrieve system information and manage your computer",
    font=subtitle_font,
    bg=HEADER_COLOR,
    fg=FG_COLOR
)
subtitle_label.pack()

# 🎮 Main Content Frame
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

# 📋 Buttons Frame with Grid Layout
buttons_frame = tk.Frame(main_frame, bg=BG_COLOR)
buttons_frame.pack(fill=tk.X, pady=(0, 10))

# Configure grid columns for responsive layout
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
buttons_frame.columnconfigure(2, weight=1)

# 🎮 Command Buttons organized in groups
create_button(buttons_frame, "🖥️ System Info", sysinfo, 0, 0)
create_button(buttons_frame, "👤 User Info", userinfo, 0, 1)
create_button(buttons_frame, "🗓️ Date/Time", datetime_info, 0, 2)

create_button(buttons_frame, "🌐 Local IP", local_ip, 1, 0)
create_button(buttons_frame, "🌍 Public IP", public_ip, 1, 1)
create_button(buttons_frame, "📁 List Files", list_files, 1, 2)

create_button(buttons_frame, "📂 Create Folder", create_directory, 2, 0, columnspan=2)
exit_btn = create_button(buttons_frame, "❌ Exit", exit_program, 2, 2)
exit_btn.config(bg="#c41e3a")
exit_btn.bind("<Enter>", lambda e: on_button_enter(exit_btn) or exit_btn.config(bg="#e81828"))
exit_btn.bind("<Leave>", lambda e: on_button_leave(exit_btn) or exit_btn.config(bg="#c41e3a"))

# 📜 Output Console Label
console_label = tk.Label(main_frame, text="📊 Console Output", font=("Arial", 10, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
console_label.pack(anchor="w", pady=(10, 5))

# 📜 Output Console
output_text = scrolledtext.ScrolledText(
    main_frame,
    width=85,
    height=18,
    state=tk.DISABLED,
    bg="#262626",
    fg="#00ff00",
    font=("Courier New", 9),
    relief=tk.FLAT,
    borderwidth=2
)
output_text.pack(fill=tk.BOTH, expand=True)

# 🚀 Run GUI
root.mainloop()
