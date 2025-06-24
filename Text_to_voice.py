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
        
        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack(pady=10)
        
        # Voice selection
        tk.Label(root, text="Select Voice:").pack(pady=5)
        self.voice_var = tk.StringVar()
        self.voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in self.voices]
        self.voice_menu = tk.OptionMenu(root, self.voice_var, *voice_names)
        self.voice_menu.pack(pady=5)
        if voice_names:
            self.voice_var.set(voice_names[0])
        