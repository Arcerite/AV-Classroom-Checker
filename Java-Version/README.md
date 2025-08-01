# 🎓 ClassroomCheck (Java Version)

**Version 2.0 – by Caleb Peters / Arcerite**

A lightweight, Windows-based Java console application that automates classroom AV and authentication checks. Designed for AV/IT technicians to quickly verify proper classroom setup including cameras, audio, document cameras (Elmo), and Duo MFA bypass.

> ⚡ The **Java version is faster** and **recommended** for day-to-day use.

---

## ✅ Features

- 📸 **Camera Test** – Verifies built-in webcam functionality  
- 📄 **Doc Cam (Elmo) Test** – Confirms document camera operation  
- 🔊 **Speaker/Audio Check** – Opens Windows sound settings for manual speaker test  
- 🔐 **Duo MFA Override Test** – Opens GVSU login and logs local IP if bypass fails  
- 🛠️ **Troubleshooting Mode** – Guides user through resolving common issues  
- 📋 **Results Summary** – Final report of all system checks  

---

## 🖥️ Requirements

- Operating System: **Windows 10 or 11**  
- Java Version: **Java 8 or newer**  
- Terminal: CMD or any Windows terminal supporting `cls`  

---

## 🚀 How to Run

You have two options to run the app:

### ✅ Option 1: Easiest (No Compilation Needed)

Use the provided `.class` file and `.bat` launcher:

1. Download or clone the repo  
2. Navigate to the `Java-Version` folder  
3. Double-click `Run_Classroom_Check.bat` to launch the app

> ☑️ This will automatically run the precompiled `ClassroomCheck.class` with one click — no setup or command line required.

---

### 🔧 Option 2: Manual Compile & Run

If you want to compile it yourself:

1. **Download** or clone the repo:  
   `git clone https://github.com/yourusername/ClassroomCheck.git`  
   `cd ClassroomCheck/Java-Version`

2. **Compile the program**:  
   `javac ClassroomCheck.java`

3. **Run the program**:  
   `java ClassroomCheck`

---

## 🧪 What to Expect

| Step               | What Happens                                                      |
|--------------------|-------------------------------------------------------------------|
| 🎥 Camera Check     | Opens Windows Camera app – user confirms webcam is working        |
| 📄 Elmo Check       | Instructs user to test document cam via camera source switch      |
| 🔐 Duo MFA Test     | Opens GVSU portal – checks if Duo MFA is bypassed                 |
| 🔊 Audio Check      | Opens Sound Settings – user uses native "Test" speaker function   |
| 🧠 Troubleshooting  | If any check fails, helpful steps are provided                    |
| 🧾 Summary          | Displays all test results at the end                              |

---

## 📁 File Overview

```
Java-Version/
│
├── ClassroomCheck.java        # Main application source
├── ClassroomCheck.class       # Precompiled Java bytecode
├── Run_Classroom_Check.bat    # Easy launcher for Windows users
├── README.md                  # Project instructions (this file)
```

---

## ❓ Troubleshooting

- **App doesn't open system dialogs**: Ensure you're on Windows and running the terminal with permission to execute apps.  
- **"control mmsys.cpl sounds" doesn't open**: This only works on Windows. Not compatible with macOS or Linux.  
- **MFA test fails**: Check network, Duo setup, and review your IP if needed for allowlisting.  
- **.class file won’t run**: Make sure Java is installed and added to your PATH.

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute with attribution.

```
MIT License © 2025 Caleb Peters / Arcerite
```
