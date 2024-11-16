#pseudo code
# from translate import Translator
# translator = Translator(to_lang='es')  #Spanish
# #Text to be translated
# text = "Hello, how are you?"
# translation = translator.translate(text)
# print('Translated text:', translation)

from googletrans import Translator, LANGUAGES
import tkinter as tk
import json
import logging

# Set up logging for error handling
logging.basicConfig(filename='translator_errors.log', level=logging.ERROR)

# Dictionary of supported languages for display
languages = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Punjabi': 'pa',
    'Marathi': 'mr',
    'Telugu': 'te'
}

# Reverse dictionary to map language names back to their codes
language_codes = {name: code for name, code in languages.items()}

# Cache to store translations for faster access
translation_cache = {}

# Function to translate text with caching
def cached_translate(text, language_code):
    if text in translation_cache:
        return translation_cache[text]
    try:
        # Set up the Translator with alternate service URLs
        translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
        translation = translator.translate(text, dest=language_code).text
        translation_cache[text] = translation
        return translation
    except Exception as e:
        logging.error(f"Error translating '{text}' to {language_code}: {e}")
        print(f"Error: {e}")  # Debugging output to see errors directly
        return "Translation failed. Check logs for details."

# GUI for the translator
def translate_text():
    language_name = language_var.get()
    language_code = language_codes[language_name]  # Get language code from selected language name
    text = input_text.get("1.0", tk.END).strip()
    translation = cached_translate(text, language_code)
    output_text.delete("1.0", tk.END)
    
    # Display the language name along with the translation
    output_text.insert(tk.END, f"{language_name} Translation:\n{translation}")

# Tkinter setup for GUI
root = tk.Tk()
root.title("Text Translator")

# Language selection dropdown
language_var = tk.StringVar(root)
language_var.set("Spanish")  # default language
tk.Label(root, text="Choose Language:").pack()
language_menu = tk.OptionMenu(root, language_var, *languages.keys())  # Display language names 
language_menu.pack()

# Input and output text boxes
input_text = tk.Text(root, height=5)
input_text.pack()
tk.Button(root, text="Translate", command=translate_text).pack()
output_text = tk.Text(root, height=5)
output_text.pack()

# Run the Tkinter main loop
root.mainloop() 

