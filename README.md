Text Translator GUI

A simple Text Translator GUI built using Python, Tkinter, and Google Translate API (via googletrans).
It allows you to input text, choose a language, and instantly get translations.

✨ Features

Translate text into multiple languages.

GUI interface with Tkinter (no command-line needed).

Supports Spanish, French, German, Hindi, Punjabi, Marathi, Telugu (easily extendable).

Translation caching for faster repeated lookups.

Error handling with logs saved in translator_errors.log.

🖼️ Demo (Example)

Input:

Hello, how are you?

Select Language: Hindi

Output:

Hindi Translation:
नमस्ते, आप कैसे हैं?

⚙️ Tech Stack

Python 3.12+

Tkinter → For GUI

googletrans → For translations

logging → Error handling and debugging

json (optional for extending language configs)


📦 Installation

Clone the repository:
git clone https://github.com/your-username/text-translator.git
cd text-translator

Install dependencies:
pip install googletrans==4.0.0-rc1

Run the app:
python translator.py

🛠️ How to Use

Launch the program.

Type/paste text in the input box.

Select the target language from the dropdown.

Click Translate.

View the translated text in the output box.
