import os
import shutil
from pathlib import Path
from tkinter import Tk, filedialog

# Dictionary that defines file categories and their corresponding extensions
Files_Types = {
    'Image' : ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.doc','.docx','.pdf','.txt','.xls','.xlsx','.ppt','.pptx'],
    'Videos': ['.mp4', '.wav','.mov','.avi'],
    'Audio': ['.mp3','.wav','.aac','.flac'],
    'Archives':['.zip','.rar','.7z','.tar','.gz']
}

def organize_folder(folder_path):
    """
    Organizes files in the given folder into categorized subfolders
    based on their extensions (Images, Documents, Videos, etc.)
    """
    for file_name in os.listdir(folder_path):  # Loop through all files in the folder
        file_path = Path(folder_path) / file_name  # Get full file path
        
        if file_path.is_file():  # Process only files, not subdirectories
            moved = False  # Flag to check if file was moved to a category

            # Loop through file type categories
            for category, extensions in Files_Types.items():
                # If file extension matches the category, move it
                if file_path.suffix.lower() in extensions:
                    category_folder = Path(folder_path) / category
                    category_folder.mkdir(exist_ok=True)  # Create category folder if not exists
                    shutil.move(str(file_path), str(category_folder / file_name))  # Move file
                    moved = True
                    break
            
            # If file does not match any category, move it to "Others"
            if not moved:
                other_folder = Path(folder_path) / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(other_folder / file_name))

if __name__ == "__main__":
    Tk().withdraw()  # Hide the main Tkinter window
    # Open a dialog box to select folder
    folder_selected = filedialog.askdirectory(title="Select Folder to Organize")

    if folder_selected:
        organize_folder(folder_selected)  # Call function to organize files
        print("Files Organized Successfully")
    else:
        print("No Folder Selected.")
