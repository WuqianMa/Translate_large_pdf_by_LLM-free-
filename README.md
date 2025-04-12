# The Great Cosmic Mother – AI Chinese Translation Project

## 📖 What is this?

This is a personal project to translate the book **"The Great Cosmic Mother: Rediscovering the Religion of the Earth"** into **Chinese** using **free AI tools**.

The book, by Monica Sjöö and Barbara Mor, explores ancient goddess religions, Earth-based spirituality, and the roles of women in early culture. It combines mythology, history, and feminist insight.

---

## 🎯 Goal of This Project

- To provide a **free and open method** to translate large PDF books using AI  
- To demonstrate the use of **AI OCR + AI translation** for cultural and personal learning  
- To guide others in doing the same, even with basic coding skills  

---

## 🧠 Models Used

### 📜 `mistral-ocr-latest`

Used for OCR (extracting text from scanned PDFs or image-based documents)

- Can be run locally (e.g., via LM Studio) or via HuggingFace Spaces  
- Converts scanned pages to usable text or markdown  

### 🌐 `gemini-2.0-flash`

Used for translating English to Chinese

- Available via the Gemini API from Google  
- Free tier accessible at [https://gemini.google.com](https://gemini.google.com)  
- Works best on small text chunks  

---

## 🗂️ Translation Workflow

1. **Convert PDF to Text**  
   - Use `mistral-ocr-latest` to extract text from scanned pages  
   - Save the text as `.txt` or `.md`

2. **Split the Content**  
   - Break large text into smaller parts (e.g., 300–1000 words)

3. **Translate with `gemini-2.0-flash`**  
   - Use Gemini to translate each chunk  
   - Save the results to new files  

4. **Merge Translations**  
   - Combine all translated parts into full chapters  
   - Clean up formatting as needed  

---

## ⚙️ How to Set API Keys in the Command Line

If your code uses:
```python
import os
api_key = os.getenv("GOOGLE_API_KEY")
```
or
```python
api_key = os.getenv("MISTRAL_API_KEY")
```

You need to set those environment variables before running your script.

### 🪟 On Windows (Permanent Setup)

Use `setx` to save the keys permanently:
```cmd
setx GOOGLE_API_KEY "your_actual_key_here"
setx MISTRAL_API_KEY "your_actual_key_here"
```

🟡 **Important:** After using `setx`, you must **restart your Command Prompt or PowerShell** for the changes to take effect.

To check that it worked:
```cmd
echo %GOOGLE_API_KEY%
echo %MISTRAL_API_KEY%
```

### 🍎 On macOS or Linux (Temporary in Terminal)

```bash
export GOOGLE_API_KEY="your_actual_key_here"
export MISTRAL_API_KEY="your_actual_key_here"
python your_script.py
```

To set it permanently, add those `export` lines to your shell config file (`.bash_profile` or `.zshrc`), then run:
```bash
source ~/.zshrc
```

---

## ❗ Drawbacks and Limitations

- 📐 **Formatting loss**: Markdown structure (like headings and lists) may break during translation  
- 🌙 **Poetic tone**: Some symbolic or poetic language might not translate accurately  
- 🛠️ **Manual cleanup required**: OCR and translation are not perfect — you'll need to review and polish  
- 🧩 **Chunking needed**: Gemini works best on short inputs, so large texts must be split first  

---

## 📌 Why This Project?

- To explore feminist and spiritual wisdom across languages  
- To practice using AI for meaningful, low-cost cultural projects  
- To provide a free way to translate full books  

---

## 🔒 Legal Notice

This translation is intended for **private learning and cultural research only**.

The original book is protected by copyright.
