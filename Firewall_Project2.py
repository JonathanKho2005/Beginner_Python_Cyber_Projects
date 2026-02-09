from scapy.all import sniff
from scapy.all import IP
from Firewall_Project3 import write_log
from datetime import datetime

firewall_rules = {
    "20.189.173.18":"block",
    "10.130.131.4":"block",
}

def handle_packet(packet):
    print(packet.summary())
    if IP in packet:
        src=packet[IP].src
        action = check_firewall_rules(src, firewall_rules)
        print(f"Source IP: {src} -> {action}")

        #Create timestamp and log_message
        timestamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        log_message = f"{timestamp} | {src} | {action}"

        #Write logging into text file records
        write_log(log_message)

def check_firewall_rules(ip,rules):
    return rules.get(ip,"allow")

sniff(prn=handle_packet)