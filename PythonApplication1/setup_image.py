import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
static_folder = script_dir / "static"
static_folder.mkdir(exist_ok=True)

# Open file browser to select image
root = tk.Tk()
root.withdraw()

source = filedialog.askopenfilename(
    title="Select your photo",
    initialdir=str(Path.home() / "Downloads"),
    filetypes=[("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")]
)

if source:
    destination = static_folder / "photo.jpg"
    shutil.copy(source, destination)
    print(f"✓ Image copied successfully!")
    print(f"✓ Location: {destination}")
    print(f"\nNow run your Flask app - the image should appear!")
else:
    print("✗ No image selected")