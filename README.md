Python Key & Text Logger (Educational Project)
📌 Overview

This repository contains a Python-based logging project developed for educational and cybersecurity lab purposes.
The project demonstrates how keyboard input can be captured, processed, and stored with timestamps using two different approaches:

Character-by-Character Logging

Line-Based Text Logging

The focus of this project is on learning input handling, event-driven programming, timestamping, and responsible logging practices.

🎯 Objectives

Understand keyboard event handling in Python

Compare real-time keystroke logging vs buffered text logging

Learn how timestamps improve log analysis

Practice ethical and controlled logging for lab environments

Maintain a clean, documented GitHub repository

🛠️ Technologies Used

Python 3.x

pynput – for keyboard event listening

datetime – for timestamp generation

Git & GitHub – version control

Virtual Environment (venv) – dependency isolation

📂 Project Structure
Keylogger/
│
├── char_logger.py        # Character-by-character logger
├── line_logger.py        # Line-based text logger
├── char_log.txt          # Output file for character logger
├── line_log.txt          # Output file for line logger
├── README.md             # Project documentation
└── .gitignore            # Ignored files and folders

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/MuhammadZaidSaqib/Keg-logger.git
cd Keg-logger

2️⃣ Create and Activate Virtual Environment (Recommended)
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux / macOS

3️⃣ Install Dependencies
pip install pynput


🐉 Kali Linux Setup Guide
⚠️ Important Note for Kali Users

Kali Linux follows PEP 668 (Externally Managed Python Environment), which prevents installing Python packages globally using pip.

Because of this, you must use a virtual environment to install project dependencies safely.

🛠️ Step-by-Step Setup on Kali Linux
1️⃣ Clone the Repository
git clone https://github.com/MuhammadZaidSaqib/Keg-logger.git
cd Keg-logger

2️⃣ Install Virtual Environment Support (if not installed)
sudo apt install python3-venv

3️⃣ Create a Virtual Environment
python3 -m venv .venv

4️⃣ Activate the Virtual Environment
source .venv/bin/activate


After activation, your terminal should look like:

(.venv) kali@kali:~/Keg-logger$

5️⃣ Install Required Dependency
pip install pynput


(Optional – save dependencies)

pip freeze > requirements.txt

6️⃣ Run the Program
python Keylogger.py
▶️ Usage
🔹 Character-by-Character Logger

Logs each key press individually with timestamps.

Run:

python char_logger.py


Features:

Logs normal keys (a, b, 1, etc.)

Logs special keys ([Key.space], [Key.enter])

Timestamped entries

Real-time event handling

Sample Output (char_log.txt):

2026-02-07 14:35:10 - h
2026-02-07 14:35:11 - e
2026-02-07 14:35:12 - [Key.space]

🔹 Line-Based Logger

Logs complete lines of text exactly as typed.

Run:

python line_logger.py


Features:

Logs full sentences

Cleaner, readable output

Timestamp added at submission time

Stops when user types EXIT

Sample Output (line_log.txt):

[2026-02-07 14:40:12] hello how are you
[2026-02-07 14:41:03] this is proper text logging

🔄 Workflow Explanation
Character Logger:

Start program

Capture keyboard events using pynput.Listener

Attach timestamp to each key

Write to log file

Stop execution manually (ESC or termination)

Line Logger:

Start program

Accept full text input

Timestamp the complete line

Write to log file

Stop by typing EXIT

✅ Key Features

Timestamped logging

Special key handling

Clean and readable logs

Separation of logging methods

Lab-safe and controlled execution

Well-documented project structure

⚠️ Ethical Notice

This project is created strictly for educational and laboratory purposes.
It was tested only on the developer’s own system.

❌ Not intended for unauthorized monitoring
❌ Not intended for real-world surveillance
✔ Focused on learning input handling mechanisms responsibly

📘 Learning Outcomes

Practical understanding of keyboard input capture

Event-driven programming in Python

Importance of readable logs in security analysis

Ethical boundaries in cybersecurity projects

Professional GitHub documentation practices

📌 Future Improvements

Configurable logging modes

Centralized log formatting

GUI-based input logger (lab-safe)

Log analysis and visualization

👤 Author

Muhammad Zaid Saqib
Cybersecurity Student | Python Enthusiast

🔗 GitHub: https://github.com/MuhammadZaidSaqib
