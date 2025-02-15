import colorama
import datetime
import sys
import os
import ctypes
import uuid
import subprocess
import winreg
import shutil
import random
import string
import socket
import time
import winshell
import pyperclip
import re
import platform
import psutil
import webbrowser
import threading
import urllib.request
from PIL import Image, ImageTk
from tqdm import tqdm
import hashlib

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
import base64

import tkinter.messagebox as messagebox
import customtkinter as ctk
from tkinter import filedialog

os.chdir(os.path.dirname(os.path.abspath(__file__)))

colorama.init()
color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

discord = "dsc.gg/lmxx"
github = "github.com/124Px"
telegram = "t.me/CMwa124p"
by = "124P"
version = "1.1"
ID = "2"

title = f"Oblivion anonymizer v{version}"

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

def Title_Console(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{title}\x07")

def Clear_Console():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")

Title_Console(title + " Console:")
Clear_Console()
print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Launch..")

def Error_Console(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white + str(e)}")

def Info(message):
    messagebox.showinfo(title, message)

def Error(message):
    messagebox.showerror(title, message)

def Warning(message):
    messagebox.showwarning(title, message)


path_ThisFile = sys.argv[0]
if ".exe" in path_ThisFile:
    extension = ".exe"
elif ".py" in path_ThisFile:
    extension = ".py"
else:
    extension = None
Spoof_Games_Code = "Cleaner/Cleaner.bat"
Regedit_Clean_Code = "Cleaner/regedit.bat"
path_Run                          = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
path_Cryptography                 = r"SOFTWARE\Microsoft\Cryptography"
path_SQMClient                    = r"SOFTWARE\Microsoft\SQMClient"
path_HardwareProfiles             = r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001"
path_ConsentStore                 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore"
path_Nvidia                       = r'SOFTWARE\NVIDIA Corporation'
path_HardwareConfig               = r'SYSTEM\HardwareConfig\Current'
path_Windows                      = os.getenv('WINDIR')
path_AppdataTempFolder            = os.getenv('TEMP')
path_TempFolder                   = os.path.join(path_Windows, 'Temp')
path_PrefetchFolder               = os.path.join(path_Windows, 'Prefetch')

path_AppdataLocal                 = os.getenv('LOCALAPPDATA')
path_AppdataRoaming               = os.getenv('APPDATA')
path_ProgramFileX86               = os.path.dirname(os.path.abspath(__file__))
path_ProgramFileX64               = os.path.dirname(os.path.abspath(__file__))
path_ProgramFileX32               = os.path.dirname(os.path.abspath(__file__))
path_ProgramFile                  = os.path.dirname(os.path.abspath(__file__))
path_ProgramData                  = os.path.dirname(os.path.abspath(__file__))
path_StartMenu                    = os.path.join(path_ProgramData, "Microsoft", "Windows", "Start Menu", "Programs")

path_LogsFolder                   = os.path.join(os.getenv('SystemRoot'), 'Logs')
path_System32WinevtLogsFolder     = os.path.join(os.getenv('SystemRoot'), 'System32', 'winevt', 'Logs')
path_System32LogFilesFolder       = os.path.join(os.getenv('SystemRoot'), 'System32', 'LogFiles')
path_DownloadSoftwareDistribution = os.path.join(os.getenv('SystemRoot'), 'SoftwareDistribution', 'Download')
path_BackupFolder                 = os.path.join(os.getenv('SystemRoot'), 'WinSxS', 'Backup')
path_AppdataApplicationLogsFolder = os.path.join(path_AppdataRoaming, 'Local', 'Application Logs')
path_ReportArchiveFolder          = os.path.join(path_AppdataLocal, 'Microsoft', 'Windows', 'WER', 'ReportArchive')
path_ReportQueueFolder            = os.path.join(path_AppdataLocal, 'Microsoft', 'Windows', 'WER', 'ReportQueue')
path_CrashDumps                   = os.path.join(path_AppdataLocal, 'CrashDumps')
path_WebCache                     = os.path.join(path_AppdataLocal, 'Microsoft', 'Windows', 'WebCache')
path_DirectXShaderCacheFolder     = os.path.join(path_AppdataLocal, 'Microsoft', 'DirectX Shader Cache')

path_UserProfile                  = os.getenv('USERPROFILE')
path_Downloads                    = os.path.join(path_UserProfile, 'Downloads')
path_Documents                    = os.path.join(path_UserProfile, 'Documents')
path_Pictures                     = os.path.join(path_UserProfile, 'Pictures')
path_Videos                       = os.path.join(path_UserProfile, 'Videos')
path_Music                        = os.path.join(path_UserProfile, 'Music')
path_Desktop                      = os.path.join(path_UserProfile, 'Desktop')
path_Objects3d                    = os.path.join(path_UserProfile, '3D Objects')

path_FolderSoftware               = os.path.join(path_ProgramFile, "Oblivion", "Oblivion_Anonimizer")
path_FolderImg                    = os.path.join(path_FolderSoftware, "img")
path_FolderApp                    = os.path.join(path_FolderSoftware)
path_FolderAmideWin               = os.path.join(path_FolderSoftware, "amidewin")
path_FolderVolumeId               = os.path.join(path_FolderSoftware, "volumeid")
path_FolderKey                    = os.path.join(path_FolderSoftware, "key")
path_Key                          = os.path.join(path_FolderKey, "key")
path_App                          = os.path.join(path_FolderApp, title + extension)
path_this                         = os.path.dirname(os.path.abspath(__file__))

Img = {
    'banner_oblivion': os.path.join(path_FolderImg, 'banner_oblivion.png'),
    'logo_browser': os.path.join(path_FolderImg, 'logo_browser.png'),
    'logo_cookie': os.path.join(path_FolderImg, 'logo_cookie.png'),
    'logo_file': os.path.join(path_FolderImg, 'logo_file.png'),
    'logo_github': os.path.join(path_FolderImg, 'logo_github.png'),
    'logo_glass': os.path.join(path_FolderImg, 'logo_glass.png'),
    'logo_hardware': os.path.join(path_FolderImg, 'logo_hardware.png'),
    'logo_home': os.path.join(path_FolderImg, 'logo_home.png'),
    'logo_internet': os.path.join(path_FolderImg, 'logo_internet.png'),
    'logo_local_storage': os.path.join(path_FolderImg, 'logo_local_storage.png'),
    'logo_password': os.path.join(path_FolderImg, 'logo_password.png'),
    'logo_plugin': os.path.join(path_FolderImg, 'logo_plugin.png'),
    'logo_protection': os.path.join(path_FolderImg, 'logo_protection.png'),
    'logo_Oblivion_Anonimizer': os.path.join(path_FolderImg, 'logo_Oblivion_Anonimizer.png'),
    'icon_Oblivion_Anonimizer': os.path.join(path_FolderImg, 'icon_Oblivion_Anonimizer.ico'),
    'logo_spoofer': os.path.join(path_FolderImg, 'logo_spoofer.png'),
    'logo_spoofing': os.path.join(path_FolderImg, 'logo_spoofing.png'),
    'logo_telegram': os.path.join(path_FolderImg, 'logo_telegram.png'),
    'logo_star': os.path.join(path_FolderImg, 'logo_star.png'),
    'logo_hello': os.path.join(path_FolderImg, 'logo_hello.png'),
    'logo_recyclebin': os.path.join(path_FolderImg, 'logo_recyclebin.png'),
    'logo_folder_encrypted': os.path.join(path_FolderImg, 'logo_folder_encrypted.png'),
    'logo_game': os.path.join(path_FolderImg, 'logo_game.png'),
    'logo_cheat': os.path.join(path_FolderImg, 'logo_cheat.png'),
    'logo_lock': os.path.join(path_FolderImg, 'logo_lock.png'),
    'logo_unlock': os.path.join(path_FolderImg, 'logo_unlock.png'),
    'logo_folder_lock': os.path.join(path_FolderImg, 'logo_folder_lock.png'),
    'logo_folder_unlock': os.path.join(path_FolderImg, 'logo_folder_unlock.png'),
    'logo_clean': os.path.join(path_FolderImg, 'logo_clean.png'),
    'logo_synchronization': os.path.join(path_FolderImg, 'logo_synchronization.png'),
    'logo_discord': os.path.join(path_FolderImg, 'logo_discord.png'),
    'logo_data': os.path.join(path_FolderImg, 'logo_data.png'),
    'logo_email': os.path.join(path_FolderImg, 'logo_email.png'),
    'logo_man': os.path.join(path_FolderImg, 'logo_man.png'),
    'logo_lock_password': os.path.join(path_FolderImg, 'logo_lock_password.png'),
    'logo_monitoring': os.path.join(path_FolderImg, 'logo_monitoring.png'),
    "logo_telemetry": os.path.join(path_FolderImg, 'logo_telemetry.png'),
    "logo_network": os.path.join(path_FolderImg, 'logo_network.png'),
    "logo_dns": os.path.join(path_FolderImg, 'logo_dns.png'),
}

browsers_paths = {
    'Chrome': os.path.join(path_AppdataLocal, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(path_AppdataLocal, 'Microsoft', 'Edge', 'User Data'),
    'Firefox': os.path.join(path_AppdataRoaming, 'Mozilla', 'Firefox', 'Profiles'),
    'Opera': os.path.join(path_AppdataRoaming, 'Opera Software', 'Opera Stable'),
    'Opera GX': os.path.join(path_AppdataRoaming, 'Opera Software', 'Opera GX Stable'),
    'Brave': os.path.join(path_AppdataLocal, 'BraveSoftware', 'Brave-Browser', 'User Data'),
    'Vivaldi': os.path.join(path_AppdataLocal, 'Vivaldi', 'User Data'),
    'Internet Explorer': os.path.join(path_AppdataLocal, 'Microsoft', 'Internet Explorer'),
    'Amigo': os.path.join(path_AppdataLocal, 'Amigo', 'User Data'),
    'Torch': os.path.join(path_AppdataLocal, 'Torch', 'User Data'),
    'Kometa': os.path.join(path_AppdataLocal, 'Kometa', 'User Data'),
    'Orbitum': os.path.join(path_AppdataLocal, 'Orbitum', 'User Data'),
    'Cent Browser': os.path.join(path_AppdataLocal, 'CentBrowser', 'User Data'),
    '7Star': os.path.join(path_AppdataLocal, '7Star', '7Star', 'User Data'),
    'Sputnik': os.path.join(path_AppdataLocal, 'Sputnik', 'Sputnik', 'User Data'),
    'Chrome SxS': os.path.join(path_AppdataLocal, 'Google', 'Chrome SxS', 'User Data'),
    'Epic': os.path.join(path_AppdataLocal, 'Epic Privacy Browser', 'User Data'),
    'Uran': os.path.join(path_AppdataLocal, 'uCozMedia', 'Uran', 'User Data'),
    'Yandex': os.path.join(path_AppdataLocal, 'Yandex', 'YandexBrowser', 'User Data'),
    'Iridium': os.path.join(path_AppdataLocal, 'Iridium', 'User Data'),
}

browsers_program = {
    'Chrome': 'chrome.exe',
    'Edge': 'msedge.exe',
    'Firefox': 'firefox.exe',
    'Opera': 'opera.exe',
    'Opera GX': 'opera.exe',
    'Brave': 'brave.exe',
    'Vivaldi': 'vivaldi.exe',
    'Internet Explorer': 'iexplore.exe',
    'Amigo': 'amigo.exe',
    'Torch': 'torch.exe',
    'Kometa': 'kometa.exe',
    'Orbitum': 'orbitum.exe',
    'Cent Browser': 'centbrowser.exe',
    '7Star': '7star.exe',
    'Sputnik': 'sputnik.exe',
    'Chrome SxS': 'chrome.exe',
    'Epic': 'epic.exe',
    'Uran': 'uran.exe',
    'Yandex': 'yandex.exe',
    'Iridium': 'iridium.exe',
}

profiles = [
    '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
]

colors = {
    "background": "#111111",
    "light_background": "#1a1a1a",
    "gray": "#252525",
    "light_gray": "#333333",
    "light_light_gray": "#686868",
    "red": "#a80505",
    "white": "#FFFFFF",
}

def ChooseFolder():
    try:
        root_folder = ctk.CTk()
        root_folder.geometry("800x500")
        root_folder.withdraw()
        root_folder.attributes('-topmost', True)
        try: root_folder.iconbitmap(Img["icon_Oblivion_Anonimizer"])
        except: pass

        folder_path = filedialog.askdirectory(parent=root_folder, title=title+" | Choose folder")
        
        if not folder_path:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} No folder selected.")
            return None
            
    except Exception as e:
        Error_Console(e)
    
    return folder_path

def Verification():
    def Check_Admin():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Checking if the program has administrator privileges..")
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} The program is not run with administrator privileges.")
            Warning("Please run the program as administrator.")
            return True
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The program was executed with administrator privileges.")
            return False

    def Check_Connection():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Checking if the internet connection is active..")
        try:
            if not urllib.request.urlopen("https://google.com", timeout=10):
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} The internet connection is not activated.")
                Warning("Please activate your internet connection.")
                return True
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The internet connection is active.")
                return False
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} The internet connection is not activated.")
            Warning("Please activate your internet connection.")
            return True

    def Check_Plugins():
        installed = False

        if not os.path.exists(path_FolderImg):
            os.makedirs(path_FolderImg, exist_ok=True)
        if os.path.exists(path_FolderImg):
            for name, path in Img.items():
                if os.path.exists(path):
                    status = False
                    continue
                else:
                    status = True
                    break

Verification()
try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Cryptography, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "MachineGuid")
        Machine_Guid = str(value).replace("{", "").replace("}", "")
except: Machine_Guid = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareProfiles, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "GUID")
        Guid_Serial_Number = str(value).replace("{", "").replace("}", "")
except: Guid_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareProfiles, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "HwProfileGuid")
        Hw_Profile_Guid = str(value).replace("{", "").replace("}", "")
except: Hw_Profile_Guid = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_SQMClient, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "MachineId")
        Machine_Id = str(value).replace("{", "").replace("}", "")
except: Machine_Id = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Nvidia+r'\Installer2', 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemID")
        Nvidia_System_Id = str(value).replace("{", "").replace("}", "")
except: Nvidia_System_Id = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "BaseBoardProduct")
        Motherboard_Product_Serial_Number = str(value).replace("{", "").replace("}", "")
except: Motherboard_Product_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "BaseBoardManufacturer")
        Motherboard_Manufacturer_Serial_Number = str(value).replace("{", "").replace("}", "")
except: Motherboard_Manufacturer_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "BIOSReleaseDate")
        Bios_Release_Date = str(value).replace("{", "").replace("}", "")
except: Bios_Release_Date = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "BIOSVersion")
        Bios_Version = str(value).replace("{", "").replace("}", "")
except: Bios_Version = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemBiosVersion")
        System_Bios_Version = str(value).replace("{", "").replace("}", "")
except: System_Bios_Version = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemVersion")
        System_Version = str(value).replace("{", "").replace("}", "")
except: System_Version = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemFamily")
        System_Family_Serial_Number = str(value).replace("{", "").replace("}", "")
except: System_Family_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemManufacturer")
        System_Manufacturer_Serial_Number = str(value).replace("{", "").replace("}", "")
except: System_Manufacturer_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemProductName")
        System_Product_Serial_Number = str(value).replace("{", "").replace("}", "")
except: System_Product_Serial_Number = None

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_READ) as key:
        value, reg_type = winreg.QueryValueEx(key, "SystemSKU")
        System_SKU_Serial_Number = str(value).replace("{", "").replace("}", "")
except: System_SKU_Serial_Number = None

try: 
    Uuid_Serial_Number = subprocess.check_output(['wmic', 'csproduct', 'get', 'UUID'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not Uuid_Serial_Number.strip():
        Uuid_Serial_Number = subprocess.check_output(['wmic', 'csproduct', 'get', 'UUID'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except: Uuid_Serial_Number = None

try: 
    Bios_Serial_Number = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not Bios_Serial_Number.strip():
        Bios_Serial_Number = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except: Bios_Serial_Number = None

try: 
    Motherboard_Serial_Number = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not Motherboard_Serial_Number.strip():
        Motherboard_Serial_Number = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except: Motherboard_Serial_Number = None

try: 
    Processor_Serial_Number = subprocess.check_output(['wmic', 'cpu', 'get', 'ProcessorId'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not Processor_Serial_Number.strip():
        Processor_Serial_Number = subprocess.check_output(['wmic', 'cpu', 'get', 'ProcessorId'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except: Processor_Serial_Number = None

try:
    OemString_Serial_Number = subprocess.check_output(['wmic', 'bios', 'get', 'OEMString'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not OemString_Serial_Number.strip():
        OemString_Serial_Number = subprocess.check_output(['wmic', 'bios', 'get', 'OEMString'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except:
    OemString_Serial_Number = None

try:
    Asset_Tag = subprocess.check_output(['wmic', 'systemenclosure', 'get', 'SMBIOSAssetTag'], stderr=subprocess.STDOUT, text=True).split('\n')[1].strip()
    if not Asset_Tag.strip():
        Asset_Tag = subprocess.check_output(['wmic', 'systemenclosure', 'get', 'SMBIOSAssetTag'], stderr=subprocess.STDOUT, text=True).split('\n')[2].strip()
except:
    Asset_Tag = None

try:
    output = subprocess.check_output(f'"{os.path.join(path_FolderAmideWin, "AMIDEWINx64.exe")}" /CS', shell=True, text=True)    
    Chassis_Serial_Number = re.search(r"Chassis Serial number\s+R\s+Done\s+\"([\w\d]+)\"", output).group(1)
except:
    Chassis_Serial_Number = None

try: Hostname = socket.gethostname()
except: Hostname = None

try: Os = platform.system()
except: Os = None

try: Os_Version = platform.version()
except: Os_Version = None

try: username_pc = os.getlogin()
except: username_pc = "username"

try:
    disk_values = {}
    volumes = subprocess.run(['wmic', 'logicaldisk', 'get', 'DeviceID,VolumeSerialNumber'], stdout=subprocess.PIPE, text=True).stdout.splitlines()[1:]
    for volume in volumes:
        if volume.strip():
            volume_parts = volume.split()
            if len(volume_parts) == 2:
                letter, hwid = volume_parts
                disk_values[letter] = hwid
except:
    disk_values = {None: None}

def Cleaner(choice):
    def Delete_File_From_Folder(name, path_folders):
        try:
            for path_folder in path_folders:
                if not os.path.exists(path_folder):
                    break

                for name_file in os.listdir(path_folder):
                    try:
                        path_file = os.path.join(path_folder, name_file)
                        if os.path.isfile(path_file):
                            os.remove(path_file)
                        elif os.path.isdir(path_file):
                            shutil.rmtree(path_file)
                    except: pass

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} All files were deleted from: {white + name}")
        except Exception as e:
            Error_Console(e)

    def Delete_Duplicate_Files_From_Folder(name, path_folders):
        def hash_file(path_file):
            hasher = hashlib.md5()
            with open(path_file, 'rb') as file:
                buf = file.read()
                hasher.update(buf)
            return hasher.hexdigest()

        for path_folder in path_folders:
            try:
                if not os.path.exists(path_folder):
                    break

                hash_dict = {}
                for name_file in os.listdir(path_folder):
                    try:
                        path_file = os.path.join(path_folder, name_file)
                        if os.path.isfile(path_file):
                            file_hash = hash_file(path_file)
                            if file_hash in hash_dict:
                                os.remove(path_file)
                            else:
                                hash_dict[file_hash] = path_file
                        elif os.path.isdir(path_file):
                            shutil.rmtree(path_file)
                    except: pass
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The duplicate files were deleted from: {white + name}")
            except Exception as e:
                Error_Console(e)

    def LogFiles_Delete(name, path_folders):
        for path_folder in path_folders:
            try:
                if not os.path.exists(path_folder):
                    break
                
                for root, dirs, files in os.walk(path_folder):
                    for file in files:
                        if file.endswith(".log"):
                            os.remove(os.path.join(root, file))
            except: pass
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The log files were deleted from: {white + name}")

    def FragmentationFiles_Delete(name, path_folders):
        for path_folder in path_folders:
            try:
                if not os.path.exists(path_folder):
                    break
                
                for root, dirs, files in os.walk(path_folder):
                    for file in files:
                        if file.endswith(".chk"):
                            os.remove(os.path.join(root, file))
            except: pass
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The fragmentation files were deleted from: {white + name}")

    def EmptyFiles_Delete(name, path_folders):
        for path_folder in path_folders:
            try:
                if not os.path.exists(path_folder):
                    break
                
                for root, dirs, files in os.walk(path_folder):
                    for file in files:
                        path_file = os.path.join(root, file)
                        if os.path.isfile(path_file) and os.path.getsize(path_file) == 0:
                            os.remove(path_file)
            except: pass
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The empty files were deleted from: {white + name}")

    def HiddenFiles_Delete(name, path_folders):
        for path_folder in path_folders:
            try:
                if not os.path.exists(path_folder):
                    break
                
                for root, dirs, files in os.walk(path_folder):
                    for file in files:
                        path_file = os.path.join(root, file)
                        if os.path.isfile(path_file) and file.startswith('.'):
                            os.remove(path_file)
            except: pass
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The hidden files were deleted from: {white + name}")
        
    def TempFile_Delete():
        Delete_File_From_Folder("Temporary Files", [path_TempFolder, path_AppdataTempFolder, path_PrefetchFolder])

    def DownloadsFile_Delete():
        Delete_File_From_Folder("Downloads Files", [path_Downloads])

    def WindowsCache_Delete():
        Delete_File_From_Folder("Windows Cache", [path_DownloadSoftwareDistribution, path_LogsFolder, path_PrefetchFolder, path_TempFolder])

    def WindowsOldUpdate_Delete():
        Delete_File_From_Folder("Windows Old Update", [path_DownloadSoftwareDistribution, path_BackupFolder, path_LogsFolder])

    def WindowsLogs_Delete():
        Delete_File_From_Folder("Windows Logs", [path_LogsFolder, path_System32WinevtLogsFolder, path_AppdataApplicationLogsFolder, path_System32LogFilesFolder])
    
    def WindowsErrorReport_Delete():
        Delete_File_From_Folder("Windows Error Report", [path_ReportArchiveFolder, path_ReportQueueFolder, path_CrashDumps, path_LogsFolder, path_System32WinevtLogsFolder])

    def WindowsWebCache_Delete():
        Delete_File_From_Folder("Windows Web Cache", [path_WebCache])
    
    def DirectXShaderCache_Delete():
        Delete_File_From_Folder("DirectX Shader Cache", [path_DirectXShaderCacheFolder])

    def DocumentsFile_Clean():
        Delete_Duplicate_Files_From_Folder("Document Files", [path_Documents])
        LogFiles_Delete("Document Files", [path_Documents])
        FragmentationFiles_Delete("Document Files", [path_Documents])
        EmptyFiles_Delete("Document Files", [path_Documents])
        HiddenFiles_Delete("Document Files", [path_Documents])

    def VideosFile_Clean():
        Delete_Duplicate_Files_From_Folder("Video Files", [path_Videos])
        LogFiles_Delete("Video Files", [path_Videos])
        FragmentationFiles_Delete("Video Files", [path_Videos])
        EmptyFiles_Delete("Video Files", [path_Videos])
        HiddenFiles_Delete("Video Files", [path_Videos])

    def MusicFile_Clean():
        Delete_Duplicate_Files_From_Folder("Music Files", [path_Music])
        LogFiles_Delete("Music Files", [path_Music])
        FragmentationFiles_Delete("Music Files", [path_Music])
        EmptyFiles_Delete("Music Files", [path_Music])
        HiddenFiles_Delete("Music Files", [path_Music])

    def PicturesFile_Clean():
        Delete_Duplicate_Files_From_Folder("Picture Files", [path_Pictures])
        LogFiles_Delete("Picture Files", [path_Pictures])
        FragmentationFiles_Delete("Picture Files", [path_Pictures])
        EmptyFiles_Delete("Picture Files", [path_Pictures])
        HiddenFiles_Delete("Picture Files", [path_Pictures])
    
    def Objects3dFile_Clean():
        Delete_Duplicate_Files_From_Folder("Object 3d Files", [path_Objects3d])
        LogFiles_Delete("Object 3d Files", [path_Objects3d])
        FragmentationFiles_Delete("Object 3d Files", [path_Objects3d])
        EmptyFiles_Delete("Object 3d Files", [path_Objects3d])
        HiddenFiles_Delete("Object 3d Files", [path_Objects3d])
    
    def ProgramFile_Clean():
        LogFiles_Delete("Program Files", [path_ProgramData, path_ProgramFile, path_ProgramFileX32, path_ProgramFileX64, path_ProgramFileX86])
        FragmentationFiles_Delete("Program Files", [path_ProgramData, path_ProgramFile, path_ProgramFileX32, path_ProgramFileX64, path_ProgramFileX86])
        EmptyFiles_Delete("Program Files", [path_ProgramData, path_ProgramFile, path_ProgramFileX32, path_ProgramFileX64, path_ProgramFileX86])
        HiddenFiles_Delete("Program Files", [path_ProgramData, path_ProgramFile, path_ProgramFileX32, path_ProgramFileX64, path_ProgramFileX86])

    def RecycleBin_Clean():
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cleaned: {white}Recycle Bin")
        except Exception as e:
            Error_Console(e)

    def Clipboard_Clean():
        try:
            pyperclip.copy('')
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cleaned: {white}Clipboard")
        except Exception as e:
            Error_Console(e)

    try:
        if "Delete Temporary Files" in choice:
            TempFile_Delete()
        if "Delete Downloads Files" in choice:
            DownloadsFile_Delete()

        if "Delete Windows Cache" in choice:
            WindowsCache_Delete()
        if "Delete Old Windows Updates" in choice:
            WindowsOldUpdate_Delete()
        if "Delete Windows Logs" in choice: 
            WindowsLogs_Delete()
        if "Delete Windows Error Report" in choice:
            WindowsErrorReport_Delete()
        if "Delete Windows Web Cache" in choice:
            WindowsWebCache_Delete()
        if "Delete DirectX Shader Cache" in choice:
            DirectXShaderCache_Delete()

        if "Clean Up Program Files" in choice:
            ProgramFile_Clean()
        if "Clean Up Document Files" in choice:
            DocumentsFile_Clean()
        if "Clean Up Video Files" in choice:
            VideosFile_Clean()
        if "Clean Up Music Files" in choice:
            MusicFile_Clean()
        if "Clean Up Picture Files" in choice:
            PicturesFile_Clean()
        if "Clean Up Object 3d Files" in choice:
            Objects3dFile_Clean()
        if "Clean Up Clipboard" in choice:
            Clipboard_Clean()
        if "Clean Up Recycle Bin" in choice:
            RecycleBin_Clean()
    except Exception as e:
        Error_Console(e)

    def Delete_path(path):
        try: os.remove(path)
        except: pass
        try: os.mkdir(path)
        except: pass
        try: shutil.rmtree(path)
        except: pass

    def UninstallOneDrive():
        try:
            try: subprocess.run("taskkill /f /im OneDrive.exe", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            except: pass
            subprocess.run("C:\\Windows\\System32\\OneDriveSetup.exe /uninstall", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            try: subprocess.run('powershell -Command "Remove-Item -Path \'HKCU:\\SOFTWARE\\Microsoft\\OneDrive\' -Recurse -Force"',shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}OneDrive")
        except Exception as e:
            Error_Console(e)

    def UninstallCortana():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.549981C3F5F10 | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Cortana")
        except Exception as e:
            Error_Console(e)

    def UninstallMicrosoftEdge():
        try:
            try: subprocess.run("taskkill /F /IM msedge.exe", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run("taskkill /F /IM msedgeupdate.exe", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.MicrosoftEdge | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            
            edge_paths = [
                os.path.join("Microsoft", "Edge"),
                os.path.join("Microsoft", "EdgeCore"),
                os.path.join("Microsoft", "EdgeUpdate"),
                os.path.join("Microsoft", "EdgeWebView")
            ]
            paths = [path_ProgramData, path_ProgramFile, path_ProgramFileX32, path_ProgramFileX64, path_ProgramFileX86, path_AppdataLocal, path_AppdataRoaming]
            other_paths = [os.path.join(path_StartMenu, "Microsoft Edge.lnk"), os.path.join(path_Desktop, "Microsoft Edge.lnk")]

            for edge_path in edge_paths:
                for path in paths:
                    try:
                        full_path = os.path.join(path, edge_path)
                        if os.path.exists(full_path):
                            for root, dirs, files in os.walk(full_path):
                                for file in files:
                                    file_path = os.path.join(root, file)
                                    Delete_path(file_path)
                            Delete_path(full_path)
                    except: continue
            for other_path in other_paths:
                Delete_path(other_path)

            try: subprocess.run('powershell -Command "Remove-Item -Path \'HKCU:\\SOFTWARE\\Microsoft\\Edge\' -Recurse -Force"',shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run('powershell -Command "Remove-Item -Path \'HKCU:\\SOFTWARE\\Microsoft\\EdgeWebView\' -Recurse -Force"',shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run('powershell -Command "Remove-Item -Path \'HKCU:\\SOFTWARE\\Microsoft\\EdgeUpdate\' -Recurse -Force"',shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Microsoft Edge")
        except Exception as e:
            Error_Console(e)

    def UninstallXboxGameBar():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Xbox Game Bar")
        except Exception as e:
            Error_Console(e)

    def UninstallSkype():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.SkypeApp | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Skype")
        except Exception as e:
            Error_Console(e)

    def UninstallMicrosoftOffice():
        try:
            try: subprocess.run("taskkill /f /im WINWORD.EXE", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run("taskkill /f /im EXCEL.EXE", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            try: subprocess.run("taskkill /f /im POWERPNT.EXE", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            subprocess.run("C:\\Program Files\\Microsoft Office\\Office16\\OfficeSetup.exe /uninstall", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            try: subprocess.run('powershell -Command "Remove-Item -Path \'HKCU:\\SOFTWARE\\Microsoft\\Office\' -Recurse -Force"',shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Microsoft Office")
        except Exception as e:
            Error_Console(e)

    def UninstallWindowsMediaPlayer():
        try:
            subprocess.run("powershell -Command \"Get-WindowsCapability -Online | Where-Object { $_.Name -like 'Media.Player*' } | Remove-WindowsCapability -Online\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Windows Media Player")
        except Exception as e:
            Error_Console(e)

    def UninstallMailAndCalendar():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.WindowsMail | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Mail and Calendar")
        except Exception as e:
            Error_Console(e)

    def UninstallMoviesAndTV():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.ZuneVideo | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Movies & TV")
        except Exception as e:
            Error_Console(e)

    def UninstallPhotos():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.Photos | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Photos")
        except Exception as e:
            Error_Console(e)

    def UninstallWeather():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.BingWeather | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Weather")
        except Exception as e:
            Error_Console(e)

    def UninstallMaps():
        try:
            subprocess.run("powershell -Command \"Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage\"", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Uninstalled: {white}Maps")
        except Exception as e:
            Error_Console(e)

    try:
        if "Uninstall One Drive" in choice:
            UninstallOneDrive()
        if "Uninstall Cortana" in choice:
            UninstallCortana()
        if "Uninstall Microsoft Edge" in choice:
            UninstallMicrosoftEdge()
        if "Uninstall Xbox Game Bar" in choice:
            UninstallXboxGameBar()
        if "Uninstall Skype" in choice:
            UninstallSkype()
        if "Uninstall Microsoft Office" in choice:
            UninstallMicrosoftOffice()
        if "Uninstall Windows Media Player" in choice:
            UninstallWindowsMediaPlayer()
        if "Uninstall Mail and Calendar" in choice:
            UninstallMailAndCalendar()
        if "Uninstall Movies & TV" in choice:
            UninstallMoviesAndTV()
        if "Uninstall Photos" in choice:
            UninstallPhotos()
        if "Uninstall Weather" in choice:
            UninstallWeather()
        if "Uninstall Maps" in choice:
            UninstallMaps()
    except Exception as e:
        Error_Console(e)

# ---------------------------------------
# --------------> SPOOFER <--------------
# ---------------------------------------

def SerialNumber_Changer(choice):

    def HwidDisk_Changer():
        try:
            available_drives = []
            for drive in range(65, 91):
                drive_letter = chr(drive) + ":"
                if os.path.exists(drive_letter):
                    available_drives.append(drive_letter)
            for drive in available_drives:
                new_numbers = ''.join(random.choice("0123456789ABCDEF") for _ in range(4)) + "-" + ''.join(random.choice("0123456789ABCDEF") for _ in range(4))
                try:
                    result = subprocess.run(f"volumeid {drive} {new_numbers}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        tructruc = current_time_hour()
                        print(f"{BEFORE + tructruc + AFTER} {INFO} Serial numbers of the disk: {white + drive}{red} changed to: {white + new_numbers}")
                    else:
                        Error_Console(f"Failed to change serial numbers on disk: {white + drive} (Error: {result.returncode})")
                except Exception as e:
                    Error_Console(e)
        except Exception as e:
            Error_Console(e)

    def MachineGuid_Changer():
        try:
            name = "Machine Guid"
            value_name = "MachineGuid"
            new_guid = str(uuid.uuid4())

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Cryptography, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def HwProfileGuid_Changer():
        try:
            name = "Hw Profile Guid"
            value_name = "HwProfileGuid"
            guid = str(uuid.uuid4())
            new_guid = "{" + guid + "}"

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareProfiles, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + guid}")
        except Exception as e:
            Error_Console(e)

    def GuidSerialNumber_Changer():
        try:
            name = "Guid"
            value_name = "GUID"
            guid = str(uuid.uuid4())
            new_guid = "{" + guid + "}"

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareProfiles, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + guid}")
        except Exception as e:
            Error_Console(e)

    def MachineId_Changer():
        try:
            name = "Machine Id"
            value_name = "MachineId"
            guid = str(uuid.uuid4())
            new_guid = "{" + guid + "}"

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_SQMClient, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + guid}")
        except Exception as e:
            Error_Console(e)

    def NvidiaSystemId_Changer():
        try:
            name = "Nvidia System Id"
            value_name = "SystemID"
            new_guid = str(uuid.uuid4()).upper()

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Nvidia+r'\Installer2', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def MotherboardProduct_Changer():
        try:
            name = "Motherboard Product"
            value_name = "BaseBoardProduct"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in Motherboard_Product_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def MotherboardManufacturer_Changer():
        try:
            name = "Motherboard Manufacturer"
            value_name = "BaseBoardManufacturer"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in Motherboard_Manufacturer_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def BiosReleaseDate_Changer():
        try:
            name = "Bios Release Date"
            value_name = "BIOSReleaseDate"
            new_guid = f"{random.randint(1,12)}/{random.randint(1,12)}/20{random.randint(16,24)}"

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Date of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)
    
    def BiosVersion_Changer():
        try:
            name = "Bios Version"
            value_name = "BIOSVersion"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in Bios_Version)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Version of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemBiosVersion_Changer():
        try:
            name = "System Bios Version"
            value_name = "SystemBiosVersion"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_Bios_Version)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Version of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemVersion_Changer():
        try:
            name = "System Version"
            value_name = "SystemVersion"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_Version)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Version of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemFamily_Changer():
        try:
            name = "System Family"
            value_name = "SystemFamily"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_Family_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemManufacturer_Changer():
        try:
            name = "System Manufacturer"
            value_name = "SystemManufacturer"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_Manufacturer_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemProduct_Changer():
        try:
            name = "System Product"
            value_name = "SystemProductName"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_Product_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)

    def SystemSKU_Changer():
        try:
            name = "System SKU"
            value_name = "SystemSKU"
            new_guid = ''.join(random.choice("0123456789") if char.isdigit() else char for char in System_SKU_Serial_Number)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_HardwareConfig, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_guid)
            winreg.CloseKey(key)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_guid}")
        except Exception as e:
            Error_Console(e)



    def UuidSerialNumber_Changer():
        try:
            name = "Uuid"
            if Uuid_Serial_Number:
                new_serial = ''.join(random.choice("0123456789ABCDEF") for _ in range(len(str(Uuid_Serial_Number).replace("-", ""))))
                subprocess.run(f'"{os.path.join(path_FolderAmideWin, "AMIDEWINx64.exe")}" /SU {new_serial}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_serial}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def MotherboardSerialNumber_Changer():
        try:
            name = "Motherboard"
            if Motherboard_Serial_Number:
                new_serial = ''.join(random.choice("0123456789ABCDEF") for _ in range(len(Motherboard_Serial_Number)))
                subprocess.run(f'"{os.path.join(path_FolderAmideWin, "AMIDEWINx64.exe")}" /SU {new_serial}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_serial}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def BiosSerialNumber_Changer():
        try:
            name = "Bios"
            if Bios_Serial_Number:
                new_serial = ''.join(random.choice("0123456789") for _ in range(len(Bios_Serial_Number)))
                subprocess.run(f"\"{os.path.join(path_FolderAmideWin, 'AMIDEWINx64.exe')}\" /BSI {new_serial}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_serial}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def ProcessorSerialNumber_Changer():
        try:
            name = "Processor"
            if Processor_Serial_Number:
                new_serial = ''.join(random.choice("0123456789ABCDEF") for _ in range(len(Processor_Serial_Number)))
                subprocess.run(f"\'{os.path.join(path_FolderAmideWin, 'AMIDEWINx64.exe')}\' /BSI {new_serial}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_serial}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def ChassisSerialNumber_Changer():
        try:
            name = "Chassis"
            if Chassis_Serial_Number:
                new_serial = ''.join(random.choice("0123456789ABCDEF") for _ in range(len(Chassis_Serial_Number)))
                subprocess.run(f"\"{os.path.join(path_FolderAmideWin, 'AMIDEWINx64.exe')}\" /CS {new_serial}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_serial}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def AssetTagSerialNumber_Changer():
        try:
            name = "Asset Tag"
            if Asset_Tag:
                new_tag = ''.join(random.choice("0123456789") for _ in range(len(Asset_Tag)))
                subprocess.run(f"\"{os.path.join(path_FolderAmideWin, 'AMIDEWINx64.exe')}\" /BT {new_tag}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_tag}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    def OemStringSerialNumber_Changer():
        try:
            name = "OEM String"
            if OemString_Serial_Number:
                new_string = ''.join(random.choice("0123456789ABCDEF") for _ in range(len(OemString_Serial_Number)))
                subprocess.run(f"\"{os.path.join(path_FolderAmideWin, 'AMIDEWINx64.exe')}\" /OS 1 {new_string}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} changed to: {white + new_string}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial numbers of {white + name + red} not found.")
        except Exception as e:
            Error_Console(e)

    try:
        if "Hwid Disk Serial Number" in choice:
            HwidDisk_Changer()

        if "Machine Guid" in choice:
            MachineGuid_Changer()
        if "Hw Profile Guid" in choice:
            HwProfileGuid_Changer()
        if "Guid Serial Number" in choice:
            GuidSerialNumber_Changer()
        if "Machine Id" in choice:
            MachineId_Changer()
        if "Nvidia System Id" in choice:
            NvidiaSystemId_Changer()
        

        if "Uuid Serial Number" in choice:
            UuidSerialNumber_Changer()
        if "Motherboard Serial Number" in choice:
            MotherboardSerialNumber_Changer()
        if "Motherboard Product" in choice:
            MotherboardProduct_Changer()
        if "Motherboard Manufacturer" in choice:
            MotherboardManufacturer_Changer()
        if "Chassis Serial Number" in choice:
            ChassisSerialNumber_Changer()
        if "Processor Serial Number" in choice:
            ProcessorSerialNumber_Changer()
        if "Oem String Serial Number" in choice:
            OemStringSerialNumber_Changer()
        if "Asset Tag Serial Number" in choice:
            AssetTagSerialNumber_Changer()
        if "Bios Serial Number" in choice:
            #BiosSerialNumber_Changer()
            pass
        if "Bios Release Date" in choice:
            BiosReleaseDate_Changer()
        if "Bios Version" in choice:
            BiosVersion_Changer()
        if "System Bios Version" in choice:
            SystemBiosVersion_Changer()
        if "System Version" in choice:
            SystemVersion_Changer()
        if "System Family" in choice:
            SystemFamily_Changer()
        if "System Manufacturer" in choice:
            SystemManufacturer_Changer()
        if "System Product" in choice:
            SystemProduct_Changer()
        if "System SKU" in choice:
            SystemSKU_Changer()
    except Exception as e:
        Error_Console(e)

def HostName_Changer():
    try:
        new_hostname = "DESKTOP-" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(7, 11)))
        command = f'Rename-Computer -NewName "{new_hostname}" -Force'
        subprocess.run(['powershell', '-Command', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Hostname Changed: {white + new_hostname}")
    except Exception as e:
        Error_Console(e)

def LauncherGames_Spoof():
    file = "SpoofLauncherGames.bat"
    finish_file = "finish.txt"

    def DeleteTempFile():
        try:
            for f in [file, finish_file]:
                if os.path.exists(f):
                    os.remove(f)
        except: 
            pass

    try:
        DeleteTempFile()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(Spoof_Games_Code)

        while True:
            if os.path.exists(file):
                break
            else:
                continue

        os.system(f"start {file}")

        while True:
            if os.path.exists(finish_file):
                time.sleep(1)
                DeleteTempFile()
                break
            else:
                time.sleep(1)
                continue


        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Launcher/Games Spoofed.")
    except Exception as e:
        DeleteTempFile()
        Error_Console(e)

def Regedit_Clean():
    file = "Regedit-Clean.bat"
    finish_file = "finish.txt"

    def DeleteTempFile():
        try:
            for f in [file, finish_file]:
                if os.path.exists(f):
                    os.remove(f)
        except: 
            pass

    try:
        DeleteTempFile()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(Regedit_Clean_Code)

        while not os.path.exists(file):
            time.sleep(0.1)

        os.system(f"start {file}")

        while not os.path.exists(finish_file):
             time.sleep(1)
        DeleteTempFile()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Regedit Cleaned.")
    except Exception as e:
        DeleteTempFile()
        Error_Console(e)

# ---------------------------------------
# --------------> BROWSER <--------------
# ---------------------------------------

def Delete_History(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4)
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for file in files:
                                    if 'places.sqlite' in file:
                                        os.remove(os.path.join(root, file))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} History deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            try:
                                history_path = os.path.join(path, profile, 'History')
                                if os.path.exists(history_path):
                                    os.remove(history_path)
                                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} History deleted: {white + browser}")
                                else: pass
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Delete_Cookies(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4)
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for file in files:
                                    if 'cookies.sqlite' in file:
                                        os.remove(os.path.join(root, file))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cookies deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            try:
                                cookies_path = os.path.join(path, profile, 'Network', 'Cookies')
                                if os.path.exists(cookies_path):
                                    os.remove(cookies_path)
                                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cookies deleted: {white + browser}")
                                else:
                                    pass
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Delete_Login_Data(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4) 
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for file in files:
                                    if 'logins.json' in file or 'signons.sqlite' in file:
                                        os.remove(os.path.join(root, file))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Login Data deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            try:
                                login_data_path = os.path.join(path, profile, 'Login Data')
                                if os.path.exists(login_data_path):
                                    os.remove(login_data_path)
                                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Login Data deleted: {white + browser}")
                                else:
                                    pass
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Delete_Cache(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4)
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for dir in dirs:
                                    if 'cache' in dir.lower():
                                        shutil.rmtree(os.path.join(root, dir))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cache deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            for name in ['cache', 'Cache', 'cache2', 'Cache2']:
                                try:
                                    cache_path = os.path.join(path, profile, name)
                                    if os.path.exists(cache_path):
                                        shutil.rmtree(cache_path)
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cache deleted: {white + browser}")
                                        break
                                    else:
                                        continue
                                except Exception as e:
                                    Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Delete_Local_Storage(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):                                                                                                                                                                                                                                                                                                                                                  
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4)
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for dir in dirs:
                                    if 'storage' in dir.lower():
                                        shutil.rmtree(os.path.join(root, dir))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Local Storage deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            try:
                                cache_path = os.path.join(path, profile, 'Local Storage')
                                if os.path.exists(cache_path):
                                    shutil.rmtree(cache_path)
                                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Local Storage deleted: {white + browser}")
                                    break
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Delete_Plugins(browser_choose):
    for browser, path in browsers_paths.items():
        if browser_choose == browser:
            if os.path.exists(path):
                try:
                    process_name = browsers_program.get(browser)
                    if process_name:
                        for proc in psutil.process_iter(['pid', 'name']):
                            if proc.info['name'] == process_name:
                                try:
                                    proc.kill()
                                    time.sleep(0.4)
                                except:
                                    pass

                    if 'Firefox' in browser:
                        for root, dirs, files in os.walk(path):
                            try:
                                for dir in dirs:
                                    if 'extensions' in dir:
                                        shutil.rmtree(os.path.join(root, dir))
                                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Plugins deleted: {white + browser}")
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                    else:
                        for profile in profiles:
                            try:
                                plugins_path = os.path.join(path, profile, 'Extensions')
                                if os.path.exists(plugins_path):
                                    shutil.rmtree(plugins_path)
                                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Plugins deleted: {white + browser}")
                                else:
                                    pass
                            except Exception as e:
                                Error_Console(f"{browser}: {e}")
                except Exception as e:
                    Error_Console(f"{browser}: {e}")
            else:
                pass

def Ipv6Protocol(state=None):
    protocol_path = os.path.join(path_Windows, "System32", "drivers", "etc", "protocol")

    try:
        with open(protocol_path, 'r', encoding='utf-8') as file:
            if "ipv6" in file.read:
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            with open(protocol_path, 'w', encoding='utf-8') as file:
                file.write("""# Copyright (c) 1993-2006 Microsoft Corp.
#
# This file contains the Internet protocols as defined by various
# RFCs.  See http://www.iana.org/assignments/protocol-numbers 
#
# Format:
#
# <protocol name>  <assigned number>  [aliases...]   [#<comment>]

ip         0     IP           # Internet protocol
icmp       1     ICMP         # Internet control message protocol
ggp        3     GGP          # Gateway-gateway protocol
tcp        6     TCP          # Transmission control protocol
egp        8     EGP          # Exterior gateway protocol
pup        12    PUP          # PARC universal packet protocol
udp        17    UDP          # User datagram protocol
hmp        20    HMP          # Host monitoring protocol
xns-idp    22    XNS-IDP      # Xerox NS IDP
rdp        27    RDP          # "reliable datagram" protocol
esp        50    ESP          # Encapsulating security payload
ah         51    AH           # Authentication header
rvd        66    RVD          # MIT remote virtual disk""")
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ipv6 Protocol: {white}Disable")

        elif state == 'enable':
            with open(protocol_path, 'w', encoding='utf-8') as file:
                file.write("""# Copyright (c) 1993-2006 Microsoft Corp.
#
# This file contains the Internet protocols as defined by various
# RFCs.  See http://www.iana.org/assignments/protocol-numbers 
#
# Format:
#
# <protocol name>  <assigned number>  [aliases...]   [#<comment>]

ip         0     IP           # Internet protocol
icmp       1     ICMP         # Internet control message protocol
ggp        3     GGP          # Gateway-gateway protocol
tcp        6     TCP          # Transmission control protocol
egp        8     EGP          # Exterior gateway protocol
pup        12    PUP          # PARC universal packet protocol
udp        17    UDP          # User datagram protocol
hmp        20    HMP          # Host monitoring protocol
xns-idp    22    XNS-IDP      # Xerox NS IDP
rdp        27    RDP          # "reliable datagram" protocol
ipv6       41    IPv6         # Internet protocol IPv6
ipv6-route 43    IPv6-Route   # Routing header for IPv6
ipv6-frag  44    IPv6-Frag    # Fragment header for IPv6
esp        50    ESP          # Encapsulating security payload
ah         51    AH           # Authentication header
ipv6-icmp  58    IPv6-ICMP    # ICMP for IPv6
ipv6-nonxt 59    IPv6-NoNxt   # No next header for IPv6
ipv6-opts  60    IPv6-Opts    # Destination options for IPv6
rvd        66    RVD          # MIT remote virtual disk""")
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ipv6 Protocol: {white}Enabled")

    except Exception as e:
        Error_Console(e)
    return state_now

def Network_Interface(state=None):

    interface_names = ['Wi-Fi', 'Ethernet 2', 'Ethernet', 'vEthernet (Ethernet)', 'vEthernet (Ethernet 2)', 'vEthernet (Wi-Fi)']
    try:
        result = subprocess.run(['netsh', 'interface', 'show', 'interface'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, encoding='utf-8', errors='replace')
        if "Enabled" in result.stdout or "Activ" in result.stdout:
            state_now = False
        if "Disabled" in result.stdout or "sactiv" in result.stdout:
            state_now = True
    except:
        state_now = None

    for interface_name in interface_names:
        try:
            if state == "enable":
                subprocess.run(f"netsh interface set interface {interface_name} admin=enable", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {interface_name}: {white}enabled")
            elif state == "disable":
                subprocess.run(f"netsh interface set interface {interface_name} admin=disable", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {interface_name}: {white}disabled")
        except: pass

    return state_now
def DnsCache_Delete():
    try:
        subprocess.run(['ipconfig', '/flushdns'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} DNS Cache: {white}Deleted")
    except subprocess.CalledProcessError as e:
        Error_Console(e)

def Network_Reset():
    try:
        commands = [
            "netsh winsock reset",
            "netsh int ip reset",
            "netsh advfirewall reset",
            "netsh int ipv4 reset",
            "netsh int ipv6 reset",
            "ipconfig /release",
            "ipconfig /renew",
            "netsh int ip set address \"%%j\" dhcp",
            "netsh int ip set dns \"%%j\" dhcp",
            "netsh interface set interface name=\"%%j\" admin=enabled",
            "certutil -URLCache * delete",
            "ipconfig /flushdns"
        ]

        error = 0
        for cmd in commands:
            try:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                error += 1
                Error_Console(e)
        if error == 0:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Network: {white}Reinitialized")
    except Exception as e:
        Error_Console(e)

def Flush_Arp_Cache():
    try:
        subprocess.run("arp -d *", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} ARP Cache: {white}Flushed")
    except Exception as e:
        Error_Console(e)

# ------------------------------------------
# --------------> PROTECTION <--------------
# ------------------------------------------

def Webcam(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\webcam', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\webcam',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Webcam: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\webcam',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Webcam: {white}Enabled")
    except Exception as e:
        Error_Console(e)
    
    return state_now

def Microphone(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\microphone', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\microphone',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Microphone: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\microphone',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Microphone: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Location(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\location', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\location',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Location: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\location',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Location: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Email(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\email', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\email',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Email: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\email',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Email: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Contacts(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\contacts', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\contacts',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Contacts: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\contacts',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Contacts: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Chat(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\chat', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\chat',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Chat: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\chat',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Chat: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def PhoneCall(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\phoneCall', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\phoneCall',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phone Call: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\phoneCall',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phone Call: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def PhoneCallHistory(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\phoneCallHistory', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\phoneCallHistory',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phone Call History: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\phoneCallHistory',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phone Call History: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Activity(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\activity', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\activity',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Activity: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\activity',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Activity: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def AppDiagnostics(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\appDiagnostics', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\appDiagnostics',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App Diagnostics: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\appDiagnostics',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App Diagnostics: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Appointments(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\appointments', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\appointments',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Appointments: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\appointments',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Appointments: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Bluetooth(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\bluetooth', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\bluetooth',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Bluetooth: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\bluetooth',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Bluetooth: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def BluetoothSync(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\bluetoothSync', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\bluetoothSync',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Bluetooth Sync: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\bluetoothSync',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Bluetooth Sync: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def BroadFileSystemAccess(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\broadFileSystemAccess', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\broadFileSystemAccess',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Broad File System Access: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\broadFileSystemAccess',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Broad File System Access: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def CellularData(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\cellularData', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\cellularData',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cellular Data: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\cellularData',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cellular Data: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def DocumentsLibrary(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\documentsLibrary', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\documentsLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Documents Library: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\documentsLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Documents Library: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def GazeInput(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\gazeInput', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\gazeInput',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Gaze Input: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\gazeInput',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Gaze Input: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def HumanInterfaceDevice(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\humanInterfaceDevice', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\humanInterfaceDevice',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Human Interface Device: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\humanInterfaceDevice',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Human Interface Device: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def PicturesLibrary(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\picturesLibrary', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\picturesLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Pictures Library: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\picturesLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Pictures Library: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def Radios(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\radios', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\radios',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Radios: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\radios',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Radios: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def SensorsCustom(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\sensors.custom', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\sensors.custom',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Custom Sensors: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\sensors.custom',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Custom Sensors: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def SerialCommunication(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\serialCommunication', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\serialCommunication',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial Communication: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\serialCommunication',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Serial Communication: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def USB(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\usb', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\usb',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} USB: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\usb',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} USB: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def UserAccountInformation(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\userAccountInformation', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userAccountInformation',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Account Information: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userAccountInformation',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Account Information: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WebCam(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\webCam', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\webCam',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} WebCam: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\webCam',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} WebCam: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsStore(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\windowsStore', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\windowsStore',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Store: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\windowsStore',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Store: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def MicrosoftAccount(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\microsoftAccount', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\microsoftAccount',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Microsoft Account: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\microsoftAccount',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Microsoft Account: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def UserDataTasks(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\userDataTasks', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userDataTasks',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Data Tasks: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userDataTasks',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Data Tasks: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now


def UserNotificationListener(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\userNotificationListener', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userNotificationListener',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Notification Listener: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\userNotificationListener',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Notification Listener: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now


def VideosLibrary(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\videosLibrary', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\videosLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Videos Library: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\videosLibrary',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Videos Library: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now


def WiFiData(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\wifiData', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\wifiData',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Wi-Fi Data: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\wifiData',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Wi-Fi Data: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now


def WiFiDirect(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_ConsentStore + r'\wifiDirect', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Value")
            state_now = value
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\wifiDirect',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Deny')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Wi-Fi Direct: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                path_ConsentStore + r'\wifiDirect',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Value', 0, winreg.REG_SZ, 'Allow')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Wi-Fi Direct: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now



def Unblock_Website():
    try:
        hosts_path = os.path.join(path_Windows, "System32", "drivers", "etc", "hosts")
        with open(hosts_path, 'w', encoding='utf-8') as file:
            file.write("# Copyright (c) 1993-2009 Microsoft Corp.")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} All websites were unlocked.")
    except Exception as e:
        Error_Console(e)

def Delete_Discord_Injection():
    try:
        def get_core(dir):
            for file in os.listdir(dir):
                if re.search(r'app-+?', file):
                    modules = dir + '\\' + file + '\\modules'
                    if not os.path.exists(modules):
                        continue
                    for file in os.listdir(modules):
                        if re.search(r'discord_desktop_core-+?', file):
                            core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                            return core, file
            return None
                
        appdata = path_AppdataLocal
        discord_dirs = [
            appdata + '\\Discord',
            appdata + '\\DiscordCanary',
            appdata + '\\DiscordPTB',
            appdata + '\\DiscordDevelopment'
        ]

        for dir in discord_dirs:
            if not os.path.exists(dir):
                continue

            core_info = get_core(dir)
            if core_info is not None:
                core, core_file = core_info
                
                index_js_path = core + '\\index.js'
                        
                if not os.path.exists(index_js_path):
                    open(index_js_path, 'w').close()

                with open(index_js_path, 'w', encoding='utf-8') as f:
                    f.write("module.exports = require('./core.asar');")
        
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The discord injection was deleted.")
    except Exception as e:
        Error_Console(e)

def RealTimeProtection(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-MpPreference | Select-Object -ExpandProperty DisableRealtimeMonitoring'], 
                                capture_output=True, text=True)
        if "False" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -DisableRealtimeMonitoring $true'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Real Time Protection: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -DisableRealtimeMonitoring $false'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Real Time Protection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsFirewall(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-NetFirewallProfile | Select-Object -ExpandProperty Enabled'], 
                                capture_output=True, text=True)
        if "True" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Firewall: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Firewall: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def CloudProtection(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-MpPreference | Select-Object -ExpandProperty MAPSReporting'], 
                                capture_output=True, text=True)
        if "2" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -MAPSReporting Disabled'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cloud Protection: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -MAPSReporting Advanced'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cloud Protection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def SampleSubmission(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-MpPreference | Select-Object -ExpandProperty SubmitSamplesConsent'], 
                                capture_output=True, text=True)
        if "1" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -SubmitSamplesConsent 0'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Sample Submission: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -SubmitSamplesConsent 1'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Sample Submission: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def DeviceSecurity(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard -Name EnableVirtualizationBasedSecurity'], 
                                capture_output=True, text=True)
        if "1" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = False

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard -Name EnableVirtualizationBasedSecurity -Value 0'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Device Security: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard -Name EnableVirtualizationBasedSecurity -Value 1'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Device Security: {white}Enabled")
    except Exception as e:
        Error_Console(f"Error changing Device Security state: {e}")

    return state_now

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px

def ZeroDayProtection(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-MpPreference | Select-Object -ExpandProperty CloudBlockLevel'], 
                                capture_output=True, text=True)
        if "2" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -CloudBlockLevel 1'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Zero Day Protection: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-MpPreference -CloudBlockLevel 2'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Zero Day Protection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def AppAndBrowserControl(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-ItemProperty -Path HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer -Name SmartScreenEnabled'], 
                                capture_output=True, text=True)
        if "RequireAdmin" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer -Name SmartScreenEnabled -Value Off'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App and Browser Control: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer -Name SmartScreenEnabled -Value RequireAdmin'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App and Browser Control: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def MemoryIntegrity(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\CredentialGuard -Name Enabled'], 
                                capture_output=True, text=True)
        if "1" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\CredentialGuard" -Name "Enabled" -Value 0'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Memory Integrity: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\CredentialGuard" -Name "Enabled" -Value 1'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Memory Integrity: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def UserAccountControl(state=None):
    try:
        result = subprocess.run(['powershell', '-Command', r'Get-ItemProperty -Path HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System -Name EnableLUA'], 
                                capture_output=True, text=True)
        if "1" in result.stdout.strip():
            state_now = True
        else:
            state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System -Name EnableLUA -Value 0'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Account Control: {white}Disabled")
        elif state == "enable":
            subprocess.run(['powershell', '-Command', r'Set-ItemProperty -Path HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System -Name EnableLUA -Value 1'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} User Account Control: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

# ------------------------------------------
# --------------> MONITORING <--------------
# ------------------------------------------

def DataCollection(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\DataCollection', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "AllowTelemetry")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except: 
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Policies\Microsoft\Windows\DataCollection',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AllowTelemetry', 0, winreg.REG_SZ, '0')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Data Collection: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Policies\Microsoft\Windows\DataCollection',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AllowTelemetry', 0, winreg.REG_SZ, '1')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Data Collection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def CEIPDataCollection(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\SQMClient\Windows', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "CEIPEnable")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\SQMClient\Windows',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'CEIPEnable', 0, winreg.REG_SZ, '0')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CEIP Data Collection: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\SQMClient\Windows',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'CEIPEnable', 0, winreg.REG_SZ, '1')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CEIP Data Collection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsEventCollector(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\Wecsvc', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Start")
            if "4" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\Wecsvc',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_SZ, '4')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Event Collector: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\Wecsvc',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_SZ, '2')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Event Collector: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsErrorReporting(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\Windows Error Reporting', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Disabled")
            if "1" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\Windows Error Reporting',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Disabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Error Reporting: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\Windows Error Reporting',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Disabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Error Reporting: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsSearch(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\WSearch', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Start")
            if "4" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\WSearch',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_SZ, '4')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Search: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\WSearch',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_SZ, '2')
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Search: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def CortanaSearchHistory(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Personalization\Settings', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "AcceptedPrivacyPolicy")
            if "0" in str(value):
                state_now = True 
            else:
                state_now = False
    except FileNotFoundError:
        state_now = None  

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'SOFTWARE\Microsoft\Personalization\Settings',
                                 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AcceptedPrivacyPolicy', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cortana Search History: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'SOFTWARE\Microsoft\Personalization\Settings',
                                 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AcceptedPrivacyPolicy', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Cortana Search History {white}Enable{red}.")
    except Exception as e:
        print(f"Erreur : {e}")

    return state_now

def SmartScreen(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "SmartScreenEnabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SmartScreenEnabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} SmartScreen: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SmartScreenEnabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} SmartScreen: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsTargetedAdvertising(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Enabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Enabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Targeted Advertising: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Enabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Targeted Advertising: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsContentSuggestions(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "SubscribedContent-338387Enabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SubscribedContent-338387Enabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Content Suggestions: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SubscribedContent-338387Enabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Content Suggestions: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def KeystrokeCollectionService(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\InputPersonalization', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "RestrictImplicitTextCollection")
            if "1" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\InputPersonalization',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'RestrictImplicitTextCollection', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Keystroke Collection: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\InputPersonalization',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'RestrictImplicitTextCollection', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Keystroke Collection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def CompatTelRunner(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\DiagSvc', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Start")
            if "4" in str(value):
                state_now = True
            else:
                state_now = False
    except FileNotFoundError:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\DiagTrack', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Start")
            if "4" in str(value):
                state_now = True
            else:
                state_now = False

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\DiagSvc',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CompatTelRunner: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\DiagSvc',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 2)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CompatTelRunner: {white}Enabled")
    except FileNotFoundError:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\DiagTrack',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CompatTelRunner: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SYSTEM\CurrentControlSet\Services\DiagTrack',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 2)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} CompatTelRunner: {white}Enabled")

    return state_now

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px

def DataCollectionInstalledPrograms(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Installer', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "DisableAutomaticCheckForUpdates")
            if "1" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Installer',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'DisableAutomaticCheckForUpdates', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Data Collection for Installed Programs: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Installer',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'DisableAutomaticCheckForUpdates', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Data Collection for Installed Programs: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WifiSenseAnonymity(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "AutoConnectAllowedOEM")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AutoConnectAllowedOEM', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} WifiSense Anonymity: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'AutoConnectAllowedOEM', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} WifiSense Anonymity: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def AdvertisingID(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "Enabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Enabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Advertising ID: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'Enabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Advertising ID: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def AppSuggestions(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "SubscribedContent-338389Enabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SubscribedContent-338389Enabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App Suggestions: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SubscribedContent-338389Enabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} App Suggestions: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def FileExplorerSuggestions(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "ShowSyncProviderNotifications")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'ShowSyncProviderNotifications', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} File Explorer Suggestions: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'ShowSyncProviderNotifications', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} File Explorer Suggestions: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def WindowsSpotlight(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "RotatingLockScreenEnabled")
            if "0" in str(value):
                state_now = True
            else:
                state_now = False
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'RotatingLockScreenEnabled', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Spotlight: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'RotatingLockScreenEnabled', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Windows Spotlight: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def KeyboardDataCollection(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "HarvestContacts")
            state_now = value == 0
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'HarvestContacts', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Keyboard Data Collection: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'HarvestContacts', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Keyboard Data Collection: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

def DefenderTelemetry(state=None):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows Defender\Spynet', 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, "SpyNetReporting")
            state_now = value == 0
    except:
        state_now = None

    try:
        if state == "disable":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows Defender\Spynet',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SpyNetReporting', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Defender Telemetry: {white}Disabled")

        elif state == 'enable':
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Microsoft\Windows Defender\Spynet',
                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'SpyNetReporting', 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Defender Telemetry: {white}Enabled")
    except Exception as e:
        Error_Console(e)

    return state_now

# --------------------------------------
# --------------> FOLDER <--------------
# --------------------------------------

def Folder_Encryption(status, path_folder, password):
    global error
    error = 0

    if not path_folder:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Please set the folder path.")
        return

    if not password:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Please set folder password.")
        return

    def generate_key_from_password(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def encrypt_filename(filename, key, iv):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_filename = padder.update(filename.encode()) + padder.finalize()

        encrypted_filename = encryptor.update(padded_filename) + encryptor.finalize()
        return base64.urlsafe_b64encode(encrypted_filename).decode().rstrip("=")

    def decrypt_filename(encrypted_filename, key, iv):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        encrypted_filename_bytes = base64.urlsafe_b64decode(encrypted_filename + '==')
        padded_filename = decryptor.update(encrypted_filename_bytes) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        filename = unpadder.update(padded_filename) + unpadder.finalize()
        return filename.decode()

    def encrypt_file(path_file, key, salt):
        with open(path_file, 'rb') as file:
            plaintext = file.read()

        iv_content = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv_content), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()

        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        original_filename = os.path.basename(path_file)
        iv_filename = os.urandom(16)
        encrypted_filename = encrypt_filename(original_filename, key, iv_filename)

        encrypted_file_path = os.path.join(os.path.dirname(path_file), encrypted_filename + '.Oblivion.enc')

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(salt + iv_content + iv_filename + ciphertext)

        os.remove(path_file)

    def decrypt_file(path_file, password):
        global error
        try:
            with open(path_file, 'rb') as encrypted_file:
                salt = encrypted_file.read(32)
                iv_content = encrypted_file.read(16)
                iv_filename = encrypted_file.read(16)
                ciphertext = encrypted_file.read()

            key = generate_key_from_password(password, salt)

            encrypted_filename = os.path.basename(path_file)[:-13]
            original_filename = decrypt_filename(encrypted_filename, key, iv_filename)

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv_content), backend=default_backend())
            decryptor = cipher.decryptor()

            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

            decrypted_file_path = os.path.join(os.path.dirname(path_file), original_filename)

            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(plaintext)

            os.remove(path_file)

        except (ValueError, KeyError):
            error += 1
            print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Incorrect password: {white + password + red}")
            Error(f"Incorrect password: {password}")
            return

    def encrypt_folder(path_folder, password):
        files_to_encrypt = []
        for root, dirs, files in os.walk(path_folder):
            for file in files:
                if not file.endswith('.Oblivion.enc'):
                    files_to_encrypt.append(os.path.join(root, file))

        for path_file in tqdm(files_to_encrypt, desc=f"{BEFORE + current_time_hour() + AFTER} {WAIT} Encryption Progress", unit="file"):
            salt = os.urandom(32)
            key = generate_key_from_password(password, salt)
            encrypt_file(path_file, key, salt)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The folder has been encrypted: {white + path_folder}")
        Info("The folder has been encrypted !")

    def decrypt_folder(path_folder, password):
        files_to_decrypt = []
        for root, dirs, files in os.walk(path_folder):
            for file in files:
                if not error >= 1:
                    if file.endswith('.Oblivion.enc'):
                        files_to_decrypt.append(os.path.join(root, file))
                else:
                    return

        for path_file in tqdm(files_to_decrypt, desc=f"{BEFORE + current_time_hour() + AFTER} {WAIT} Decryption Progress", unit="file"):
            if not error >= 1:
                decrypt_file(path_file, password)
            else:
                return
            
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The folder has been decrypted: {white + path_folder}")
        Info("The folder has been decrypted !")

    if status == "encrypt":
        encrypt_folder(path_folder, password)
    elif status == "decrypt":
        decrypt_folder(path_folder, password)



def Startup(status=None):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Run, 0, winreg.KEY_READ) 
        value, _ = winreg.QueryValueEx(registry_key, title)
        winreg.CloseKey(registry_key)
        status_now = True
    except FileNotFoundError:
        status_now = False
    except:
        status_now = False

    try:
        if status == "enable":
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Run, 0, winreg.KEY_SET_VALUE) 
            winreg.SetValueEx(registry_key, title, 0, winreg.REG_SZ, f'"{path_App}"')
            winreg.CloseKey(registry_key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Startup Enable.")
        elif status == "disable":
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path_Run, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(registry_key, title)
            winreg.CloseKey(registry_key)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Startup Disabled.")
    except Exception as e:
        Error_Console(e)

    return status_now

def Shutdown():
    reponse = messagebox.askquestion(title, "Do you want to restart your pc ? (recommended)")

    if reponse in ['yes', 'YES', 'Yes', 'oui', 'OUI', 'Oui']:
        number = 5
        while True:
            if number != 0:
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Shutdown in: {white + str(number)}s")
                number -= 1
                time.sleep(1)
            else:
                break
        os.system("shutdown /r /t 0")
    else:
        print("Vous avez choisi Non.")


def Software():
    def run(function, *args):
        threading.Thread(target=function, daemon=True, args=args if args else ()).start()

    def display_pc_info():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        def system_info():
            return {
                "Os": f"{Os} (v{Os_Version})",
                "Hostname": Hostname,
                "Machine Id": Machine_Id,
                "Machine Guid": Machine_Guid,
                "Hw Profile Guid": Hw_Profile_Guid,
                "Nvidia System Id": Nvidia_System_Id,
                "Guid Serial Number": Guid_Serial_Number,
                "Uuid Serial Number": Uuid_Serial_Number,
                "Motherboard Serial Number": Motherboard_Serial_Number,
                "Motherboard Product": Motherboard_Product_Serial_Number,
                "Motherboard Manufacturer": Motherboard_Manufacturer_Serial_Number,
                "Processor Serial Number": Processor_Serial_Number,
                "Bios Serial Number": Bios_Serial_Number,
                "Bios Release Date": Bios_Release_Date,
                "Bios Version": Bios_Version,
                "System Bios Version": System_Bios_Version,
                "System Version": System_Version,
                "System Family": System_Family_Serial_Number,
                "System Manufacturer": System_Manufacturer_Serial_Number,
                "System Product": System_Product_Serial_Number,
                "System SKU": System_SKU_Serial_Number,
                "Chassis Serial Number": Chassis_Serial_Number,
                "Oem String Serial Number": OemString_Serial_Number,
                "Asset Tag Serial Number": Asset_Tag,
            }
        
        def DownloadInformation():
            path = ChooseFolder()
            path_file = os.path.join(path, f"Information - {Hostname}.txt")
            with open(path_file, 'w', encoding='utf-8') as file:
                file.write(f"Computer information from {Hostname}:\n")
                for key, value in system_info().items():
                    file.write(f"[+] {key:<35} : {value}\n")
                for disk, hwid in disk_values.items():
                    file.write(f"[+] {'Hwid Disk ' + disk :<35} : {hwid}\n")
            
        image = ctk.CTkImage(light_image=Image.open(Img["logo_glass"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Pc Information", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        frame = ctk.CTkScrollableFrame(display_right, width=614, height=314, fg_color=colors["light_background"])
        frame.grid(row=1, column=0, pady=(10, 0), padx=(10, 0), sticky="nsew")

        row_num = 1
        for key, value in system_info().items():
            key_label = ctk.CTkLabel(frame, text=f"{key}", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w")
            key_label.grid(row=row_num, column=0, sticky="w", padx=(10, 0), pady=2)

            value_label = ctk.CTkLabel(frame, text=f":", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w")
            value_label.grid(row=row_num, column=1, sticky="w", padx=10, pady=2)

            value_label = ctk.CTkLabel(frame, text=f"{value}", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w", text_color=colors["light_light_gray"])
            value_label.grid(row=row_num, column=2, sticky="w", padx=0, pady=2)
            
            row_num += 1

        row_num = 52
        for disk, hwid in disk_values.items():
            disk_key = ctk.CTkLabel(frame, text=f"Hwid Disk {disk}\\", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w")
            disk_key.grid(row=row_num, column=0, sticky="w", padx=(10, 0), pady=2)

            value_label = ctk.CTkLabel(frame, text=f":", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w")
            value_label.grid(row=row_num, column=1, sticky="w", padx=10, pady=2)

            hwid_key = ctk.CTkLabel(frame, text=f"{hwid}", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), anchor="w", text_color=colors["light_light_gray"])
            hwid_key.grid(row=row_num, column=2, sticky="w", padx=0, pady=2)

            row_num += 1

        download_image = ctk.CTkImage(light_image=Image.open(Img["logo_file"]), size=(22, 22))
        download_select = ctk.CTkButton(display_right, text="Download All Information", font=ctk.CTkFont(family="Helvetica", size=13,), 
                                            width=640, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                            image=download_image, command=DownloadInformation)
        download_select.grid(row=2, column=0, pady=10, padx=(10, 0), columnspan=3, sticky="w")

        loading = False

    def display_spoofer():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        def SerialNumber(choice):
            run(SerialNumber_Changer, choice)
            Info("Serial Number Spoofed.")

        def Spoofer(choice):
            if "Regedit Clean" in choice:
                run(Regedit_Clean)
            if "Hostname Changer" in choice:
                run(HostName_Changer)
            if "Spoof Launcher/Games" in choice:
                run(LauncherGames_Spoof)
            Info("Everything that was selected was spoofed.")

        Title = ctk.CTkLabel(display_right, text=" Hardware Spoofer", compound="left",
                             font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), 
                             image=ctk.CTkImage(light_image=Image.open(Img["logo_spoofer"]), size=(40, 40))
        ).grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        serial_number_frame = ctk.CTkScrollableFrame(display_right, width=290, height=314, fg_color=colors["light_background"]) 
        serial_number_frame.grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0), padx=(10, 0))
        serial_number_frame.grid_columnconfigure(0, weight=1)
        serial_number_frame.grid_columnconfigure(1, weight=1)
        serial_number_frame.grid_columnconfigure(2, weight=1)

        title = ctk.CTkLabel(serial_number_frame, text=" Serial Number", compound="left",
                             font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), 
                             image=ctk.CTkImage(light_image=Image.open(Img["logo_hardware"]), size=(25, 25))
        ).grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")
        
        checkboxes_text_serial = [
            "Machine Id", "Machine Guid", "Hw Profile Guid", "Nvidia System Id", "Guid Serial Number", "Uuid Serial Number",
            "Hwid Disk Serial Number", "Motherboard Serial Number", "Motherboard Product", "Motherboard Manufacturer",
            "Processor Serial Number", "Chassis Serial Number", "Bios Serial Number", "Bios Release Date", "Bios Version", "System Bios Version", 
            "System Version", "System Family", "System Manufacturer", "System Product", "System SKU",
            "Oem String Serial Number", "Asset Tag Serial Number",
        ]

        checkboxes_serial = []
        selected_choices_serial = []

        def on_checkbox_change_serial(selected_text, var):
            if var.get():
                selected_choices_serial.append(selected_text)
            else:
                if selected_text in selected_choices_serial:
                    selected_choices_serial.remove(selected_text)

        for idx, text in enumerate(checkboxes_text_serial):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                serial_number_frame, 
                text=text, 
                variable=var, 
                command=lambda 
                selected_text=text, 
                var=var: on_checkbox_change_serial(selected_text, var), 
                text_color=colors["white"],
                fg_color=colors['light_light_gray'],
                hover_color=colors['light_light_gray'],
                border_color=colors['light_light_gray'],
                font=ctk.CTkFont(family="Helvetica", size=14)
            )
            checkbox.grid(row=idx + 1, column=0, sticky="w", pady=6, padx=2)
            checkboxes_serial.append(checkbox)

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px


        def on_select_button_click_serial():
            run(lambda: SerialNumber(selected_choices_serial))

        serial_number_image = ctk.CTkImage(light_image=Image.open(Img["logo_hardware"]), size=(22, 22))
        serial_number_select = ctk.CTkButton(
            display_right, 
            text="Spoof Serial Number", 
            font=ctk.CTkFont(family="Helvetica", size=13,),   
            width=312, 
            height=40, 
            fg_color=colors["light_gray"], 
            hover_color=colors["gray"], 
            image=serial_number_image, 
            command=on_select_button_click_serial
        )
        serial_number_select.grid(row=2, column=0, pady=10, padx=(10, 0), columnspan=3, sticky="w")



        spoofer_frame = ctk.CTkScrollableFrame(display_right, width=290, height=314, fg_color=colors["light_background"])
        spoofer_frame.grid(row=1, column=0, columnspan=3, sticky="e", pady=(10, 0), padx=(0, 10))
        spoofer_frame.grid_columnconfigure(0, weight=1)
        spoofer_frame.grid_columnconfigure(1, weight=1)
        spoofer_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_spoofing"]), size=(25, 25))
        title = ctk.CTkLabel(spoofer_frame, text=" Other Spoofing", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        checkboxes_text_spoofer = ["Hostname Changer", "Regedit Clean", "Spoof Launcher/Games"]

        checkboxes_spoofer = []
        selected_choices_spoofer = []

        def on_checkbox_change_spoofer(selected_text, var):
            if var.get():
                selected_choices_spoofer.append(selected_text)
            else:
                if selected_text in selected_choices_spoofer:
                    selected_choices_spoofer.remove(selected_text)

        for idx, text in enumerate(checkboxes_text_spoofer):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                spoofer_frame, 
                text=text, 
                variable=var, 
                command=lambda 
                selected_text=text, 
                var=var: on_checkbox_change_spoofer(selected_text, var), 
                text_color=colors["white"],
                fg_color=colors['light_light_gray'],
                hover_color=colors['light_light_gray'],
                border_color=colors['light_light_gray'],
                font=ctk.CTkFont(family="Helvetica", size=14)
            )
            checkbox.grid(row=idx + 1, column=0, sticky="w", pady=6, padx=2)
            checkboxes_spoofer.append(checkbox)

        def on_select_button_click_spoofer():
            run(lambda: Spoofer(selected_choices_spoofer))

        spoofer_image = ctk.CTkImage(light_image=Image.open(Img["logo_spoofing"]), size=(22, 22))
        spoofer_number = ctk.CTkButton(display_right, text="Spoof Selected", font=ctk.CTkFont(family="Helvetica", size=13,), 
                                        width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                        image=spoofer_image, command=on_select_button_click_spoofer)
        spoofer_number.grid(row=2, column=0, pady=10, padx=(0, 10), columnspan=3, sticky="e")

        loading = False

    def display_monitoring():
        global loading
        loading = True
        
        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_monitoring"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Windows Monitoring", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")
        
        def DisableDataCollection():
            DataCollection("disable")    

        def EnableDataCollection():
            DataCollection("enable")

        def DisableCEIPDataCollection():
            CEIPDataCollection("disable")

        def EnableCEIPDataCollection():
            CEIPDataCollection("enable")

        def DisableWindowsEventCollector():
            WindowsEventCollector("disable")

        def EnableWindowsEventCollector():
            WindowsEventCollector("enable")

        def DisableWindowsErrorReporting():
            WindowsErrorReporting("disable")

        def EnableWindowsErrorReporting():
            WindowsErrorReporting("enable")

        def DisableWindowsSearch():
            WindowsSearch("disable")

        def EnableWindowsSearch():
            WindowsSearch("enable")

        def DisableCortanaSearchHistory():
            CortanaSearchHistory("disable")

        def EnableCortanaSearchHistory():
            CortanaSearchHistory("enable")

        def DisableSmartScreen():
            SmartScreen("disable")

        def EnableSmartScreen():
            SmartScreen("enable")

        def DisableWindowsContentSuggestions():
            WindowsContentSuggestions("disable")

        def EnableWindowsContentSuggestions():
            WindowsContentSuggestions("enable")

        def DisableTargetedAdvertising():
            WindowsTargetedAdvertising("disable")

        def EnableTargetedAdvertising():
            WindowsTargetedAdvertising("enable")

        def DisableKeystrokeCollection():
            KeystrokeCollectionService("disable")

        def EnableKeystrokeCollection():
            KeystrokeCollectionService("enable")

        def DisableWifiSenseAnonymity():
            WifiSenseAnonymity("disable")

        def EnableWifiSenseAnonymity():
            WifiSenseAnonymity("enable")

        def DisableCompatTelRunner():
            CompatTelRunner("disable")

        def EnableCompatTelRunner():
            CompatTelRunner("enable")

        def DisableProgramDataCollection():
            DataCollectionInstalledPrograms("disable")

        def EnableProgramDataCollection():
            DataCollectionInstalledPrograms("enable")

        def DisableAdvertisingID():
            AdvertisingID("disable")

        def EnableAdvertisingID():
            AdvertisingID("enable")

        def DisableAppSuggestions():
            AppSuggestions("disable")

        def EnableAppSuggestions():
            AppSuggestions("enable")

        def DisableFileExplorerSuggestions():
            FileExplorerSuggestions("disable")

        def EnableFileExplorerSuggestions():
            FileExplorerSuggestions("enable")

        def DisableWindowsSpotlight():
            WindowsSpotlight("disable")

        def EnableWindowsSpotlight():
            WindowsSpotlight("enable")
        
        def DisableDefenderTelemetry():
            DefenderTelemetry("disable")

        def EnableDefenderTelemetry():
            DefenderTelemetry("enable")

        def DisableKeyboardDataCollection():
            KeyboardDataCollection("disable")

        def EnableKeyboardDataCollection():
            KeyboardDataCollection("enable")
        
        
        monitoring_frame = ctk.CTkScrollableFrame(display_right, width=290, height=365, fg_color=colors["light_background"])
        monitoring_frame.grid(row=1, column=0, columnspan=3, sticky="we", pady=(10, 0), padx=10)
        monitoring_frame.grid_columnconfigure(0, weight=1)
        monitoring_frame.grid_columnconfigure(1, weight=1)
        monitoring_frame.grid_columnconfigure(2, weight=1)

        monitoring_vars = {}

        monitoring_controls = [
            ("Disable Data Collection", lambda: run(EnableDataCollection) if not monitoring_DataCollection.get() else run(DisableDataCollection)),
            ("Disable Program Data Collection", lambda: run(EnableProgramDataCollection) if not monitoring_ProgramDataCollection.get() else run(DisableProgramDataCollection)),
            ("Disable CEIP Data Collection", lambda: run(EnableCEIPDataCollection) if not monitoring_CEIPDataCollection.get() else run(DisableCEIPDataCollection)),
            ("Disable Keyboard Data Collection", lambda: run(EnableKeyboardDataCollection) if not monitoring_KeyboardDataCollection.get() else run(DisableKeyboardDataCollection)),
            ("Disable Defender Telemetry", lambda: run(EnableDefenderTelemetry) if not monitoring_DefenderTelemetry.get() else run(DisableDefenderTelemetry)),
            ("Disable Windows Event Collector", lambda: run(EnableWindowsEventCollector) if not monitoring_WindowsEventCollector.get() else run(DisableWindowsEventCollector)),
            ("Disable Windows Error Reporting", lambda: run(EnableWindowsErrorReporting) if not monitoring_WindowsErrorReporting.get() else run(DisableWindowsErrorReporting)),
            ("Disable Windows Spotlight", lambda: run(EnableWindowsSpotlight) if not monitoring_windows_spotlight.get() else run(DisableWindowsSpotlight)),
            ("Disable Windows Content Suggestions", lambda: run(EnableWindowsContentSuggestions) if not monitoring_WindowsContentSuggestions.get() else run(DisableWindowsContentSuggestions)),
            ("Disable App Suggestions", lambda: run(EnableAppSuggestions) if not monitoring_app_suggestions.get() else run(DisableAppSuggestions)),
            ("Disable File Explorer Suggestions", lambda: run(EnableFileExplorerSuggestions) if not monitoring_file_explorer_suggestions.get() else run(DisableFileExplorerSuggestions)),
            ("Disable Windows Search", lambda: run(EnableWindowsSearch) if not monitoring_WindowsSearch.get() else run(DisableWindowsSearch)),
            ("Disable Cortana Search History", lambda: run(EnableCortanaSearchHistory) if not monitoring_CortanaSearchHistory.get() else run(DisableCortanaSearchHistory)),
            ("Disable Smart Screen", lambda: run(EnableSmartScreen) if not monitoring_SmartScreen.get() else run(DisableSmartScreen)),
            ("Disable Targeted Advertising", lambda: run(EnableTargetedAdvertising) if not monitoring_TargetedAdvertising.get() else run(DisableTargetedAdvertising)),
            ("Disable Advertising ID", lambda: run(EnableAdvertisingID) if not monitoring_advertising_id.get() else run(DisableAdvertisingID)),
            ("Disable Keystroke Collection", lambda: run(EnableKeystrokeCollection) if not monitoring_KeystrokeCollection.get() else run(DisableKeystrokeCollection)),
            ("Disable CompatTelRunner", lambda: run(EnableCompatTelRunner) if not monitoring_CompatTelRunner.get() else run(DisableCompatTelRunner)),
            ("Config WifiSense", lambda: run(EnableWifiSenseAnonymity) if not monitoring_WifiSenseAnonymity.get() else run(DisableWifiSenseAnonymity)),
        ]

        space = ctk.CTkLabel(monitoring_frame, text=" "
        ).grid(pady=0)

        for idx, (text, command) in enumerate(monitoring_controls):
            monitoring_var = ctk.BooleanVar(value=False)
            monitoring_vars[text] = monitoring_var

            if text == 'Disable Data Collection':
                state_now = DataCollection()
                monitoring_DataCollection = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_DataCollection

            elif text == 'Disable CEIP Data Collection':
                state_now = CEIPDataCollection()
                monitoring_CEIPDataCollection = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_CEIPDataCollection

            elif text == 'Disable Windows Event Collector':
                state_now = WindowsEventCollector()
                monitoring_WindowsEventCollector = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_WindowsEventCollector

            elif text == 'Disable Windows Error Reporting':
                state_now = WindowsErrorReporting()
                monitoring_WindowsErrorReporting = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_WindowsErrorReporting

            elif text == 'Disable Windows Search':
                state_now = WindowsSearch()
                monitoring_WindowsSearch = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_WindowsSearch

            elif text == 'Disable Cortana Search History':
                state_now = CortanaSearchHistory()
                monitoring_CortanaSearchHistory = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_CortanaSearchHistory

            elif text == 'Disable Smart Screen':
                state_now = SmartScreen()
                monitoring_SmartScreen = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_SmartScreen

            elif text == 'Disable Windows Content Suggestions':
                state_now = WindowsContentSuggestions()
                monitoring_WindowsContentSuggestions = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_WindowsContentSuggestions

            elif text == 'Disable Targeted Advertising':
                state_now = WindowsTargetedAdvertising()
                monitoring_TargetedAdvertising = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_TargetedAdvertising

            elif text == 'Disable Keystroke Collection':
                state_now = KeystrokeCollectionService()
                monitoring_KeystrokeCollection = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_KeystrokeCollection

            elif text == 'Config WifiSense':
                state_now = WifiSenseAnonymity()
                monitoring_WifiSenseAnonymity = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_WifiSenseAnonymity

            elif text == 'Disable CompatTelRunner':
                state_now = CompatTelRunner()
                monitoring_CompatTelRunner = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_CompatTelRunner

            elif text == 'Disable Program Data Collection':
                state_now = DataCollectionInstalledPrograms()
                monitoring_ProgramDataCollection = ctk.BooleanVar(value=state_now is not None and state_now)
                monitoring_var = monitoring_ProgramDataCollection

            elif text == 'Disable Advertising ID':
                state_now = AdvertisingID()
                monitoring_advertising_id = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_advertising_id

            elif text == 'Disable App Suggestions':
                state_now = AppSuggestions()
                monitoring_app_suggestions = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_app_suggestions

            elif text == 'Disable File Explorer Suggestions':
                state_now = FileExplorerSuggestions()
                monitoring_file_explorer_suggestions = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_file_explorer_suggestions

            elif text == 'Disable Windows Spotlight':
                state_now = WindowsSpotlight()
                monitoring_windows_spotlight = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_windows_spotlight
            
            elif text == 'Disable Keyboard Data Collection':
                state_now = KeyboardDataCollection()
                monitoring_KeyboardDataCollection = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_KeyboardDataCollection
            
            elif text == 'Disable Defender Telemetry':
                state_now = DefenderTelemetry()
                monitoring_DefenderTelemetry = ctk.BooleanVar(value=state_now is not None and state_now == True)
                monitoring_var = monitoring_DefenderTelemetry

            column = idx % 2 
            row = idx // 2

            switch = ctk.CTkSwitch(
                monitoring_frame,
                text=text,
                command=command,
                variable=monitoring_var,
                onvalue=True,
                offvalue=False,           
                text_color=colors["white"],
                fg_color=colors['light_gray'],
                button_color=colors["white"],
                progress_color=colors["light_light_gray"],
                font=ctk.CTkFont(family="Helvetica", size=14),
            )

            switch.grid(row=row + 3, column=column, padx=3, pady=6, sticky="w")

        loading = False

# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px


    def display_folder():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        global path_folder_encrypt
        global path_folder_decrypt

        path_folder_encrypt = None
        path_folder_decrypt = None

        def choose_folder_encrypt():
            global path_folder_encrypt
            path_folder_encrypt = filedialog.askdirectory()
            text_path_folder_encrypt.configure(text=f"{path_folder_encrypt}")

        def choose_folder_decrypt():
            global path_folder_decrypt
            path_folder_decrypt = filedialog.askdirectory()
            text_path_folder_decrypt.configure(text=f"{path_folder_decrypt}")

        def Folder_Action(status, path_folder):
            if status == "encrypt":
                password = password_entry_encrypt.get()
                Folder_Encryption(status, path_folder, password)
            elif status == "decrypt":
                password = password_entry_decrypt.get()
                Folder_Encryption(status, path_folder, password)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_folder_encrypted"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Folder Encryption", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        encrypt_frame = ctk.CTkFrame(display_right, width=312, height=376, fg_color=colors["light_background"]) 
        encrypt_frame.grid(row=1, column=0, sticky="w", pady=(10, 0), padx=(10, 0))
        encrypt_frame.grid_propagate(False)
        encrypt_frame.grid_columnconfigure(0, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_lock"]), size=(25, 25))
        title = ctk.CTkLabel(encrypt_frame, text=" Encryption", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(15, 15), padx=0, sticky="ew")

        image = ctk.CTkImage(light_image=Image.open(Img["logo_folder_lock"]), size=(23, 23))
        button = ctk.CTkButton(encrypt_frame, text="Select Folder Path", image=image, compound="left", command=choose_folder_encrypt, fg_color=colors["light_gray"], hover_color=colors["gray"], text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=14), 
            **{
                "width": 0, 
                "height": 40,
            }
        )
        button.grid(row=1, column=0, columnspan=3, padx=10, pady=0, sticky="we")

        path_frame = ctk.CTkFrame(encrypt_frame, fg_color=colors["gray"]) 
        path_frame.grid(row=2, column=0, columnspan=3, pady=20, padx=10, sticky="we")  

        text_path_folder_encrypt  = ctk.CTkLabel(path_frame, text=f"Folder Path..", font=ctk.CTkFont(family="Helvetica", size=12), compound="left", wraplength=275)
        text_path_folder_encrypt.grid(row=1, column=0, columnspan=3, pady=6, padx=10, sticky="w")

        password_entry_encrypt = ctk.CTkEntry(encrypt_frame, placeholder_text="Create a Password")
        password_entry_encrypt.grid(row=3, column=0, columnspan=3, pady=(10, 5), padx=50, sticky="we")

        encrypt_button = ctk.CTkButton(encrypt_frame, text="Encrypt Folder", command=lambda: run(Folder_Action, "encrypt", path_folder_encrypt), fg_color=colors["light_gray"], hover_color=colors["gray"], text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
            **{
                "width": 0,
                "height": 40,
            }
        )
        encrypt_button.grid(row=5, column=0, columnspan=3, pady=(94, 0), padx=50, sticky="we")

        decrypt_frame = ctk.CTkFrame(display_right, width=312, height=376, fg_color=colors["light_background"])
        decrypt_frame.grid(row=1, column=1, sticky="e", pady=(10, 0), padx=(0, 1))
        decrypt_frame.grid_propagate(False)
        decrypt_frame.grid_columnconfigure(0, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_unlock"]), size=(25, 25))
        title = ctk.CTkLabel(decrypt_frame, text=" Decryption", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(16, 16), padx=0, sticky="ew")

        image = ctk.CTkImage(light_image=Image.open(Img["logo_folder_unlock"]), size=(23, 23))
        button = ctk.CTkButton(decrypt_frame, text="Select Folder Path", image=image, compound="left", command=choose_folder_decrypt, fg_color=colors["light_gray"], hover_color=colors["gray"], text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=14), 
            **{
                "width": 0, 
                "height": 40,
            }
        )
        button.grid(row=1, column=0, columnspan=3, padx=10, pady=0, sticky="we")

        path_frame = ctk.CTkFrame(decrypt_frame, fg_color=colors["gray"]) 
        path_frame.grid(row=2, column=0, columnspan=3, pady=20, padx=10, sticky="we")  

        text_path_folder_decrypt = ctk.CTkLabel(path_frame, text=f"Folder Path..", font=ctk.CTkFont(family="Helvetica", size=12), compound="left", wraplength=275)
        text_path_folder_decrypt.grid(row=1, column=0, columnspan=3, pady=6, padx=10, sticky="we")

        password_entry_decrypt = ctk.CTkEntry(decrypt_frame, placeholder_text="Enter Password")
        password_entry_decrypt.grid(row=3, column=0, columnspan=3, pady=(10, 5), padx=50, sticky="we")

        decrypt_button = ctk.CTkButton(decrypt_frame, text="Decrypt Folder", command=lambda: run(Folder_Action, "decrypt", path_folder_decrypt), fg_color=colors["light_gray"], hover_color=colors["gray"], text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
            **{
                "width": 0,
                "height": 40,
            }
        )
        decrypt_button.grid(row=5, column=0, columnspan=3, pady=(94, 0), padx=50, sticky="we")

        loading = False

    def display_data():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        def generated_password():
            password = ''.join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ==++--..__@@!!??**") for _ in range(random.randint(25, 30)))
            text_generated_password.configure(text=password)

        def generated_email():
            email = ''.join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(random.randint(15, 20))) + "@email.com"
            text_generated_email.configure(text=email)

        def generated_identity():

            names = [
                "Martin", "Dupont", "Leroy", "Moreau", "Garnier", "Benoit", 
                "Lemoine", "David", "Durand", "Petit", "Guillet", "Fontaine", 
                "Brun", "Michel", "Lemaire", "Caron", "Garnier", "Rousseau", 
                "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", 
                "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"
            ]

            firstnames = [
                "Jean", "Marie", "Pierre", "Sophie", "Lucas", "Emma", "L�a", 
                "Noah", "Alice", "Julien", "Camille", "Th�o", "Lucas", 
                "Chlo�", "Antoine", "Clara", "Charlotte", "James", "Michael", 
                "Sarah", "Jessica", "Emily", "Daniel", "David", "Andrew"
            ]

            addresses = [
                "9-11 Pl. du Colonel Fabien, 75010 Paris, France",
                "12 Rue de Rivoli, 75004 Paris, France",
                "25 Rue du Faubourg Saint-Antoine, 75011 Paris, France",
                "30 Avenue des Champs-�lys�es, 75008 Paris, France",
                "15 Rue de la R�publique, 69001 Lyon, France",
                "5 Avenue Jean Jaur�s, 75019 Paris, France",
                "30 Rue du Parc, 67000 Strasbourg, France",
                "150 Boulevard Haussmann, 75008 Paris, France",
                "35 Boulevard Montmartre, 75002 Paris, France",
                "15 Place de la Bourse, 75002 Paris, France",
                "25 Acacia Avenue, London, N2 2AD, United Kingdom",
                "75 King�s Road, Chelsea, London, SW3 4NX, United Kingdom",
                "50 Oxford Street, London, W1D 1LL, United Kingdom",
                "18 Baker Street, London, NW1 6XE, United Kingdom",
                "221B Baker Street, London, NW1 6XE, United Kingdom",
                "100 Bishopsgate, London, EC2N 4AG, United Kingdom",
                "10 Downing Street, London, SW1A 2AA, United Kingdom",
                "12 Chelsea Embankment, London, SW3 4LE, United Kingdom",
                "30 Fenchurch Street, London, EC3M 3BD, United Kingdom",
                "1-3 Upper Brook Street, London, W1K 7RQ, United Kingdom"
            ]

            blood_groups = [
                "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"
            ]

            vehicles = [
                "Bicycle", "Car", "Motorcycle", "Truck", "Van", "Scooter", 
                "Bus", "Train", "Boat", "Airplane"
            ]

            jobs = [
                "Engineer", "Teacher", "Doctor", "Nurse", "Artist", "Scientist", 
                "Chef", "Developer", "Manager", "Writer", "Accountant", "Designer"
            ]
            name = random.choice(names)
            firstname = random.choice(firstnames)
            start_date = datetime.date(1960, 1, 1)
            end_date = datetime.date(2005, 12, 31)
            delta = end_date - start_date
            random_days = random.randint(0, delta.days)
            dateofbirth = start_date + datetime.timedelta(days=random_days)
            today = datetime.date.today()
            age = today.year - dateofbirth.year - ((today.month, today.day) < (dateofbirth.month, dateofbirth.day))
            height = random.randint(150, 200)
            weight = random.randint(50, 100) 
            bloodgroupe = random.choice(blood_groups)
            adress = random.choice(addresses)
            vehicle = random.choice(vehicles)
            job = random.choice(jobs)
            
            identity = f"Full Name: {name} {firstname}\nDate of Birth: {dateofbirth}\nAge: {age}\nHeight: {height} cm\nWeight: {weight} kg\nBlood Group: {bloodgroupe}\nAddress: {adress}\nVehicle: {vehicle}\nJob: {job}"
            text_generated_identity.configure(text=identity)


        def copy_to_clipboard(text):
            pyperclip.copy(text)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_data"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Data Generator", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        password_frame = ctk.CTkFrame(display_right, width=312, height=179, fg_color=colors["light_background"]) 
        password_frame.grid(row=1, column=0, sticky="wn", pady=(10, 0), padx=(10, 0))
        password_frame.grid_propagate(False)
        password_frame.grid_columnconfigure(0, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_lock_password"]), size=(25, 25))
        title = ctk.CTkLabel(password_frame, text=" Password Generator", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(16, 16), padx=0, sticky="ew")

        password_button = ctk.CTkButton(password_frame, text="Generate Password", command=lambda: generated_password(),
                                        fg_color=colors["light_gray"], hover_color=colors["gray"],
                                        text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                        **{"width": 0, "height": 40})
        password_button.grid(row=2, column=0, pady=(5, 10), padx=10, sticky="we")

        password_frame = ctk.CTkFrame(password_frame, fg_color=colors["gray"])
        password_frame.grid(row=3, column=0, pady=10, padx=10, sticky="we")  

        text_generated_password = ctk.CTkLabel(password_frame, text="Password Generate..                               ", 
                                                font=ctk.CTkFont(family="Helvetica", size=12), compound="left", wraplength=275)
        text_generated_password.grid(row=0, column=0, padx=10, pady=6, sticky="w")

        copy_password_button = ctk.CTkButton(password_frame, text="Copy", command=lambda: copy_to_clipboard(text_generated_password.cget("text")),
                                            fg_color=colors["light_gray"], hover_color=colors["gray"],
                                            text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                            **{"width": 0, "height": 30})
        copy_password_button.grid(row=0, column=1, padx=(10, 0), pady=6, sticky="e")


        email_frame = ctk.CTkFrame(display_right, width=312, height=179, fg_color=colors["light_background"]) 
        email_frame.grid(row=1, column=0, sticky="ws", pady=(10, 0), padx=(10, 0))
        email_frame.grid_propagate(False)
        email_frame.grid_columnconfigure(0, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_email"]), size=(25, 25))
        title = ctk.CTkLabel(email_frame, text=" Email Generator", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=4, column=0, columnspan=3, pady=(16, 16), padx=0, sticky="ew")

        email_button = ctk.CTkButton(email_frame, text="Generate Email", command=lambda: generated_email(),
                                    fg_color=colors["light_gray"], hover_color=colors["gray"],
                                    text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                    **{"width": 0, "height": 40})
        email_button.grid(row=6, column=0, pady=(5, 10), padx=10, sticky="we")

        email_frame = ctk.CTkFrame(email_frame, fg_color=colors["gray"])
        email_frame.grid(row=7, column=0, pady=10, padx=10, sticky="we")  

        text_generated_email = ctk.CTkLabel(email_frame, text="Email Generate..                                       ", 
                                            font=ctk.CTkFont(family="Helvetica", size=12), compound="left", wraplength=275)
        text_generated_email.grid(row=0, column=0, padx=10, pady=6, sticky="w")

        copy_email_button = ctk.CTkButton(email_frame, text="Copy", command=lambda: copy_to_clipboard(text_generated_email.cget("text")),
                                        fg_color=colors["light_gray"], hover_color=colors["gray"],
                                        text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                        **{"width": 0, "height": 30})
        copy_email_button.grid(row=0, column=1, padx=(10, 0), pady=6, sticky="e")



        right_frame = ctk.CTkFrame(display_right, width=312, height=376, fg_color=colors["light_background"])
        right_frame.grid(row=1, column=1, sticky="e", pady=(10, 0), padx=(0, 1))
        right_frame.grid_propagate(False)
        right_frame.grid_columnconfigure(0, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_man"]), size=(25, 25))
        title = ctk.CTkLabel(right_frame, text=" Identity Generator", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(16, 16), padx=0, sticky="ew")

        identity_button = ctk.CTkButton(right_frame, text="Generate Identity", command=lambda: generated_identity(),
                                        fg_color=colors["light_gray"], hover_color=colors["gray"],
                                        text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                        **{"width": 0, "height": 40})
        identity_button.grid(row=2, column=0, pady=(5, 10), padx=10, sticky="we")

        identity_frame = ctk.CTkFrame(right_frame, fg_color=colors["gray"])
        identity_frame.grid(row=3, column=0, pady=10, padx=10, sticky="we")  

        text_generated_identity = ctk.CTkLabel(identity_frame, text="Full Name:\nDate of Birth:\nAge:\nHeight:\nWeight:\nBlood Group:\nAddress:\nVehicle:\nJob:", 
                                        font=ctk.CTkFont(family="Helvetica", size=12), compound="left", wraplength=275)
        text_generated_identity.grid(row=0, column=0, padx=10, pady=6, sticky="w")


        copy_identity_button = ctk.CTkButton(right_frame, text="Copy", command=lambda: copy_to_clipboard(text_generated_identity.cget("text")),
                                            fg_color=colors["light_gray"], hover_color=colors["gray"],
                                            text_color=colors["white"], font=ctk.CTkFont(family="Helvetica", size=13),
                                            **{"width": 0, "height": 35})
        copy_identity_button.grid(row=4, column=0, pady=(10, 0), padx=80, sticky="we")

        loading = False

    def display_cleaning():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_clean"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Cleaning", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        cleaning_frame = ctk.CTkScrollableFrame(display_right, width=290, height=314, fg_color=colors["light_background"]) 
        cleaning_frame.grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0), padx=(10, 0))
        cleaning_frame.grid_columnconfigure(0, weight=1)
        cleaning_frame.grid_columnconfigure(1, weight=1)
        cleaning_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_file"]), size=(25, 25))
        title = ctk.CTkLabel(cleaning_frame, text=" Windows File", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        checkboxes_text_clean = [
            "Delete Temporary Files",
            "Delete Downloads Files",

            "Delete Windows Cache",
            "Delete Old Windows Updates",
            "Delete Windows Logs",
            "Delete Windows Error Report",
            "Delete Windows Web Cache",
            "Delete DirectX Shader Cache",

            "Clean Up Program Files",
            "Clean Up Document Files",
            "Clean Up Video Files",
            "Clean Up Music Files",
            "Clean Up Picture Files",
            "Clean Up Object 3d Files",

            "Clean Up Clipboard",
            "Clean Up Recycle Bin"
        ]
        checkboxes_clean = []
        selected_choices_clean = []

        def on_checkbox_change_clean(selected_text, var):
            if var.get():
                selected_choices_clean.append(selected_text)
            else:
                if selected_text in selected_choices_clean:
                    selected_choices_clean.remove(selected_text)

        for idx, text in enumerate(checkboxes_text_clean):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                cleaning_frame, 
                text=text, 
                variable=var, 
                command=lambda 
                selected_text=text, 
                var=var: on_checkbox_change_clean(selected_text, var), 
                text_color=colors["white"],
                fg_color=colors['light_light_gray'],
                hover_color=colors['light_light_gray'],
                border_color=colors['light_light_gray'],
                font=ctk.CTkFont(family="Helvetica", size=14)
            )
            checkbox.grid(row=idx + 1, column=0, sticky="w", pady=6, padx=2)
            checkboxes_clean.append(checkbox)

        def on_select_button_click_clean():
            run(lambda: Cleaner(selected_choices_clean))

        clean_image = ctk.CTkImage(light_image=Image.open(Img["logo_file"]), size=(22, 22))
        clean_button = ctk.CTkButton(display_right, text="Clean Selected", font=ctk.CTkFont(family="Helvetica", size=13,), 
                                            width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                            image=clean_image, command=on_select_button_click_clean)
        clean_button.grid(row=2, column=0, pady=10, padx=(10, 0), columnspan=3, sticky="w")


        uninstall_frame = ctk.CTkScrollableFrame(display_right, width=290, height=314, fg_color=colors["light_background"])
        uninstall_frame.grid(row=1, column=0, columnspan=3, sticky="e", pady=(10, 0), padx=(0, 10))
        uninstall_frame.grid_columnconfigure(0, weight=1)
        uninstall_frame.grid_columnconfigure(1, weight=1)
        uninstall_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_recyclebin"]), size=(25, 25))
        title = ctk.CTkLabel(uninstall_frame, text=" Windows Uninstall", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        checkboxes_text_uninstall = [
            "Uninstall One Drive",
            "Uninstall Cortana",
            "Uninstall Microsoft Edge",
            "Uninstall Xbox Game Bar",
            "Uninstall Skype",
            "Uninstall Microsoft Office",
            "Uninstall Windows Media Player",
            "Uninstall Mail and Calendar",
            "Uninstall Movies & TV",
            "Uninstall Photos",
            "Uninstall Weather",
            "Uninstall Maps",
        ]
        checkboxes_uninstall = []
        selected_choices_uninstall = []

        def on_checkbox_change_uninstall(selected_text, var):
            if var.get():
                selected_choices_uninstall.append(selected_text)
            else:
                if selected_text in selected_choices_uninstall:
                    selected_choices_uninstall.remove(selected_text)

        for idx, text in enumerate(checkboxes_text_uninstall):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                uninstall_frame, 
                text=text, 
                variable=var, 
                command=lambda 
                selected_text=text, 
                var=var: on_checkbox_change_uninstall(selected_text, var), 
                text_color=colors["white"],
                fg_color=colors['light_light_gray'],
                hover_color=colors['light_light_gray'],
                border_color=colors['light_light_gray'],
                font=ctk.CTkFont(family="Helvetica", size=14)
            )
            checkbox.grid(row=idx + 1, column=0, sticky="w", pady=6, padx=2)
            checkboxes_uninstall.append(checkbox)

        def on_select_button_click_uninstall():
            run(lambda: Cleaner(selected_choices_uninstall))

        uninstall_image = ctk.CTkImage(light_image=Image.open(Img["logo_recyclebin"]), size=(22, 22))
        uninstall_number = ctk.CTkButton(display_right, text="Uninstall Selected", font=ctk.CTkFont(family="Helvetica", size=13,), 
                                        width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                        image=uninstall_image, command=on_select_button_click_uninstall)
        uninstall_number.grid(row=2, column=0, pady=10, padx=(0, 10), columnspan=3, sticky="e")

        loading = False

    def display_browser():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)
        
        image = ctk.CTkImage(light_image=Image.open(Img["logo_browser"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Browser", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")
        
        def BrowserOptions(choice, browser_choose):
            if "Choose Browser" in browser_choose:
                Error_Console("Please choose a browser.")
                Error("Please choose a browser.")
                return
            if "Delete History" in choice:
                run(Delete_History, browser_choose)
            if "Delete Cookies" in choice:
                run(Delete_Cookies, browser_choose)
            if "Delete Login Data" in choice:
                run(Delete_Login_Data, browser_choose)
            if "Delete Cache" in choice:
                run(Delete_Cache, browser_choose)
            if "Delete Local Storage" in choice:
                run(Delete_Local_Storage, browser_choose)
            if "Delete Plugins" in choice:
                run(Delete_Plugins, browser_choose)
            Info("Everything that was selected has been deleted.")

        browser_frame = ctk.CTkScrollableFrame(display_right, width=290, height=314, fg_color=colors["light_background"]) 
        browser_frame.grid(row=1, column=0, columnspan=1, sticky="wn", pady=(10, 0), padx=(10, 0))
        browser_frame.grid_columnconfigure(0, weight=1)
        browser_frame.grid_columnconfigure(1, weight=1)
        browser_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_clean"]), size=(25, 25))
        title = ctk.CTkLabel(browser_frame, text=" Cleaning", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        checkboxes_text_browser = [
            "Delete History", "Delete Cookies", "Delete Login Data", "Delete Cache", "Delete Local Storage", "Delete Plugins",
        ]
        checkboxes_browser = []
        selected_choices_browser = []

        def on_checkbox_change_browser(selected_text, var):
            if var.get():
                selected_choices_browser.append(selected_text)
            else:
                if selected_text in selected_choices_browser:
                    selected_choices_browser.remove(selected_text)

        for idx, text in enumerate(checkboxes_text_browser):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                browser_frame, 
                text=text, 
                variable=var, 
                command=lambda 
                selected_text=text, 
                var=var: on_checkbox_change_browser(selected_text, var), 
                text_color=colors["white"],
                fg_color=colors['light_light_gray'],
                hover_color=colors['light_light_gray'],
                border_color=colors['light_light_gray'],
                font=ctk.CTkFont(family="Helvetica", size=14)
            ).grid(row=idx + 1, column=0, sticky="w", pady=6, padx=2)

            checkboxes_browser.append(checkbox)
        
        choose_browser = ctk.CTkOptionMenu(
            master=browser_frame,
            values=list(browsers_paths.keys()),
            text_color=colors["white"],
            fg_color=colors['light_gray'],
            button_color=colors["gray"],
            button_hover_color=colors['light_light_gray'],
            font=ctk.CTkFont(size=13),
        )
        choose_browser.grid(row=20, column=0, sticky="e", pady=10)
        choose_browser.set("Choose Browser")

        def on_select_button_click_browser():
            run(lambda: BrowserOptions(selected_choices_browser, choose_browser.get()))

        browser_image = ctk.CTkImage(light_image=Image.open(Img["logo_clean"]), size=(22, 22))
        browser_button = ctk.CTkButton(display_right, text="Clean Selected", font=ctk.CTkFont(family="Helvetica", size=13,), 
                                            width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                            image=browser_image, command=on_select_button_click_browser)
        browser_button.grid(row=1, column=0, pady=(0,1), padx=(10, 0), columnspan=3, sticky="ws")

        def EnableIpv6Protocol():
            Ipv6Protocol("enable")
        
        def DisableIpv6Protocol():
            Ipv6Protocol("disable")

        def EnableNetworkInterface():
            Network_Interface("enable")
        
        def DisableNetworkInterface():
            Network_Interface("disable")

        settings_frame = ctk.CTkScrollableFrame(display_right, width=290, height=365, fg_color=colors["light_background"])
        settings_frame.grid(row=1, column=1, columnspan=3, sticky="e", pady=(10, 0), padx=(0, 10))
        settings_frame.grid_columnconfigure(0, weight=1)
        settings_frame.grid_columnconfigure(1, weight=1)
        settings_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_network"]), size=(25, 25))
        title = ctk.CTkLabel(settings_frame, text=" Network", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        dns_image = ctk.CTkImage(light_image=Image.open(Img["logo_dns"]), size=(25, 25))
        button = ctk.CTkButton(settings_frame, text="Delete Dns Cache", font=ctk.CTkFont(family="Helvetica", size=14), 
                                width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                image=dns_image, command=DnsCache_Delete)
        button.grid(row=1, column=0, pady=(0, 5), padx=10, columnspan=3, sticky="we")

        image = ctk.CTkImage(light_image=Image.open(Img["logo_dns"]), size=(25, 25))
        button = ctk.CTkButton(settings_frame, text="Delete Arp Cache", font=ctk.CTkFont(family="Helvetica", size=14), 
                                width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                image=image, command=Flush_Arp_Cache)
        button.grid(row=2, column=0, pady=5, padx=10, columnspan=3, sticky="we")

        netowrk_image = ctk.CTkImage(light_image=Image.open(Img["logo_network"]), size=(25, 25))
        button = ctk.CTkButton(settings_frame, text="Reset Network", font=ctk.CTkFont(family="Helvetica", size=14), 
                                width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                image=netowrk_image, command=Network_Reset)
        button.grid(row=3, column=0, pady=5, padx=10, columnspan=3, sticky="we")

        settings_vars = {}

        settingss = [
            ("Disable Ipv6 Protocol", lambda: run(EnableIpv6Protocol) if not settings_ipv6_protocol.get() else run(DisableIpv6Protocol)),
            ("Disable Network Interface", lambda: run(EnableNetworkInterface) if not settings_network_interface.get() else run(DisableNetworkInterface)),
        ]

        for idx, (text, command) in enumerate(settingss):
            settings_var = ctk.BooleanVar(value=False)
            settings_vars[text] = settings_var

            if text == 'Disable Ipv6 Protocol':
                state_now = Ipv6Protocol()
                settings_ipv6_protocol = ctk.BooleanVar(value=state_now is not None and state_now == True)
                settings_var = settings_ipv6_protocol

            elif text == 'Disable Network Interface':
                state_now = Network_Interface()
                settings_network_interface = ctk.BooleanVar(value=state_now is not None and state_now == True)
                settings_var = settings_network_interface

            switch = ctk.CTkSwitch(
                settings_frame,
                text=text,
                command=command,
                variable=settings_var,
                onvalue=True,
                offvalue=False,
                text_color=colors["white"],
                fg_color=colors['light_gray'],
                button_color=colors["white"],
                progress_color=colors["light_light_gray"],
                font=ctk.CTkFont(family="Helvetica", size=14),
            )

            switch.grid(row=idx + 10, column=0, padx=2, pady=6, sticky="w")
        
        loading = False

    def display_protection():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        def DisableMicrophone():
            Microphone("disable")

        def EnableMicrophone():
            Microphone("enable")

        def DisableWebcam():
            Webcam("disable")

        def EnableWebcam():
            Webcam("enable")

        def DisableLocation():
            Location("disable")

        def EnableLocation():
            Location("enable")

        def DisableEmail():
            Email("disable")

        def EnableEmail():
            Email("enable")

        def DisableContacts():
            Contacts("disable")

        def EnableContacts():
            Contacts("enable")

        def DisableChat():
            Chat("disable")

        def EnableChat():
            Chat("enable")

        def DisablePhoneCall():
            PhoneCall("disable")

        def EnablePhoneCall():
            PhoneCall("enable")

        def DisablePhoneCallHistory():
            PhoneCallHistory("disable")

        def EnablePhoneCallHistory():
            PhoneCallHistory("enable")

        def DisableActivity():
            Activity("disable")

        def EnableActivity():
            Activity("enable")

        def DisableAppDiagnostics():
            AppDiagnostics("disable")

        def EnableAppDiagnostics():
            AppDiagnostics("enable")

        def DisableAppointments():
            Appointments("disable")

        def EnableAppointments():
            Appointments("enable")

        def DisableBluetooth():
            Bluetooth("disable")

        def EnableBluetooth():
            Bluetooth("enable")

        def DisableBluetoothSync():
            BluetoothSync("disable")

        def EnableBluetoothSync():
            BluetoothSync("enable")

        def DisableBroadFileSystemAccess():
            BroadFileSystemAccess("disable")

        def EnableBroadFileSystemAccess():
            BroadFileSystemAccess("enable")

        def DisableCellularData():
            CellularData("disable")

        def EnableCellularData():
            CellularData("enable")

        def DisableDocumentsLibrary():
            DocumentsLibrary("disable")

        def EnableDocumentsLibrary():
            DocumentsLibrary("enable")

        def DisableGazeInput():
            GazeInput("disable")

        def EnableGazeInput():
            GazeInput("enable")

        def DisableHumanInterfaceDevice():
            HumanInterfaceDevice("disable")

        def EnableHumanInterfaceDevice():
            HumanInterfaceDevice("enable")

        def DisablePicturesLibrary():
            PicturesLibrary("disable")

        def EnablePicturesLibrary():
            PicturesLibrary("enable")

        def DisableRadios():
            Radios("disable")

        def EnableRadios():
            Radios("enable")

        def DisableSensorsCustom():
            SensorsCustom("disable")

        def EnableSensorsCustom():
            SensorsCustom("enable")

        def DisableSerialCommunication():
            SerialCommunication("disable")

        def EnableSerialCommunication():
            SerialCommunication("enable")

        def DisableUSB():
            USB("disable")

        def EnableUSB():
            USB("enable")

        def DisableUserAccountInformation():
            UserAccountInformation("disable")

        def EnableUserAccountInformation():
            UserAccountInformation("enable")

        def DisableUserDataTasks():
            UserDataTasks("disable")

        def EnableUserDataTasks():
            UserDataTasks("enable")

        def DisableUserNotificationListener():
            UserNotificationListener("disable")

        def EnableUserNotificationListener():
            UserNotificationListener("enable")

        def DisableVideosLibrary():
            VideosLibrary("disable")

        def EnableVideosLibrary():
            VideosLibrary("enable")

        def DisableWiFiData():
            WiFiData("disable")

        def EnableWiFiData():
            WiFiData("enable")

        def DisableWiFiDirect():
            WiFiDirect("disable")

        def EnableWiFiDirect():
            WiFiDirect("enable")

        image = ctk.CTkImage(light_image=Image.open(Img["logo_protection"]), size=(40, 40))
        title = ctk.CTkLabel(display_right, text=" Windows Protection", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(60, 10), padx=(0, 20), sticky="we")

        synchronization_frame = ctk.CTkScrollableFrame(display_right, width=290, height=365, fg_color=colors["light_background"])
        synchronization_frame.grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0), padx=(10, 0))
        synchronization_frame.grid_columnconfigure(0, weight=1)
        synchronization_frame.grid_columnconfigure(1, weight=1)
        synchronization_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_synchronization"]), size=(25, 25))
        title = ctk.CTkLabel(synchronization_frame, text=" App Synchronization", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")
 
        synchronizations = [
            ("Disable Microphone", lambda: run(DisableMicrophone) if synchronization_microphone.get() else run(EnableMicrophone)),
            ("Disable Webcam", lambda: run(DisableWebcam) if synchronization_webcam.get() else run(EnableWebcam)),
            ("Disable Location", lambda: run(DisableLocation) if synchronization_location.get() else run(EnableLocation)),
            ("Disable Email", lambda: run(DisableEmail) if synchronization_email.get() else run(EnableEmail)),
            ("Disable Contacts", lambda: run(DisableContacts) if synchronization_contacts.get() else run(EnableContacts)),
            ("Disable Chat", lambda: run(DisableChat) if synchronization_chat.get() else run(EnableChat)),
            ("Disable Phone Call", lambda: run(DisablePhoneCall) if synchronization_phone_call.get() else run(EnablePhoneCall)),
            ("Disable Phone Call History", lambda: run(DisablePhoneCallHistory) if synchronization_phone_call_history.get() else run(EnablePhoneCallHistory)),
            ("Disable Activity", lambda: run(DisableActivity) if synchronization_activity.get() else run(EnableActivity)),
            ("Disable App Diagnostics", lambda: run(DisableAppDiagnostics) if synchronization_app_diagnostics.get() else run(EnableAppDiagnostics)),
            ("Disable Appointments", lambda: run(DisableAppointments) if synchronization_appointments.get() else run(EnableAppointments)),
            ("Disable Bluetooth", lambda: run(DisableBluetooth) if synchronization_bluetooth.get() else run(EnableBluetooth)),
            ("Disable Bluetooth Sync", lambda: run(DisableBluetoothSync) if synchronization_bluetooth_sync.get() else run(EnableBluetoothSync)),
            ("Disable Broad File System Access", lambda: run(DisableBroadFileSystemAccess) if synchronization_broad_file_system_access.get() else run(EnableBroadFileSystemAccess)),
            ("Disable Cellular Data", lambda: run(DisableCellularData) if synchronization_cellular_data.get() else run(EnableCellularData)),
            ("Disable Documents Library", lambda: run(DisableDocumentsLibrary) if synchronization_documents_library.get() else run(EnableDocumentsLibrary)),
            ("Disable Gaze Input", lambda: run(DisableGazeInput) if synchronization_gaze_input.get() else run(EnableGazeInput)),
            ("Disable Human Interface Device", lambda: run(DisableHumanInterfaceDevice) if synchronization_human_interface_device.get() else run(EnableHumanInterfaceDevice)),
            ("Disable Pictures Library", lambda: run(DisablePicturesLibrary) if synchronization_pictures_library.get() else run(EnablePicturesLibrary)),
            ("Disable Radios", lambda: run(DisableRadios) if synchronization_radios.get() else run(EnableRadios)),
            ("Disable Sensors Custom", lambda: run(DisableSensorsCustom) if synchronization_sensors_custom.get() else run(EnableSensorsCustom)),
            ("Disable Serial Communication", lambda: run(DisableSerialCommunication) if synchronization_serial_communication.get() else run(EnableSerialCommunication)),
            ("Disable USB", lambda: run(DisableUSB) if synchronization_usb.get() else run(EnableUSB)),
            ("Disable User Account Information", lambda: run(DisableUserAccountInformation) if synchronization_user_account_information.get() else run(EnableUserAccountInformation)),
            ("Disable User Data Tasks", lambda: run(DisableUserDataTasks) if synchronization_user_data_tasks.get() else run(EnableUserDataTasks)),
            ("Disable User Notification Listener", lambda: run(DisableUserNotificationListener) if synchronization_user_notification_listener.get() else run(EnableUserNotificationListener)),
            ("Disable Videos Library", lambda: run(DisableVideosLibrary) if synchronization_videos_library.get() else run(EnableVideosLibrary)),
            ("Disable Wi-Fi Data", lambda: run(DisableWiFiData) if synchronization_wifi_data.get() else run(EnableWiFiData)),
            ("Disable Wi-Fi Direct", lambda: run(DisableWiFiDirect) if synchronization_wifi_direct.get() else run(EnableWiFiDirect)),
        ]

        for idx, (text, command) in enumerate(synchronizations):
            if text == 'Disable Microphone':
                synchronization_var = ctk.BooleanVar(value=Microphone() != 'Allow')
                synchronization_microphone = synchronization_var
            elif text == 'Disable Webcam':
                synchronization_var = ctk.BooleanVar(value=WebCam() != 'Allow')
                synchronization_webcam = synchronization_var
            elif text == 'Disable Location':
                synchronization_var = ctk.BooleanVar(value=Location() != 'Allow')
                synchronization_location = synchronization_var
            elif text == 'Disable Email':
                synchronization_var = ctk.BooleanVar(value=Email() != 'Allow')
                synchronization_email = synchronization_var
            elif text == 'Disable Contacts':
                synchronization_var = ctk.BooleanVar(value=Contacts() != 'Allow')
                synchronization_contacts = synchronization_var
            elif text == 'Disable Chat':
                synchronization_var = ctk.BooleanVar(value=Chat() != 'Allow')
                synchronization_chat = synchronization_var
            elif text == 'Disable Phone Call':
                synchronization_var = ctk.BooleanVar(value=PhoneCall() != 'Allow')
                synchronization_phone_call = synchronization_var
            elif text == 'Disable Phone Call History':
                synchronization_var = ctk.BooleanVar(value=PhoneCallHistory() != 'Allow')
                synchronization_phone_call_history = synchronization_var
            elif text == 'Disable Activity':
                synchronization_var = ctk.BooleanVar(value=Activity() != 'Allow')
                synchronization_activity = synchronization_var
            elif text == 'Disable App Diagnostics':
                synchronization_var = ctk.BooleanVar(value=AppDiagnostics() != 'Allow')
                synchronization_app_diagnostics = synchronization_var
            elif text == 'Disable Appointments':
                synchronization_var = ctk.BooleanVar(value=Appointments() != 'Allow')
                synchronization_appointments = synchronization_var
            elif text == 'Disable Bluetooth':
                synchronization_var = ctk.BooleanVar(value=Bluetooth() != 'Allow')
                synchronization_bluetooth = synchronization_var
            elif text == 'Disable Bluetooth Sync':
                synchronization_var = ctk.BooleanVar(value=BluetoothSync() != 'Allow')
                synchronization_bluetooth_sync = synchronization_var
            elif text == 'Disable Broad File System Access':
                synchronization_var = ctk.BooleanVar(value=BroadFileSystemAccess() != 'Allow')
                synchronization_broad_file_system_access = synchronization_var
            elif text == 'Disable Cellular Data':
                synchronization_var = ctk.BooleanVar(value=CellularData() != 'Allow')
                synchronization_cellular_data = synchronization_var
            elif text == 'Disable Documents Library':
                synchronization_var = ctk.BooleanVar(value=DocumentsLibrary() != 'Allow')
                synchronization_documents_library = synchronization_var
            elif text == 'Disable Gaze Input':
                synchronization_var = ctk.BooleanVar(value=GazeInput() != 'Allow')
                synchronization_gaze_input = synchronization_var
            elif text == 'Disable Human Interface Device':
                synchronization_var = ctk.BooleanVar(value=HumanInterfaceDevice() != 'Allow')
                synchronization_human_interface_device = synchronization_var
            elif text == 'Disable Pictures Library':
                synchronization_var = ctk.BooleanVar(value=PicturesLibrary() != 'Allow')
                synchronization_pictures_library = synchronization_var
            elif text == 'Disable Radios':
                synchronization_var = ctk.BooleanVar(value=Radios() != 'Allow')
                synchronization_radios = synchronization_var
            elif text == 'Disable Sensors Custom':
                synchronization_var = ctk.BooleanVar(value=SensorsCustom() != 'Allow')
                synchronization_sensors_custom = synchronization_var
            elif text == 'Disable Serial Communication':
                synchronization_var = ctk.BooleanVar(value=SerialCommunication() != 'Allow')
                synchronization_serial_communication = synchronization_var
            elif text == 'Disable USB':
                synchronization_var = ctk.BooleanVar(value=USB() != 'Allow')
                synchronization_usb = synchronization_var
            elif text == 'Disable User Account Information':
                synchronization_var = ctk.BooleanVar(value=UserAccountInformation() != 'Allow')
                synchronization_user_account_information = synchronization_var
            elif text == 'Disable User Data Tasks':
                synchronization_var = ctk.BooleanVar(value=UserDataTasks() != 'Allow')
                synchronization_user_data_tasks = synchronization_var
            elif text == 'Disable User Notification Listener':
                synchronization_var = ctk.BooleanVar(value=UserNotificationListener() != 'Allow')
                synchronization_user_notification_listener = synchronization_var
            elif text == 'Disable Videos Library':
                synchronization_var = ctk.BooleanVar(value=VideosLibrary() != 'Allow')
                synchronization_videos_library = synchronization_var
            elif text == 'Disable Wi-Fi Data':
                synchronization_var = ctk.BooleanVar(value=WiFiData() != 'Allow')
                synchronization_wifi_data = synchronization_var
            elif text == 'Disable Wi-Fi Direct':
                synchronization_var = ctk.BooleanVar(value=WiFiDirect() != 'Allow')
                synchronization_wifi_direct = synchronization_var
            else:
                synchronization_var = ctk.BooleanVar(value=False)

            switch = ctk.CTkSwitch(
                synchronization_frame,
                text=text,
                command=command,
                variable=synchronization_var,
                onvalue=True,
                offvalue=False,
                text_color=colors["white"],
                fg_color=colors['light_gray'],
                button_color=colors["white"],
                progress_color=colors["light_light_gray"],
                font=ctk.CTkFont(family="Helvetica", size=14),
            )
            
            switch.grid(row=idx + 1, column=0, padx=2, pady=6, sticky="w")

        def UnblockWebsite():
            Unblock_Website()
            
        def DeleteDiscordInjection():
            Delete_Discord_Injection()

        def DisableRealTimeProtection():
            RealTimeProtection("disable")

        def EnableRealTimeProtection():
            RealTimeProtection("enable")

        def DisableWindowsFirewall():
            WindowsFirewall("disable")

        def EnableWindowsFirewall():
            WindowsFirewall("enable")

        def DisableCloudProtection():
            CloudProtection("disable")

        def EnableCloudProtection():
            CloudProtection("enable")

        def DisableSampleSubmission():
            SampleSubmission("disable")

        def EnableSampleSubmission():
            SampleSubmission("enable")

        def DisableDeviceSecurity():
            DeviceSecurity("disable")

        def EnableDeviceSecurity():
            DeviceSecurity("enable")

        def DisableZeroDayProtection():
            ZeroDayProtection("disable")

        def EnableZeroDayProtection():
            ZeroDayProtection("enable")

        def DisableAppAndBrowserControl():
            AppAndBrowserControl("disable")

        def EnableAppAndBrowserControl():
            AppAndBrowserControl("enable")

        def DisableMemoryIntegrity():
            MemoryIntegrity("disable")

        def EnableMemoryIntegrity():
            MemoryIntegrity("enable")

        def DisableUserAccountControl():
            UserAccountControl("disable")

        def EnableUserAccountControl():
            UserAccountControl("enable")

        defense_frame = ctk.CTkScrollableFrame(display_right, width=290, height=365, fg_color=colors["light_background"])
        defense_frame.grid(row=1, column=0, columnspan=3, sticky="e", pady=(10, 0), padx=(0, 10))
        defense_frame.grid_columnconfigure(0, weight=1)
        defense_frame.grid_columnconfigure(1, weight=1)
        defense_frame.grid_columnconfigure(2, weight=1)

        image = ctk.CTkImage(light_image=Image.open(Img["logo_protection"]), size=(25, 25))
        title = ctk.CTkLabel(defense_frame, text=" Defense", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), image=image, compound="left")
        title.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=0, sticky="ew")

        website_image = ctk.CTkImage(light_image=Image.open(Img["logo_internet"]), size=(25, 25))
        discord_image = ctk.CTkImage(light_image=Image.open(Img["logo_discord"]), size=(25, 25))

        button = ctk.CTkButton(defense_frame, text="Unblock All Website", font=ctk.CTkFont(family="Helvetica", size=14), 
                                width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                image=website_image, command=UnblockWebsite)
        button.grid(row=1, column=0, pady=5, padx=10, columnspan=3, sticky="we")

        button = ctk.CTkButton(defense_frame, text="Delete Discord Injection", font=ctk.CTkFont(family="Helvetica", size=14), 
                                width=312, height=40, fg_color=colors["light_gray"], hover_color=colors["gray"], 
                                image=discord_image, command=DeleteDiscordInjection)
        button.grid(row=2, column=0, pady=5, padx=10, columnspan=3, sticky="we")

        defense_vars = {}

        defenses = [
            ("Enable Real Time Protection", lambda: run(DisableRealTimeProtection) if not defense_real_time_protection.get() else run(EnableRealTimeProtection)),
            ("Enable Windows Firewall", lambda: run(DisableWindowsFirewall) if not defense_windows_firewall.get() else run(EnableWindowsFirewall)),
            ("Enable Cloud Protection", lambda: run(DisableCloudProtection) if not defense_cloud_protection.get() else run(EnableCloudProtection)),
            ("Enable Sample Submission", lambda: run(DisableSampleSubmission) if not defense_sample_submission.get() else run(EnableSampleSubmission)),
            ("Enable Device Security", lambda: run(DisableDeviceSecurity) if not defense_device_security.get() else run(EnableDeviceSecurity)),
            ("Enable Zero Day Protection", lambda: run(DisableZeroDayProtection) if not defense_zero_day_protection.get() else run(EnableZeroDayProtection)),
            ("Enable App and Browser Control", lambda: run(DisableAppAndBrowserControl) if not defense_app_and_browser_control.get() else run(EnableAppAndBrowserControl)),
            ("Enable Memory Integrity", lambda: run(DisableMemoryIntegrity) if not defense_memory_integrity.get() else run(EnableMemoryIntegrity)),
            ("Enable User Account Control", lambda: run(DisableUserAccountControl) if not defense_user_account_control.get() else run(EnableUserAccountControl)),
        ]

        for idx, (text, command) in enumerate(defenses):
            defense_var = ctk.BooleanVar(value=False)
            defense_vars[text] = defense_var

            if text == 'Enable Real Time Protection':
                state_now = RealTimeProtection()
                defense_real_time_protection = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_real_time_protection
            elif text == 'Enable Windows Firewall':
                state_now = WindowsFirewall()
                defense_windows_firewall = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_windows_firewall
            elif text == 'Enable Cloud Protection':
                state_now = CloudProtection()
                defense_cloud_protection = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_cloud_protection
            elif text == 'Enable Sample Submission':
                state_now = SampleSubmission()
                defense_sample_submission = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_sample_submission
            elif text == 'Enable Device Security':
                state_now = DeviceSecurity()
                defense_device_security = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_device_security
            elif text == 'Enable Zero Day Protection':
                state_now = ZeroDayProtection()
                defense_zero_day_protection = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_zero_day_protection
            elif text == 'Enable App and Browser Control':
                state_now = AppAndBrowserControl()
                defense_app_and_browser_control = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_app_and_browser_control
            elif text == 'Enable Memory Integrity':
                state_now = MemoryIntegrity()
                defense_memory_integrity = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_memory_integrity
            elif text == 'Enable User Account Control':
                state_now = UserAccountControl()
                defense_user_account_control = ctk.BooleanVar(value=state_now is not None and state_now == True)
                defense_var = defense_user_account_control

            switch = ctk.CTkSwitch(
                defense_frame,
                text=text,
                command=command,
                variable=defense_var,
                onvalue=True,
                offvalue=False,
                text_color=colors["white"],
                fg_color=colors['light_gray'],
                button_color=colors["white"],
                progress_color=colors["light_light_gray"],
                font=ctk.CTkFont(family="Helvetica", size=14),
            )

            switch.grid(row=idx + 3, column=0, padx=2, pady=6, sticky="w")

        loading = False

    def display_home():
        global loading
        loading = True

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        def Telegram():
            webbrowser.open("https://" + telegram)
        def Discord():
            webbrowser.open("https://" + discord)
        def Github():
            webbrowser.open("https://" + github)
        

        image_path = ctk.CTkImage(light_image=Image.open(Img["banner_oblivion"]), size=(660, 220))
        image_banner = ctk.CTkLabel(display_right, image=image_path, text='')
        image_banner.grid(row=0, column=0, columnspan=3, sticky="we", pady=0)

        title = ctk.CTkLabel(display_right, text="Oblivion Anonimizer", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"))
        title.grid(row=1, column=0, columnspan=3, pady=0, padx=(0, 20), sticky="we")
        by_text = ctk.CTkLabel(display_right, text=f"By {by}", font=ctk.CTkFont(family="Helvetica", size=15))
        by_text.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=(0, 20), sticky="we")

        container_frame = ctk.CTkFrame(display_right, fg_color=colors["light_background"]) 
        container_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10), padx=(170, 190), sticky="we")  

        container_frame.grid_columnconfigure(0, weight=1)
        container_frame.grid_rowconfigure(0, weight=1)

        key_image = ctk.CTkImage(light_image=Image.open(Img["logo_hello"]), size=(21, 21))
        time_image = ctk.CTkImage(light_image=Image.open(Img["logo_star"]), size=(22, 22))

        key_text = ctk.CTkLabel(container_frame, text=f" Welcome on Oblivion", font=ctk.CTkFont(family="Helvetica", size=13), image=key_image, compound="left", text_color="white")
        key_text.grid(row=3, column=0, pady=(10, 4), padx=(0, 20), sticky="we") 

        time_text = ctk.CTkLabel(container_frame, text=f" Please star the repoo !", font=ctk.CTkFont(family="Helvetica", size=13), image=time_image, compound="left", text_color="white")
        time_text.grid(row=4, column=0, pady=(4, 10), padx=(0, 20), sticky="we")

        telegram_image = ctk.CTkImage(light_image=Image.open(Img["logo_telegram"]), size=(25, 25))
        website_image = ctk.CTkImage(light_image=Image.open(Img["logo_internet"]), size=(25, 25))
        github_image = ctk.CTkImage(light_image=Image.open(Img["logo_github"]), size=(25, 25))

        def DisableStartup():
            Startup("disable")
            Info("Startup Disable.")
        def EnableStartup():
            Startup("enable")
            Info("Startup Enabled.")

        switch = [
            ("Launch the software at startup", lambda: run(EnableStartup) if synchronization_microphone.get() == True else run(DisableStartup)),
        ]

        for index, (text, command) in enumerate(switch):
            row = 5 + (index // 3)
            col = index % 3

            if text == 'Launch the software at startup':
                if Startup() == False:
                    synchronization_var = ctk.BooleanVar(value=False)
                else:
                    synchronization_var = ctk.BooleanVar(value=True)
            else:
                synchronization_var = ctk.BooleanVar(value=False)

            switch = ctk.CTkSwitch(
                display_right,
                text=text,
                command=command,
                variable=synchronization_var,
                onvalue=True,
                offvalue=False,
                text_color=colors["white"],
                fg_color=colors['light_gray'],
                button_color=colors["white"],
                progress_color=colors["light_light_gray"],
                font=ctk.CTkFont(family="Helvetica", size=14),
            )

            if text == "Launch the software at startup":
                synchronization_microphone = switch

            switch.grid(row=row, column=0, columnspan=3, sticky="we", padx=(22, 0), pady=(13, 13))

        buttons = [
            ("Telegram", telegram_image, lambda: run(Telegram)),
            ("Github", github_image, lambda: run(Github)),
            ("Discord", website_image, lambda: run(Discord)),
        ]

        for index, (text, image, command) in enumerate(buttons):
            row = 11 + (index // 3)
            col = index % 3
            button = ctk.CTkButton(
                display_right,
                text=text,
                image=image,
                compound="left",
                command=command,
                fg_color=colors["light_gray"],
                hover_color=colors["gray"],
                text_color=colors["white"],
                font=ctk.CTkFont(family="Helvetica", size=14),
                **{
                    "width": 10, 
                    "height": 40,
                }
            )
            button.grid(row=row, column=col, padx=20, pady=10, sticky="ew")

        loading = False
        
# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px


    # <<<<<<<<<< SETTINGS >>>>>>>>>> 
    if "a" == "a":
        ctk.set_appearance_mode("dark")
        root = ctk.CTk()
        root.title(title)
        root.geometry("820x508")
        root.resizable(False, False)
        try: root.iconphoto(True, ImageTk.PhotoImage(Image.open(Img["logo_Oblivion_Anonimizer"])))
        except: pass
        try: root.iconbitmap(Img["icon_Oblivion_Anonimizer"])
        except: pass
    else:
        sys.exit(-1)
        raise SystemExit

    # <<<<<<<<<< NAVIGATION >>>>>>>>>> 
    sidebar_frame = ctk.CTkFrame(root, width=180, corner_radius=0, fg_color=colors["background"])
    sidebar_frame.grid(row=0, column=0, sticky="ns")

    # <<<<<<<<<< TITLE NAVIGATION >>>>>>>>>> 
    image = ctk.CTkImage(light_image=Image.open(Img["logo_Oblivion_Anonimizer"]), size=(27, 27))
    sidebar_label = ctk.CTkLabel(sidebar_frame, text=f" Oblivion v{version}", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), image=image, compound="left")
    sidebar_label.pack(pady=(15,15))

    # <<<<<<<<<< BUTTON NAVIGATION >>>>>>>>>> 
    button_style = {
        "fg_color": colors["background"],
        "hover_color": colors["light_gray"],
        "text_color": colors["white"],
        "font": ctk.CTkFont(family="Helvetica", size=14),
        "width": 160, 
        "height": 50,
        "anchor": "w"
    }

    button_style_active = {
        "fg_color": colors["light_gray"],
        "hover_color": colors["light_gray"],
        "text_color": colors["white"],
        "font": ctk.CTkFont(family="Helvetica", size=14),
        "width": 160, 
        "height": 50,
        "anchor": "w"
    }

    home_image = ctk.CTkImage(light_image=Image.open(Img["logo_home"]), size=(25, 25))
    monitoring_image = ctk.CTkImage(light_image=Image.open(Img["logo_monitoring"]), size=(25, 25))
    pc_info_image = ctk.CTkImage(light_image=Image.open(Img["logo_glass"]), size=(25, 25))
    spoofer_image = ctk.CTkImage(light_image=Image.open(Img["logo_spoofer"]), size=(25, 25))
    folder_image = ctk.CTkImage(light_image=Image.open(Img["logo_folder_encrypted"]), size=(25, 25))
    cleaning_image = ctk.CTkImage(light_image=Image.open(Img["logo_clean"]), size=(25, 25))
    browser_image = ctk.CTkImage(light_image=Image.open(Img["logo_browser"]), size=(25, 25))
    data_image = ctk.CTkImage(light_image=Image.open(Img["logo_data"]), size=(25, 25))
    protection_image = ctk.CTkImage(light_image=Image.open(Img["logo_protection"]), size=(25, 25))
    
    home_button = ctk.CTkButton(
        sidebar_frame, 
        text="Home", 
        image=home_image, 
        command=lambda: show_section("home"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    home_button.pack(fill="x", padx=0, pady=0)

    monitoring_button = ctk.CTkButton(
        sidebar_frame, 
        text="Monitoring", 
        image=monitoring_image, 
        command=lambda: show_section("monitoring"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    monitoring_button.pack(fill="x", padx=0, pady=0)

    protection_button = ctk.CTkButton(
        sidebar_frame, 
        text="Protection", 
        image=protection_image, 
        command=lambda: show_section("protection"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    protection_button.pack(fill="x", padx=0, pady=0)

    folder_button = ctk.CTkButton(
        sidebar_frame, 
        text="Folder", 
        image=folder_image, 
        command=lambda: show_section("folder"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    folder_button.pack(fill="x", padx=0, pady=0)

    spoofer_button = ctk.CTkButton(
        sidebar_frame, 
        text="Spoofer", 
        image=spoofer_image, 
        command=lambda: show_section("spoofer"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    spoofer_button.pack(fill="x", padx=0, pady=0)

    cleaning_button = ctk.CTkButton(
        sidebar_frame, 
        text="Cleaning", 
        image=cleaning_image, 
        command=lambda: show_section("cleaning"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    cleaning_button.pack(fill="x", padx=0, pady=0)

    browser_button = ctk.CTkButton(
        sidebar_frame, 
        text="Browser", 
        image=browser_image, 
        command=lambda: show_section("browser"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    browser_button.pack(fill="x", padx=0, pady=0)

    data_button = ctk.CTkButton(
        sidebar_frame, 
        text="Data", 
        image=data_image, 
        command=lambda: show_section("data"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    data_button.pack(fill="x", padx=0, pady=0)
    
    pc_info_button = ctk.CTkButton(
        sidebar_frame, 
        text="Information", 
        image=pc_info_image, 
        command=lambda: show_section("pc_info"), 
        compound="left",
        corner_radius=0,
        **button_style
    )
    pc_info_button.pack(fill="x", padx=0, pady=0)

    display_right = ctk.CTkFrame(root, fg_color=colors["background"])
    display_right.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    border_frame = ctk.CTkFrame(root, width=2, corner_radius=0, fg_color=colors["gray"])
    border_frame.grid(row=0, column=1, sticky="wsn")

    def show_section(section):
        global loading

        if loading:
            return

        for widget in display_right.winfo_children():
            widget.destroy()

        display_right.grid_columnconfigure(0, weight=1)
        display_right.grid_columnconfigure(1, weight=1)
        display_right.grid_columnconfigure(2, weight=1)

        buttons = {
            "home": home_button,
            "monitoring": monitoring_button,
            "protection": protection_button,
            "folder": folder_button,
            "spoofer": spoofer_button,
            "cleaning": cleaning_button,
            "browser": browser_button,
            "data": data_button,
            "pc_info": pc_info_button,
        }

        for section_name, button in buttons.items():
            if section_name == section:
                button.configure(**button_style_active)
            else:
                button.configure(**button_style)

        if section == "home":
            display_home()
        elif section == "monitoring":
            display_monitoring()
        elif section == "protection":
            threading.Thread(target=display_protection, daemon=True).start()
        elif section == "folder":
            display_folder()
        elif section == "spoofer":
            display_spoofer()
        elif section == "cleaning":
            display_cleaning()
        elif section == "browser":
            display_browser()
        elif section == "data":
            display_data()
        elif section == "pc_info":
            display_pc_info()

    if "a" == "a":
        show_section("home")
        root.mainloop()
    else: return

def Start():
    global loading
    loading = False
    Software()
    sys.exit(-1)
    raise SystemExit

try: Start()
except Exception as e: Error_Console(e)


# Oblivion Anonimizer
# Dev by 124P
# https://github.com/124Px
