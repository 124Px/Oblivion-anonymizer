import subprocess
import sys
import os
import ctypes

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px

required_packages = [
    "colorama",
    "requests",
    "pyperclip",
    "psutil",
    "tqdm",
    "cryptography",
    "Pillow",
    "customtkinter",
    "winshell",
    "pywin32",
]

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

script_path = os.path.join(os.path.dirname(__file__), "RedTiger.py")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Relaunching with admin privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
else:
    subprocess.run([sys.executable, script_path])
