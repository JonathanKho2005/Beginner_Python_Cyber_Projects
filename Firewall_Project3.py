# from scapy.all import sniff, IP
# from Firewall_Project2 import handle_packet, check_firewall_rules
import datetime

def get_current_datetime():
    now = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    print(now)

if __name__ == '__main__':
    get_current_datetime()


