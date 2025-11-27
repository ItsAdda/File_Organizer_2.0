📂 File Organizer

A desktop application built with PySide6 that automatically organizes files in a folder based on their file sizes.
Keep your directories tidy and your workflow efficient.

✨ Features

📁 Automatic Sorting — organizes files into Small, Medium, Large folders

🗃️ Recursive Mode — optionally include subfolders

🖥️ Clean UI — modern, responsive, and intuitive layout

📊 Progress Bar — displays real-time progress during organization

⚠️ Safety Checks — prevents organizing system folders or protected paths

🔧 Customizable — modify file size thresholds easily

🚀 How to Run
1️⃣ Prerequisites

Make sure Python 3.10+ is installed:

python --version


Install PySide6:

pip install PySide6

2️⃣ Running the App

Navigate to the project folder and execute:

python main.py

🗂️ How It Works

The app scans the selected folder and sorts files based on size:

Small: under 10 MB

Medium: 10–200 MB

Large: over 200 MB

Example folder structure after organizing:

MyFolder/
 ├── Small/
 ├── Medium/
 ├── Large/
 ├── example.txt
 ├── video.mp4
 └── image.png

🧭 Planned Improvements

📝 Log window displaying moved files

🖱 Drag & drop folder selection

🔙 Undo last operation

📦 Additional sorting options (by type, date, etc.)

⚡ Performance optimization for large directories

🧰 Tech Stack

Python 3.10+

PySide6

OS & shutil modules

QThread for background processing

⚖️ License

Released under the MIT License — free to use, modify, and distribute with proper credit.

✨ Author

ItsAdda — Student & aspiring Python developer. Building practical tools to learn and improve.
