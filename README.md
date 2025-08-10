# 📂 File Organizer

A simple yet powerful **Python-based File Organizer** with a **Graphical User Interface (GUI)** to quickly sort files in a folder into categorized subfolders based on file extensions.  
Perfect for cleaning up your messy "Downloads" or any other directory in seconds!

---

## 🚀 Features
- **One-click folder selection** — select any folder from your system using a dialog box.
- **Automatic file categorization** — sorts files into predefined categories like:
  - **Images** (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, etc.)
  - **Videos** (`.mp4`, `.mkv`, `.avi`, `.mov`, etc.)
  - **Documents** (`.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx`, etc.)
  - **Audio** (`.mp3`, `.wav`, `.aac`, `.flac`, etc.)
  - **Compressed** (`.zip`, `.rar`, `.7z`, `.tar`, `.gz`, etc.)
  - **Others** (uncategorized files)
- **Cross-platform support** — works on Windows, macOS, and Linux.
- **Fast & lightweight** — no heavy dependencies.

---

## 📂 Project Structure
File Organizer/
│
├── file_organizer.py # Main Python script
├── README.md # Project documentation
├── demo_video.mp4 # Screen recording of the project in action

---

▶ Usage
1️⃣ Run the program
bash
Copy
Edit
python file_organizer.py
2️⃣ Select a folder
A dialog box will appear.

Choose the folder you want to organize.

3️⃣ Done! 🎉
Files will be automatically moved into categorized subfolders inside the same directory.


📌 Example Output
Before:
Downloads/
│ file1.jpg
│ movie.mp4
│ resume.pdf
│ song.mp3
│ randomfile.xyz
After running the program:

arduino
Copy
Edit
Downloads/
│
├── Images/
│   └── file1.jpg
│
├── Videos/
│   └── movie.mp4
│
├── Documents/
│   └── resume.pdf
│
├── Audio/
│   └── song.mp3
│
├── Others/
│   └── randomfile.xyz


## Demo Video
You can watch the demo video of this project here: [Watch on Google Drive](https://drive.google.com/file/d/14AR9IYdebYZ7XKzKVtqQrjGh6lv9leak/view?usp=drive_link)


📜 License
This project is licensed under the MIT License — feel free to use, modify, and share.

💡 Author
Developed by Harsh as a Python project for learning and practical use.
If you like this project, consider ⭐ starring the repo!