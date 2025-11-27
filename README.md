📂 File Organizer 2.0

A simple PySide6 desktop tool that automatically organizes files in a folder based on their file sizes (Small, Medium, Large).
Made to keep your messy directories under control because you clearly weren’t doing it yourself.

Still a work in progress, but already fully usable — clean UI, smooth behavior, and runs without freezing thanks to threading.

✨ Features

📁 Automatic Sorting — organizes files into Small / Medium / Large folders
🗃️ Recursive Mode — option to include subfolders
🖥️ Modern UI — built with PySide6, clean and centered layout
📊 Progress Bar — shows real-time progress while files move
⚠️ Safety Checks — prevents organizing system folders or protected paths
🔧 Easy to Modify — clear code structure, customizable thresholds

🚀 How to Run
1️⃣ Prerequisites

Make sure you have Python 3.10+ installed.

Check with:

python --version


If you don’t have it, get it from python.org.

2️⃣ Install Dependencies
pip install PySide6

3️⃣ Run the Program

Navigate to your project folder and run:

python File_Organizer.py

🗂️ How It Works

The app scans the selected folder (and optionally its subfolders).
Each file gets measured and moved into one of these:

Small (under 10 MB)

Medium (10–200 MB)

Large (200 MB+)

Resulting structure example:

MyFolder/
 ├── Small/
 ├── Medium/
 ├── Large/
 ├── yourfile.txt
 ├── video.mp4
 └── image.png

🧭 Planned Improvements

📝 Log window showing moved files
🖱 Drag & drop folder selection
🔙 Undo last operation
📦 Custom sorting modes (by type, by date, etc.)
⚡ Faster scanning & batching

🧰 Tech Stack

Python 3

PySide6

OS & shutil modules

QThread for background tasks

⚖️ License

Released under MIT License — feel free to use or modify it.
Just credit ItsAdda.

✨ Author

ItsAdda — student & aspiring Python developer.
Learning by building real, useful tools.
