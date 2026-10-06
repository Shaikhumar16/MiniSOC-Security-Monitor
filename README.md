\# MiniSOC - Python Based Security Monitoring



\## About the Project



MiniSOC is a small Python security monitoring project that I built to understand the basic working of a Security Operations Center (SOC).



The program reads simple security log files and looks for suspicious activities. When it finds a suspicious pattern, it displays an alert along with a basic severity level.



I kept this project simple because my main goal was to understand how security logs are monitored and how basic detection rules work.



\## What It Detects



The current version checks for:



\- Repeated failed login attempts

\- Possible port scanning

\- Possible SQL injection activity



\## How It Works



The project follows a simple process:



1\. Security events are stored in log files.

2\. Python reads the log files.

3\. The program searches for specific security event patterns.

4\. A suspicious pattern generates an alert.

5\. A severity level is displayed.



\## Technologies Used



\- Python

\- Log analysis

\- File handling

\- Basic security detection

\- Git

\- GitHub



No external Python packages are required.



\## Project Structure



```text

MiniSOC-Security-Monitor/

│

├── minisoc.py

├── README.md

├── requirements.txt

├── .gitignore

│

├── logs/

│   ├── login.log

│   └── web.log

