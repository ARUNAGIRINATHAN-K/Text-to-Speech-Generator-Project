import tkinter as tk
from tkinter import messagebox
import pyttsx3


class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Generator")
        self.root.geometry("400x300")
        
        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        
        # Create GUI elements
        tk.Label(root, text="Enter Text:").pack(pady=10)
        