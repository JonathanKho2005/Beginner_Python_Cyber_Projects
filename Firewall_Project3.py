import datetime

now = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

def write_log(log):
    with open("firewall_log.txt", "a") as log_file:
        log_file.write(f"{log}\n")


