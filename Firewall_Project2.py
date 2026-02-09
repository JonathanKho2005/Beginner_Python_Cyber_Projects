from scapy.all import sniff
from scapy.all import IP

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


def check_firewall_rules(ip,rules):
    return rules.get(ip,"allow")


sniff(prn=handle_packet)