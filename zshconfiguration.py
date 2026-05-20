import os
from pathlib import Path
import time
home = Path.home()
otherscript = f"{home}/QuoteFolder/main.py"
username = os.getenv("USER")
shell= os.environ.get("SHELL", "")
time.sleep(2)
if "zsh" in shell:
    
    try:
        zshrc = os.path.expanduser("~/.zshrc")

        already_exists = False
        if os.path.exists(zshrc):
            with open(zshrc, "r") as f:
                if otherscript in f.read():
                    already_exists = True


        if already_exists:
            print("FATAL: Already Written to ZSHRC configuration.")
        else:
            with open(zshrc, "a")as f:
                f.write(f'\n/usr/bin/python3 "{otherscript}"\n')
                print("Sucessfully Wrote to ZSH")
    except Exception as e:
        print(f"FATAL ERROR:{e}")
elif "bash" in shell:
    try:
        bash = os.path.expanduser("~/.bashrc")
        already_exists = False
        if os.path.exists(bash):
            with open(bash, "r") as f:
                if otherscript in f.read():
                    already_exists = True


        if already_exists:
            print("FATAL: Already Written to BASH configuration.")
        else:
            with open(bash, "a")as f:
                f.write(f'\n/usr/bin/python3 "{otherscript}"\n')
                print("Sucessfully Wrote to BASH")
    except Exception as e:
            print(f"FATAL ERROR:{e}")