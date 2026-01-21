# 🖥️ XENOS OS - System Information GUI

A sleek and modern graphical user interface for retrieving comprehensive system information and managing your computer. Built with Python and Tkinter for cross-platform compatibility.

## 📋 Features

- **🖥️ System Information**: Display OS, processor, and memory details
- **👤 User Information**: View current user and home directory
- **🗓️ Date & Time**: Show current date and time
- **🌐 Local IP Address**: Retrieve your machine's local IP
- **🌍 Public IP Address**: Fetch your public IP from the internet
- **📁 List Files**: Display files in the current directory
- **📂 Create Directory**: Create new folders easily
- **🎨 Modern Dark Theme**: Professional dark UI with cyan accents
- **✨ Hover Effects**: Interactive button animations
- **📊 Live Console Output**: Real-time display of command results

## 🎯 Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- psutil
- requests

## 📦 Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com/yourusername/xenos-os-gui.git
   cd xenos-os-gui
   ```

2. **Install dependencies**:
   ```bash
   pip install psutil requests
   ```

3. **Run the application**:
   ```bash
   python xenosguifinal.py
   ```

## 🚀 Usage

1. Launch the application by running `xenosguifinal.py`
2. Click any button to retrieve the corresponding system information
3. Results display in the console output window
4. The console automatically scrolls to show the latest output
5. Click **Exit** to close the application

### Available Commands

| Button | Function | Output |
|--------|----------|--------|
| 🖥️ System Info | Displays OS, processor, and total memory | System details |
| 👤 User Info | Shows current user and home directory | User details |
| 🗓️ Date/Time | Displays current date and time | Current datetime |
| 🌐 Local IP | Retrieves your local network IP | Local IP address |
| 🌍 Public IP | Fetches your public IP from the internet | Public IP address |
| 📁 List Files | Shows files in current directory | File listing |
| 📂 Create Folder | Creates a new directory named "test_dir" | Confirmation message |
| ❌ Exit | Closes the application | N/A |

## 🎨 User Interface

### Design Features

- **Dark Theme**: Easy on the eyes with professional appearance
- **Color Scheme**:
  - Background: Dark gray (#1e1e2e)
  - Buttons: Ocean blue (#0078d4)
  - Accent: Cyan (#00d9ff)
  - Exit Button: Red (#c41e3a)
  
- **Layout**:
  - Organized button grid (3 columns)
  - Header section with title and description
  - Scrollable console output area
  - Responsive window design

### Interactive Elements

- **Hover Effects**: Buttons brighten when you hover over them
- **Hand Cursor**: Changes to hand pointer on button hover
- **Auto-scroll Console**: Output automatically scrolls to show latest results
- **Resizable Window**: Adjust window size to your preference

## 🔧 Technical Details

### Dependencies

- **tkinter**: GUI framework (included with Python)
- **psutil**: System and process utilities
- **requests**: HTTP library for public IP lookup
- **os, platform, socket, getpass, datetime**: Python standard library

### Architecture

- Modular function design for each system information command
- Centralized output display system
- Reusable button creation helper function
- Clean separation of UI and functionality

## 📝 Example Output

```
> sysinfo
System: Windows 10
Processor: Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz
Memory: 32.00 GB

> userinfo
User: liltr
Home Directory: C:\Users\liltr

> ip
Local IP Address: 192.168.1.100
```

## 💻 System Compatibility

- ✅ Windows (7, 10, 11, etc.)
- ✅ macOS
- ✅ Linux (Ubuntu, Fedora, Debian, etc.)

## 🛠️ Customization

You can easily customize the application by modifying:

1. **Colors**: Edit the color scheme at the top of the file (BG_COLOR, BUTTON_COLOR, etc.)
2. **Window Size**: Change the `geometry()` parameter
3. **Fonts**: Modify font names and sizes in button creation
4. **Buttons**: Add new commands by creating functions and adding buttons in the buttons_frame section

## 📄 License

This project is provided as-is for educational and personal use.

## 👨‍💻 Author

Created for system information retrieval and demonstration purposes.

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'psutil'"
- Solution: Install psutil with `pip install psutil`

### "ModuleNotFoundError: No module named 'requests'"
- Solution: Install requests with `pip install requests`

### Public IP button not working
- Solution: Check your internet connection. The app attempts to reach an external IP service.

### Window not displaying properly
- Solution: Ensure tkinter is installed. On Linux, run `sudo apt-get install python3-tk`

## 📬 Feedback

Feel free to fork, modify, and submit pull requests to improve this project!

---

**Enjoy exploring your system with XENOS OS GUI! 🚀**
