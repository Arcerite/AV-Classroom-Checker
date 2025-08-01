# 🎓 AV Classroom Checker Suite

**By Caleb Peters / Arcerite**  
_A multi-language toolkit for verifying classroom AV readiness and Duo MFA bypass._

This repository contains two implementations — one in **Python** and one in **Java** — of a lightweight classroom technology verification tool designed for AV/IT technicians, instructors, and classroom support staff at GVSU or similar institutions.

Each version walks through a checklist of key AV features (camera, audio, Elmo/doc cam) and includes troubleshooting guidance and MFA bypass validation.

> ⚡ **Recommendation:** The Java version is faster and more streamlined. Use it when speed and simplicity are priorities.

---

## 🧰 Available Versions

### ☕ Java Edition (`/Java-Version`) – **Recommended**

A standalone Java console utility designed for quick AV validation using Windows system commands and user-driven checks. This version runs fast, requires no dependencies, and is ideal for AV/IT technician use in the field.

- 📸 Camera opens in Windows Camera app
- 🔊 Audio settings via `control mmsys.cpl sounds`
- 🔐 Duo MFA check with IP capture
- 🧾 Result summary and troubleshooting support

🔗 **[View Java Version README](./Java-Version/README.md)**

---

### 🐍 Python Edition (`/Python-Version`)

An interactive, scriptable classroom checker built in Python 3 — designed for flexibility, EXE conversion, and PDF-linked troubleshooting documentation.

- ✅ Audio output test
- ✅ Camera and Elmo input verification
- ✅ Duo MFA bypass check with local IP capture
- ✅ Opens troubleshooting guides if issues are detected
- ✅ Compatible with PyInstaller for EXE packaging

🔗 **[View Python Version README](./Python-Version/README.md)**

---

## 📁 Folder Structure

```
/
├── Java-Version/          # Java version (ClassroomCheck.java)
│   └── README.md
├── Python-Version/        # Python version (Classroom_Checker.py, PDFs, .wav)
│   └── README.md
└── README.md              # You are here (root project overview)
```

---

## ⚙️ System Requirements

| Requirement   | Python Version         | Java Version (⚡ Recommended) |
|---------------|------------------------|-------------------------------|
| OS            | Windows 10 or 11       | Windows 10 or 11              |
| Language      | Python 3.7+            | Java 8 or newer               |
| Dependencies  | Standard library only  | None                          |
| Packaging     | PyInstaller (optional) | Compile via `javac`           |

---

## 🤔 Why Two Versions?

This repo supports both **script-based automation** (Python) and **performance-focused console tooling** (Java). Use the version that best suits your environment, comfort level, or workflow.

- Use **Java** when you need speed, simplicity, and minimal dependencies.
- Use **Python** if you want more flexibility, error handling, and easier cross-platform editing.

---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute with attribution.

```
MIT License © 2025 Caleb Peters / Arcerite
```

---

## ✉️ Contact

Questions or suggestions? Open an issue or reach out via GitHub.

---
