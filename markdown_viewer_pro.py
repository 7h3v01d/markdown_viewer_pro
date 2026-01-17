import sys
import subprocess
import os
from typing import Set, List, Dict, Union
import argparse  # Built-in, no dependency needed for basic parsing
import importlib.util

# --- SECTION 1: DEPENDENCY MANAGEMENT ---
# Define the required dependencies here with version specs. This is the only part you need to change.
REQUIRED_DEPENDENCIES = {
    "markdown2": "markdown2>=2.4.0",
    "tkinterweb": "tkinterweb>=3.17.0",
    # tkinter is part of the Python standard library, so no need to include it here
}

def check_and_install_dependencies(args) -> None:
    """
    Checks for required dependencies and prompts the user to install them if missing.
    """
    missing_deps = []
    
    # Check for each dependency using importlib for safer module existence check
    for import_name, package_spec in REQUIRED_DEPENDENCIES.items():
        if importlib.util.find_spec(import_name) is None:
            # If the module is not found, add the package spec to our list of missing dependencies.
            missing_deps.append(package_spec)

    # If the list is not empty, it means we found missing packages.
    if missing_deps:
        print("❌ Error: Missing dependencies required to run this program.")
        print("Please install them in your environment by running the following command:")
        
        python_executable = sys.executable
        
        # Suggest --user if not in venv for safer user-level installation
        in_venv = sys.prefix != sys.base_prefix
        user_flag = "--user" if not in_venv else ""
        install_command = f"{python_executable} -m pip install {user_flag} {' '.join(missing_deps)}"
        
        print(f"\n   `{install_command}`\n")
        
        print("⚠️ Warning: Installing packages can pose security risks. Consider using a virtual environment (venv) for isolation.")
        print("For more info: https://docs.python.org/3/library/venv.html")
        
        if args.no_install:
            print("Skipping installation due to --no-install flag.")
            sys.exit(1)
        
        # Optionally, provide a way for the user to install automatically
        if sys.stdin and sys.stdin.isatty():
            install_now = input("Would you like to install them now? (y/n): ").lower()
            if install_now == 'y':
                print("⏳ Installing dependencies...")
                try:
                    # Verify pip is available to avoid errors during installation
                    import pip  # This will raise ImportError if pip is missing
                    
                    result = subprocess.run(
                        [python_executable, '-m', 'pip', 'install', user_flag, *missing_deps],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode != 0:
                        print("❌ Installation failed. Output:")
                        print(result.stdout + result.stderr)
                        print("Please run the command manually.")
                    else:
                        print("✅ Dependencies installed successfully. Please re-run the program.")
                except ImportError:
                    print("❌ Error: pip is not available. Please install pip manually or use a full Python installation.")
                except Exception as e:
                    print(f"❌ An unexpected error occurred: {e}")
                sys.exit(1)
        
        sys.exit(1)

# Parse arguments early (using built-in argparse) for flags like --no-install
parser = argparse.ArgumentParser(description="Markdown Viewer with dependency management.")
parser.add_argument('--no-install', action='store_true', help='Skip installation prompt and exit if dependencies are missing.')
args = parser.parse_args()

# Call the dependency check function immediately after its definition.
# This ensures it runs as the very first step of your program.
check_and_install_dependencies(args)

# --- SECTION 2: IMPORTING REQUIRED LIBRARIES ---
# Now that we have confirmed all dependencies are available, we can safely
# import them here. This section should include all the third-party libraries
# your program's core logic will use.

import tkinter as tk
from tkinter import filedialog
import markdown2
from tkinterweb.htmlwidgets import HtmlFrame
from rich.console import Console

# --- SECTION 3: YOUR MAIN PROGRAM LOGIC ---
# This is where the core of your program goes. You can define functions, classes,
# and other logic here, confident that all necessary libraries are imported
# and ready to use.

def load_markdown_file(html_frame, console):
    """
    Loads and renders a Markdown file into the HtmlFrame widget.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md *.markdown")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
                console.print(f"[bold green]Loaded Markdown file: {file_path}[/bold green]")
                # Convert Markdown to HTML with enhanced extras for code blocks
                html_content = markdown2.markdown(markdown_content, extras=["fenced-code-blocks", "codehilite", "tables"])
                # Add custom CSS
                styled_html = f"""
                <style>
                    body {{
                        font-family: 'Helvetica', 'Arial', sans-serif;
                        background-color: #ffffff;
                        color: #000000;
                        margin: 20px;
                        line-height: 1.6;
                    }}
                    h1 {{
                        font-size: 2em;
                        color: #000000;
                        border-bottom: 1px solid #000000;
                        padding-bottom: 0.3em;
                    }}
                    code {{
                        font-family: 'Consolas', 'Courier New', monospace;
                        background-color: #f0f0f0;
                        padding: 2px 4px;
                    }}
                    pre {{
                        font-family: 'Consolas', 'Courier New', monospace;
                        background-color: #f0f0f0;
                        padding: 16px;
                    }}
                </style>
                {html_content}
                """
                # Load styled HTML
                html_frame.load_html(styled_html)
        except Exception as e:
            console.print(f"[bold red]❌ Error loading file: {str(e)}[/bold red]")
            html_frame.load_html(f"<h3>Error</h3><p>Could not load file: {str(e)}</p>")

def main() -> None:
    """
    This is the main entry point for the Markdown Viewer program.
    """
    console = Console()
    console.print("[bold green]✅ Markdown Viewer is starting...[/bold green]")
    
    try:
        # Create the main window
        root = tk.Tk()
        root.title("Markdown Viewer with Styles")
        root.geometry("800x600")

        # Create a button to load the Markdown file
        load_button = tk.Button(root, text="Load Markdown File", command=lambda: load_markdown_file(html_frame, console))
        load_button.pack(pady=10)

        # Create an HtmlFrame to display the rendered Markdown
        html_frame = HtmlFrame(root, messages_enabled=False)
        html_frame.pack(fill="both", expand=True)

        # Start the Tkinter event loop
        root.mainloop()
    except Exception as e:
        console.print(f"[bold red]❌ An error occurred: {str(e)}[/bold red]")

# --- SECTION 4: PROGRAM ENTRY POINT ---
# This standard Python idiom ensures that your `main` function is called
# only when the script is executed directly, not when it's imported as a module
# into another script.

if __name__ == "__main__":
    main()