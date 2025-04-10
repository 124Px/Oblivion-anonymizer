# Oblivion Anonymizer

<img src="https://raw.githubusercontent.com/124Px/Oblivion-anonymizer/refs/heads/main/Oblivion/Oblivion_Anonimizer/img/banner_oblivion.png" width="500" />

## Overview
**Oblivion Anonymizer** is an advanced privacy tool designed to enhance anonymity on Windows-based systems. This program provides users with multiple features to obfuscate system information, clean up traces, spoof hardware identifiers, and secure personal data. It is a comprehensive solution for users seeking greater control over their digital footprint. 🛡️

## Features
Oblivion Anonymizer includes a wide array of functionalities grouped into different categories:

### 1. Monitoring 📊
This category includes features to retrieve system information such as:
- **Machine GUID, Hardware IDs, and Serial Numbers**
- **BIOS Information (Release Date, Version, System SKU, Manufacturer, etc.)**
- **Processor and Motherboard Serial Numbers**
- **Network and Internet Information (Hostname, OS Version, IP, etc.)**

### 2. Protection 🔒
This module provides security enhancements by allowing users to:
- **Disable Windows telemetry and tracking services**
- **Remove pre-installed Windows applications**
- **Modify system permissions to restrict unauthorized access**

### 3. Cleaning 🧹
The cleaning functionality ensures that sensitive user data is wiped from the system:
- **Delete temporary files, logs, and caches**
- **Clear browser history, cookies, and saved credentials**
- **Remove duplicate and hidden files**
- **Wipe clipboard data and empty the recycle bin**

### 4. Folder Management 📂
Allows users to:
- **Encrypt and decrypt specific folders**
- **Lock and unlock directories for enhanced privacy**
- **Monitor changes in sensitive directories**

### 5. Spoofer (Hardware Serial Modification) 🛠️
One of the core features of Oblivion Anonymizer is its ability to spoof hardware serial numbers using **Amidewin** and **VolumeID**.

#### **Amidewin**
- A powerful utility that interacts with low-level system firmware to modify DMI (Desktop Management Interface) information.
- Uses **kernel-mode drivers (.sys)** to apply changes.
- Can alter **UUID, BIOS serials, and motherboard identifiers**.

#### **VolumeID**
- A lightweight tool used to modify the **disk volume serial number**.
- Often used for anonymity or evading system tracking mechanisms.

### 6. Browser Data Management 🌐
Provides extensive controls over browser data privacy:
- **Delete history, cookies, and cache from Chrome, Edge, Firefox, Brave, and other major browsers**
- **Remove stored login credentials**
- **Clear local storage and browser extensions**

## Installation ⚙️
To install Oblivion Anonymizer, simply run the following command:
```bash
git clone https://github.com/124Px/Oblivion-Anonymizer.git
cd Oblivion-Anonymizer
python start.py
```

### Dependencies 📦
Required dependencies:
```bash
pip install -r requirements.txt
```

The following Python modules are required:
- `colorama`
- `requests`
- `pyperclip`
- `psutil`
- `tqdm`
- `cryptography`
- `Pillow`
- `customtkinter`
- `winshell`
- `pywin32`

## Usage 🖥️
After installation, launch the main script to access the graphical interface and configure settings based on your anonymity needs.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/124Px/Oblivion-anonymizer/blob/main/LICENSE) file for details.

## 🤝 Contribute
Contributions are welcome! Fork the repo and submit a pull request.

## ⭐️ Support
If you like this project, **give it a star** to support its development!

[![Stars](https://img.shields.io/github/stars/124Px/Oblivion-anonymizer.svg?style=social)](https://github.com/124Px/Oblivion-anonymizer)

⚠ **Disclaimer:** This tool is meant to be used responsibly and for legal purposes only. ❌ The author is not responsible for any misuse or consequences that arise from improper use of this software. Please ensure that you comply with local laws and regulations when using Oblivion Anonymizer. Stay safe and respect privacy ethics! 🔒

