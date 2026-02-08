import random
from ipaddress import ip_address


def main():
    firewall_rules = {
        "10.130.131.4":"block",
        "10.130.131.1":"block",
    }

    for x in range(10):
        ip = generate_random_ip()
        action = check_firewall_rules(ip, firewall_rules)
        print(f"IP: {ip}, Action: {action}")

def generate_random_ip():
    return f"10.130.131.{random.randint(1,10)}"

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

if __name__ == '__main__':
    main()