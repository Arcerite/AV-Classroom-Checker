# 🎓 Classroom Check (Python-Version)

A simple interactive Python utility to walk through classroom technology checks — including audio, camera, document camera (Elmo), and Duo MFA bypass verification.

This tool is designed to assist technicians and support staff in quickly verifying classroom AV readiness.

---

## 🚀 Features

- ✅ Launches Windows Sound Settings to manually test audio output  
- ✅ Camera and document camera (Elmo) checks via built-in Camera app  
- ✅ Duo MFA bypass check with automatic IP address display  
- ✅ Fully interactive terminal prompts  
- ✅ Provides troubleshooting instructions in case of failure  
- ✅ No dependencies beyond Python standard library  
- ✅ Supports bundling as a Windows executable with PyInstaller  

---

## 🖥️ Requirements

- **Windows OS**
- **Python 3.7+**
- No external libraries required (standard library only)

---

## 📦 Installation (Development)

Clone the repo and run the script directly:

```bash
git clone https://github.com/Arcerite/AV-Classroom-Checker-For-GVSU.git
cd AV-Classroom-Checker-For-GVSU/Python-Version
python classroom_check.py
```

---

## 🛠️ Building the EXE with PyInstaller

You can turn this script into a standalone `.exe` file using [PyInstaller](https://pyinstaller.org/).

### ✅ Prerequisites

- Python 3.7+ (on Windows)
- PyInstaller installed:

```bash
pip install pyinstaller
```

### 📦 Build Instructions

```bash
pyinstaller --onedir --noconfirm --clean ^
  --icon=icon.ico ^
  classroom_check.py
```

> 💡 `--onedir` creates a folder with the `.exe` and all dependencies. You can use `--onefile` if you prefer a single-file EXE, though it may launch slower.

---

## 📁 Output

- PyInstaller will create a new folder at `dist/classroom_check/`
- Inside that folder will be:
  - `classroom_check.exe` (your executable)
  - Required `.dll` and support files

Launch the app by double-clicking the EXE or running it in CMD:

```bash
dist\classroom_check\classroom_check.exe
```

---

## ⚡ Recommendation

> 🔄 A **Java-Version** of this tool is also available in the repo. It launches faster and offers better native integration on Windows.  
> You can find it under: `/Java-Version`

---

## 🧾 License

MIT License.  
© Caleb Peters / Arcerite
