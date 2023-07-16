import subprocess

# Check if Python is installed
try:
    subprocess.run(["python", "--version"], check=True)
    print("Python is already installed.")
except FileNotFoundError:
    print("Python is not installed. Please install Python from https://www.python.org.")

# Check if PrettyMIDI is installed
try:
    import pretty_midi
    print("PrettyMIDI is already installed.")
except ImportError:
    print("PrettyMIDI is not installed. Installing PrettyMIDI...")
    subprocess.run(["pip", "install", "pretty_midi"])

# Check if Tkinter is installed
try:
    import tkinter
    print("Tkinter is already installed.")
except ImportError:
    print("Tkinter is not installed. Installing Tkinter...")
    subprocess.run(["pip", "install", "tk"])

# Continue with your code
import pretty_midi
from tkinter import Tk, Button, Entry, Label, filedialog
# Rest of your code...

import setuptools

setuptools.setup(
    name="pianotrans",
    version="1.0.1",
    author="Zhong Jianxin",
    author_email="azuwis@gmail.com",
    description="Simple GUI for ByteDance's Piano Transcription with Pedals",
    py_modules=["PianoTrans"],
    install_requires=[
        'piano_transcription_inference',
    ],
    entry_points={
        'console_scripts':[
            'pianotrans = PianoTrans:main',
        ],
    },
)
