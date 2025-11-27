from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, \
    QSizePolicy, QCheckBox, QFileDialog, QMessageBox, QProgressBar
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QThread, Signal
import sys
import os
import shutil


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("File Organizer")
window.resize(800, 600)

v_layout = QVBoxLayout()
v_layout.addStretch(1)

# ---- TITLE LABEL ----
label = QLabel("File Organizer")
label.setFont(QFont("Montserrat", 36))
v_layout.addWidget(label, alignment=Qt.AlignCenter)
v_layout.addSpacing(40)

# ---- BUTTON ----
button = QPushButton("Browse Folder to Organize")
button.setFont(QFont("Open Sans", 28))
button.setMinimumWidth(500)
button.setMinimumHeight(80)
button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
v_layout.addWidget(button, alignment=Qt.AlignCenter)
v_layout.addSpacing(30)

# ---- OR LABEL ----
label_2 = QLabel("Or")
label_2.setFont(QFont("Open Sans", 28))
v_layout.addWidget(label_2, alignment=Qt.AlignCenter)
v_layout.addSpacing(30)

# ---- PATH ENTRY HORIZONTAL LAYOUT ----
h_layout = QHBoxLayout()
h_layout.addStretch(1)

label_3 = QLabel("Enter Path:")
label_3.setFont(QFont("Open Sans", 25))
h_layout.addWidget(label_3, alignment=Qt.AlignVCenter)

input_field = QLineEdit()
input_field.setFont(QFont("Open Sans", 25))
input_field.setFixedWidth(340)
h_layout.addWidget(input_field)
h_layout.addStretch(1)

v_layout.addLayout(h_layout)
v_layout.addSpacing(20)

# ---- CHECKBOX WITH UNCLICKABLE TEXT ----
checkbox_layout = QHBoxLayout()
checkbox_layout.addStretch(1)

checkBox = QCheckBox()
checkBox.setText("")
checkBox.setChecked(False)
checkBox.setFixedSize(45, 45)
checkBox.setStyleSheet("""
    QCheckBox::indicator {
        width: 45px;
        height: 45px;
    }
    QCheckBox::indicator:unchecked {
        image: url(Images/Unchecked.png);
    }
    QCheckBox::indicator:checked {
        image: url(Images/Checked.png);
    }
""")
checkbox_layout.addWidget(checkBox, alignment=Qt.AlignVCenter)


checkBox_label = QLabel("Organize subfolders")
checkBox_label.setFont(QFont("Open Sans", 25))
checkbox_layout.addWidget(checkBox_label, alignment=Qt.AlignVCenter)

checkbox_layout.addStretch(1)
v_layout.addLayout(checkbox_layout)

v_layout.addSpacing(20)

# ---- ORGANIZE BUTTON ----
Organize_button = QPushButton("Organize Folder")
Organize_button.setFont(QFont("Open Sans", 25))
v_layout.addWidget(Organize_button, alignment=Qt.AlignCenter)

v_layout.addStretch(10)

progress_bar = QProgressBar()
progress_bar.setValue(0)
progress_bar.setVisible(False)
progress_bar.setFixedHeight(40)
v_layout.addWidget(progress_bar)


window.setLayout(v_layout)
window.showMaximized()



sizes = {
    "small": 1024 * 1024 * 10,
    "medium": 1024 * 1024 * 200,
    "large": 1024 * 1024 * 1000
}


def show_popup(message, title="Notice"):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.exec()

class OrganizerThread(QThread):
    progress = Signal(int)
    done = Signal()

    def __init__(self, path, recursive):
        super().__init__()
        self.path = path
        self.recursive = recursive

    def count_files(self, root):
        total = 0
        for dirpath, _, filenames in os.walk(root):
            total += len(filenames)
            if not self.recursive:
                break
        return total

    def run(self):
        total_files = self.count_files(self.path)
        processed = 0

        for dirpath, _, filenames in os.walk(self.path):
            for file in filenames:
                full_path = os.path.join(dirpath, file)

                size = os.path.getsize(full_path)
                if size < sizes["small"]:
                    dest = os.path.join(dirpath, "Small")
                elif size <= sizes["medium"]:
                    dest = os.path.join(dirpath, "Medium")
                else:
                    dest = os.path.join(dirpath, "Large")

                os.makedirs(dest, exist_ok=True)
                shutil.move(full_path, dest)

                processed += 1
                self.progress.emit(int(processed / total_files * 100))

            if not self.recursive:
                break

        self.done.emit()

def browse_folder():
    folder_path = QFileDialog.getExistingDirectory(
        window,
        "Select Folder to Organize",
    )
    if folder_path:
        system_paths = [os.environ.get("WINDIR", "C:\\Windows"), "C:\\Program Files", "C:\\Program Files (x86)", "C:\\System64", "C:\\System32", "C:\\System"]
        folder_abs = os.path.abspath(folder_path)
        if any(folder_abs.startswith(sp) for sp in system_paths):
            show_popup("Cannot organize system folders!", "Permission Error")
            return
        if not os.access(folder_abs, os.W_OK):
            show_popup("You don't have write permission for this folder!", "Permission Error")
            return
        input_field.setText(folder_abs)



def start_organizing():
    path = input_field.text()

    if not os.path.exists(path):
        show_popup("Folder not found")
        return

    progress_bar.setValue(0)
    progress_bar.setVisible(True)

    global worker
    worker = OrganizerThread(path, checkBox.isChecked())
    worker.progress.connect(progress_bar.setValue)
    worker.done.connect(lambda: show_popup("Finished organizing!"))
    worker.done.connect(lambda: progress_bar.setVisible(False))

    worker.start()






button.clicked.connect(browse_folder)
Organize_button.clicked.connect(start_organizing)


if __name__ == "__main__":
    checkBox.setChecked(False)
    app.exec()
