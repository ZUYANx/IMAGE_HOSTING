import base64
import requests
import sqlite3
import os
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
#DEVELOPED by : MR ZUYAN
#Team : XVSOULX
#Facebook : unknown
#if you edit please give credit 
console = Console()
API_KEY = "6d207e02198a847aa98d0a2a901485a5"
DB_FILE = "images.db"

# Database setup
conn = sqlite3.connect(DB_FILE)
conn.execute("CREATE TABLE IF NOT EXISTS images (image_url TEXT)")
conn.commit()

def clear_screen():
    os.system('clear')

def show_menu():
    clear_screen()
    
    console.print("[bold cyan]IMAGE UPLOADER ([-_-])[/bold cyan]")
    console.print("─" * 30)
    console.print("➤ UPLOAD IMAGE    [1]")
    console.print("➤ VIEW HISTORY    [2]") 
    console.print("➤ EXIT SYSTEM     [0]")
    console.print("─" * 30)
    console.print("DEVELOPED BY: MR ZUYAN")
    console.print("─" * 30)

def upload_image():
    clear_screen()
    
    console.print("[bold cyan]UPLOAD IMAGE[/bold cyan]")
    console.print("─" * 20)
    
    path = Prompt.ask("➤ ENTER IMAGE PATH")
    
    if not os.path.exists(path):
        console.print("● ERROR: FILE NOT FOUND", style="red")
        input("PRESS ENTER TO CONTINUE")
        return
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[green]{task.description}[/green]"),
        transient=True,
    ) as progress:
        task = progress.add_task("● UPLOADING IMAGE...", total=None)
        
        try:
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            
            resp = requests.post(
                "https://freeimage.host/api/1/upload",
                data={"key": API_KEY, "action": "upload", "source": data}
            )
            
            url = resp.json().get('image', {}).get('display_url')
            
            if url:
                conn.execute("INSERT INTO images VALUES (?)", (url,))
                conn.commit()
                
                console.print("\n● UPLOAD SUCCESSFUL!", style="green")
                console.print("● IMAGE URL:", style="white")
                console.print(url, style="cyan")
            else:
                console.print("● UPLOAD FAILED", style="red")
                
        except Exception as e:
            console.print(f"● ERROR: {str(e)}", style="red")
    
    input("PRESS ENTER TO CONTINUE")

def view_history():
    clear_screen()
    
    console.print("[bold cyan]UPLOAD HISTORY[/bold cyan]")
    console.print("─" * 20)
    
    cursor = conn.execute("SELECT image_url FROM images")
    urls = cursor.fetchall()
    
    if not urls:
        console.print("● NO IMAGES UPLOADED", style="yellow")
    else:
        for i, (url,) in enumerate(urls, 1):
            console.print(f"[{i}] {url}", style="cyan")
        console.print(f"● TOTAL: {len(urls)} images", style="green")
    
    input("PRESS ENTER TO CONTINUE")

def main():
    while True:
        try:
            show_menu()
            choice = IntPrompt.ask("● CHOOSE OPTION", choices=["0", "1", "2"])
            
            if choice == 1:
                upload_image()
            elif choice == 2:
                view_history()
            elif choice == 0:
                console.print("● EXITING SYSTEM...", style="green")
                break
                
        except KeyboardInterrupt:
            console.print("● EXITING SYSTEM...", style="green")
            break
        except Exception as e:
            console.print(f"● ERROR: {str(e)}", style="red")
            input("PRESS ENTER TO CONTINUE")

if __name__ == "__main__":
    main()
    conn.close()