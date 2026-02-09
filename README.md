# Beginner_Python_Cyber_Projects
A repository which contains beginners Python cybersecurity projects.

---
## Learnings

- Real‑time packet sniffing using Scapy  
- Extraction of source IP addresses from incoming packets  
- Rule‑based filtering with allow/block decisions  
- Simulated block action using control‑flow termination  
- Timestamped event logging to `firewall_log.txt`  
- Modular architecture separating packet handling, rule evaluation, and logging  

---

## How It Works

The simulator listens for incoming network packets.  
For each packet:

1. The source IP address is extracted  
2. The IP is checked against a predefined rule set  
3. The packet is marked as **allowed** or **blocked**  
4. A timestamped log entry is written to `firewall_log.txt`  
5. Blocked packets stop further processing  

This mirrors the behaviour of a basic firewall without requiring kernel‑level packet manipulation.

---

## Project Structure

```
Firewall_Project1.py     # Firewall simulator using Python logic without involving real time packets yet
Firewall_Project2.py     # Main firewall logic (packet handling + rule checking)
Firewall_Project3.py     # Logging module (write_log function)
firewall_log.txt         # Generated log file
```

---

## Example Log Entries

```
02/09/2026 06:45:12 PM | 192.168.1.5 | allowed
02/09/2026 06:45:13 PM | 20.189.173.18 | BLOCKED
```

---

## Requirements

- Python 3.x  
- Scapy  
- Administrator/root privileges (required for packet sniffing)


## Running the Firewall using terminal

Run the main script with elevated privileges:

```bash
sudo python3 Firewall_Project2.py
```

The firewall will begin sniffing packets and writing log entries to `firewall_log.txt`.

---


