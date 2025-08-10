import os
import shutil
from pathlib import Path
from tkinter import Tk, filedialog

Files_Types = {
    'Image' : ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.doc','.docx','.pdf','.txt','.xls','.xlsx','.ppt','.pptx'],
    'Videos': ['.mp4', '.wav','.mov','.avi'],
    'Audio': ['.mp3','.wav','.aac','.flac'],
    'Archieves':['.zip','.rar','.7z','.tar','.gz']
}
def organize_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = Path(folder_path)/ file_name
        if file_path.is_file():
            moved = False
            for category,extentions in Files_Types.items():
                if file_path.suffix.lower() in extentions:
                    category_folder = Path(folder_path)/category
                    category_folder.mkdir(exist_ok = True)
                    shutil.move(str(file_path), str(category_folder / file_name))
                    moved = True
                    break
            if not moved:
                other_folder = Path(folder_path) / "Others"
                other_folder.mkdir(exist_ok = True)
                shutil.move(str(file_path), str(other_folder / file_name))

if __name__ == "__main__":
    Tk().withdraw()
    folder_selected = filedialog.askdirectory(title= "Select Folder to Organize")
    if folder_selected:
        organize_folder(folder_selected)
        print("Files Organized Successfully")
    else:
        print("No Folders Selected .")

