import socket
import argparse
from colorama import Fore, Style

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            print(f"{Fore.GREEN}Port {port} is open{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Port {port} is closed or filtered{Style.RESET_ALL}")

def scan(ip, ports):
    print(f"""
███▄ ▄███▓ ▄▄▄     ▓██   ██▓ ██▓     ▒█████    ██████  ▄████▄   ▄▄▄       ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▒██  ██▒▓██▒    ▒██▒  ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄   ▒██ ██░▒██░    ▒██░  ██▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██  ░ ▐██▓░▒██░    ▒██   ██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒ ░ ██▒▓░░██████▒░ ████▓▒░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
░      ░     ░   ▒   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒  ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
       ░         ░  ░░ ░         ░  ░    ░ ░        ░  ░ ░            ░  ░         ░ 
                     ░ ░                               ░
""")
    print(f"Scanning {ip}")
    for port in ports:
        scan_port(ip, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maylo's Network Scanner")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("-p", "--ports", type=str, default="1-1024",
                        help="Port range or comma-separated list of ports (default: 1-1024)")

    args = parser.parse_args()

    target_ip = args.target_ip
    port_range = args.ports

    if "-" in port_range:
        start_port, end_port = port_range.split("-")
        ports = range(int(start_port), int(end_port) + 1)
    else:
        ports = [int(port) for port in port_range.split(",")]

    scan(target_ip, ports)

while True:
    pass