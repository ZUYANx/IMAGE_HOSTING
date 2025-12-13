# IMAGE_UPLOADER

**Unlimited Image Hosting & Upload Tool**  
**Made By MR ZUYAN**
A terminal-based Python tool to upload images to the cloud using **FreeImage.host API**. Built with Python, SQLite3, and Rich for a beautiful CLI interface. Keep track of uploaded images with **local history**.

---

## Features
- Upload images to FreeImage.host using **base64 encoding**.
- Store uploaded image URLs in **SQLite3 database**.
- View upload history directly in the terminal.
- Beautiful, interactive terminal UI using **Rich**.
- Developed in **Bangladesh** by **MR ZUYAN** from **XVSOULX Team**.

---

## inside  
IMAGE UPLOADER ([-_-])
──────────────────────────────
➤ UPLOAD IMAGE    [1]
➤ VIEW HISTORY    [2]
➤ EXIT SYSTEM     [0]
──────────────────────────────
DEVELOPED BY: MR ZUYAN
──────────────────────────────

## Requirements

- **Python 3.x**
- **Libraries/Modules**:
  - `requests` → for HTTP requests to FreeImage.host API
  - `sqlite3` → for local database storage (built-in)
  - `os` → for file and system operations (built-in)
  - `base64` → for encoding images to upload (built-in)
  - `rich` → for terminal UI, prompts, and progress bars

---

## Install Dependencies

Run the following command to install all required external libraries:

```bash
pip install requests rich base64
