# 🎓 Classroom Check

A simple interactive Python utility to walk through classroom technology checks — including audio, camera, document camera (Elmo), and Duo MFA bypass verification.

This tool is designed for quick tech setup confirmation before a class, meeting, or event, and includes troubleshooting help in PDF format.

---

## 🚀 Features

- ✅ Audio output test via `.wav` file
- ✅ Camera and document camera checks
- ✅ Duo MFA bypass check with IP capture
- ✅ Interactive prompts (yes/no)
- ✅ Opens relevant troubleshooting PDFs on failure
- ✅ Compatible with PyInstaller (Windows EXE support)

---

## 🖥️ Requirements

- **Windows OS**
- **Python 3.7+**
- No external libraries required (standard library only)

---

## 📦 Installation (Development)

Clone the repo and run the script directly with Python:

```bash
git clone https://github.com/Arcerite/classroom-check.git
cd classroom-check
python classroom_check.py
```

---

## 🛠️ Building the EXE with PyInstaller

You can turn this project into a standalone Windows executable using [PyInstaller](https://pyinstaller.org/).

### ✅ Prerequisites

- Python 3.7+ (on Windows)
- PyInstaller installed:

```bash
pip install pyinstaller
```

### 📦 Build Instructions

Run this command from the project directory:

```bash
pyinstaller --onedir --noconfirm --clean ^
  --icon=icon.ico ^
  --add-data "sound_test.wav;." ^
  --add-data "Audio.pdf;." ^
  --add-data "Camera.pdf;." ^
  --add-data "Elmo.pdf;." ^
  Classroom_Checker.py
```

> 💡 Note: Use `:` instead of `;` if you're on Linux or macOS:
> ```bash
> --add-data "sound_test.wav:."
> ```

### 📁 Output

- PyInstaller will create a new folder at `dist/Classroom_Checker/`
- Inside that folder will be:
  - `Classroom_Checker.exe` (your executable)
  - All bundled `.dll`s and dependencies
  - Your `.wav` and `.pdf` files

To run the app, just double-click the EXE or launch it from CMD:

```bash
dist\Classroom_Checker\Classroom_Checker.exe
```

> ⚠️ Keep the EXE and all data files in the same folder — do not move them individually.
