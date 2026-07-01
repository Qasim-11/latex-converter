 # later disable printing and logging


import keyboard
# pyrefly: ignore [missing-import]
from PIL import Image
import os
# pyrefly: ignore [missing-import]
from PIL import ImageGrab
import pyperclip
# pyrefly: ignore [missing-import]
from plyer import notification
import tkinter as tk
import threading

from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Add your key lil bro")

# Initialize the client
client = genai.Client(api_key=api_key)

def grab_image_from_clipboard():
    img = ImageGrab.grabclipboard()
    if img is None:
        print("No image in clipboard!")
        return None
    # Convert image to RGB if it isn't
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img

def show_popup(message="Copied!", duration=2000):
    def popup():
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.configure(bg='black')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        width = 200
        height = 50
        x = screen_width - width - 10
        y = screen_height - height - 60
        root.geometry(f"{width}x{height}+{x}+{y}")

        label = tk.Label(root, text=message, bg='black', fg='white', font=("Arial", 12))
        label.pack(expand=True, fill='both')

        root.after(duration, root.destroy)
        root.mainloop()
    threading.Thread(target=popup).start()

def run_app():
    try:
        print("App is Running")
        img = grab_image_from_clipboard()

        if img is None:
            show_popup("No image found in clipboard", 2000)
            return
        
        print("Sending image to Gemma for processing...")
        show_popup("Processing image...", 3000)

        prompt = (
            "Convert the text and math formulas in this image into a mix of plain text and LaTeX. "
            "Use inline math ($...$) for inline formulas and display math ($$...$$) for standalone blocks. "
            "Use standards LaTeX syntax for all formulas. For example, use /exp(x) instead of e^x"
            "If mutliple formulas are present on the same line, use $formula$"
            "If mutliple formulas are present on different lines, you MUST use $$formula$$ in order to separate them."
            "Output ONLY the exact result. Do not include markdown code blocks like ```latex or ```."
        )
        
        response = client.models.generate_content(
            # model='gemma-4-26b-a4b-it',
            model = "gemini-3.1-flash-lite",
            contents=[prompt, img]
        )
        result = response.text.strip()
        
        pyperclip.copy(result)
        show_popup("u good", 2000)
        print("Text and formulas copied to clipboard:\n", result)

    except Exception as e:
        print("Error:", e)
        show_popup("An error occurred", 2000)


keyboard.add_hotkey('alt+c', run_app)

print("App initialized. Press alt+c to capture clipboard and convert. Press esc to quit.")
keyboard.wait('esc')  # Quit 
