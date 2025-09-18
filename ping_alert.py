from scapy.all import sniff, ICMP, IP
import smtplib
from email.mime.text import MIMEText

# ==== CONFIGURATION ====
YOUR_IP = "Your_IP"                # Your local IP
EMAIL_SENDER = "personal_email@gmail.com"    # Your Gmail address
EMAIL_PASSWORD = "password"    # Your Gmail App Password
EMAIL_RECEIVER = "personal_email@gmail.com"  # Target email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
# ========================

# Keep track of IPs already alerted to avoid repeated emails
alerted_ips = set()

def send_email(source_ip):
    subject = "Ping Alert!"
    body = f"Your IP {YOUR_IP} was pinged by {source_ip}."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print(f"[+] Alert sent for ping from {source_ip}")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

def packet_callback(packet):
    if packet.haslayer(ICMP) and packet.haslayer(IP):
        if packet[IP].dst == YOUR_IP and packet[ICMP].type == 8:  # Type 8 = Echo request
            source_ip = packet[IP].src
            if source_ip not in alerted_ips:
                alerted_ips.add(source_ip)
                print(f"[!] Ping detected from {source_ip}")
                send_email(source_ip)

if __name__ == "__main__":
    print(f"[*] Monitoring pings to {YOUR_IP}...")
    sniff(filter="icmp", prn=packet_callback, store=0)
