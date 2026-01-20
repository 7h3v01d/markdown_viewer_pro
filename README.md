# Markdown Viewer Pro

A lightweight, standalone desktop Markdown viewer built with Python and Tkinter. It renders Markdown files with syntax-highlighted code blocks, tables, and clean styling using the `markdown2` and `tkinterweb` libraries.

---

⚠️ **LICENSE & USAGE NOTICE — READ FIRST**

This repository is **source-available for private technical evaluation and testing only**.

- ❌ No commercial use  
- ❌ No production use  
- ❌ No academic, institutional, or government use  
- ❌ No research, benchmarking, or publication  
- ❌ No redistribution, sublicensing, or derivative works  
- ❌ No independent development based on this code  

All rights remain exclusively with the author.  
Use of this software constitutes acceptance of the terms defined in **LICENSE.txt**.

---

Perfect for quickly previewing Markdown documents without needing a browser or heavy IDE.

![Markdown Viewer Screenshot](https://via.placeholder.com/800x500.png?text=Markdown+Viewer+Pro+Screenshot)  
*(Replace the placeholder with an actual screenshot after taking one)*

## Features

- **Fast Markdown rendering** with support for:
  - Fenced code blocks with syntax highlighting
  - Tables
  - Headings, lists, links, images, bold/italic, blockquotes
- **Clean, readable styling** with custom CSS (light theme by default)
- **Simple GUI** using Tkinter – no external browser required
- **Automatic dependency checking** – prompts to install missing packages if needed
- **Cross-platform** – works on Windows, macOS, and Linux (where Tkinter is available)
- **No internet connection required** after dependencies are installed

## Screenshot

![Screenshot of Markdown Viewer Pro](https://via.placeholder.com/800x500.png?text=Loaded+Markdown+File+in+Viewer)  
*(Add your own screenshots here)*

## Requirements

- Python 3.7 or higher
- Tkinter (included with standard Python installations on most systems)
- pip (for installing dependencies)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/markdown-viewer-pro.git
cd markdown-viewer-pro
```
### 2. (Recommended) Create a virtual environment
```Bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. Run the script
The script will automatically check for required dependencies and guide you through installation if they're missing.
```Bash
python markdown_viewer_pro.py
```
If dependencies are missing, it will:

Show the exact pip install command
Ask if you want to install them automatically
Exit gracefully if you decline

Manual dependency installation (if preferred)
```Bash
pip install markdown2>=2.4.0 tkinterweb>=3.17.0
```
Note: tkinterweb provides the HtmlFrame widget capable of rendering HTML with basic CSS support.

### Usage

1. Run the application:
```Bash
python markdown_viewer_pro.py
```
2. Click the "Load Markdown File" button.
3. Select any .md or .markdown file.
4. The rendered content appears instantly in the window with full styling and code highlighting.

You can resize the window, scroll, and load new files as needed.
Command-Line Options
```Bash
python markdown_viewer_pro.py --no-install
```
--no-install: Skip the automatic dependency installation prompt. The program will exit immediately if dependencies are missing.

Project Structure
textmarkdown-viewer-pro/
├── markdown_viewer_pro.py    # Main application script
├── README.md                # This file
├── LICENSE                  # (Recommended to add)
└── screenshots/             # (Optional folder for screenshots)
Known Limitations

Only supports a light theme currently (dark mode not implemented)
No live preview (file must be loaded manually)
No editing capabilities – view-only
Syntax highlighting is basic (via markdown2 extras)
Some advanced Markdown features (e.g., footnotes, task lists) may have limited support

### Future Ideas / Roadmap

- Add dark mode toggle
- Support drag-and-drop of Markdown files
- Live preview from clipboard or text input
- Export rendered HTML
- Custom CSS themes
- Search within document
- Recent files menu

### Contribution Policy

Feedback, bug reports, and suggestions are welcome.

You may submit:

- Issues
- Design feedback
- Pull requests for review

However:

- Contributions do not grant any license or ownership rights
- The author retains full discretion over acceptance and future use
- Contributors receive no rights to reuse, redistribute, or derive from this code

---

### License
This project is not open-source.

It is licensed under a private evaluation-only license.
See LICENSE.txt for full terms.
