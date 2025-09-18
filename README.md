# Ping Alert System

## Overview

The Ping Alert System is a Python script that monitors incoming ICMP ping requests to a specific IP address and sends an email notification whenever someone tries to reach your system.

This tool is useful for monitoring network activity on your local network or public IP if your machine is reachable.

---

## Features

* Detects pings to a specified IP.
* Sends email notifications to a specified recipient.
* Prevents repeated emails for the same IP.
* Easy configuration and setup.

---

## Requirements

* Python 3.x
* Python libraries: `scapy`, `smtplib`, `email`
* Gmail account with 2-Step Verification enabled.
* Gmail App Password to securely send emails.
* Admin/root privileges to sniff network packets.

---

## Setup Instructions

### 1. Enable 2-Step Verification

1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Turn on **2-Step Verification** and follow the instructions.

### 2. Create Gmail App Password

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Select **Mail** as the app, and **Other** as the device.
3. Generate a 16-character App Password.
4. Use this password in the script as `EMAIL_PASSWORD`.

### 3. Install Dependencies

```bash
pip install scapy
```

### 4. Configure the Script

Edit the script with your details:

```python
YOUR_IP = "192.168.x.x"
EMAIL_SENDER = "yourgmail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "yourgmail@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

### 5. Run the Script

Run with admin/root privileges:

```bash
sudo python ping_alert.py  # Linux/macOS
```

or as Administrator on Windows.

---

## Usage

1. Start the script.
2. Ping your IP from another device:

```bash
ping 192.168.x.x
```

3. The script will detect the ping and send an email to `yourgmail@gmail.com`.

---

## Notes

* Only one email per unique IP per session is sent to avoid spamming.
* The script prints detected pings to the console for real-time monitoring.
* Works on local network IPs and public IPs if reachable.

---

## Full Python Script

Refer to the script in the Notion documentation or the included `ping_alert.py` file.
