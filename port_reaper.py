#!/usr/bin/python3

# Importing all necessary packages
import socket # Used to connect and test for open ports
import pyfiglet # Create banner
from datetime import datetime
from colorama import Fore, init # Colorise the banner
import time
import sys # Used for error handling

# Initialize colorama for colored text output
init(autoreset=True)

# Create dictionary of common ports and protocols
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    110: "POP3",
    143: "IMAP",
    123: "NTP",
}

# Function to create banner to be displayed when script is run
def print_banner():
    banner = pyfiglet.figlet_format("PORT REAPER")
    print(f"{Fore.LIGHTRED_EX}{banner}")
    print(f"{Fore.YELLOW}* Developed by Kathit Sagar *")
    print("")

# Function to scan ports on Target IP
def scan_ports(target):
    print("-" * 50)
    print(f"Scanning target: {target}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Display current date and time
    print(f"Scan started at: {now}")
    print("-" * 50)
    print("")

    scan_start_time = time.time() # Record start time of scan

    try:
        for port in range(1, 65536): # Test for all ports
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a IP/TCP socket
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port)) # Attempt to connect to the port
            if result == 0: # Successful result ( port open )
                protocol = common_ports.get(port) # Use port number scanned and search dictionary for associated protocol
                if protocol: # If port number is found in common port dictionary , get the protocol name
                    print(f"[*] Port {port} is open - {protocol}")
                else: # If port number is not found in common port dictionary , display Unknown
                    print(f"[*] Port {port} is open - Unknown")
            s.close() # Close the connection and move to next port


    except KeyboardInterrupt: # Handle interruption "Ctrl+C"
        print(f"{Fore.LIGHTRED_EX}Scan exited successfully.")
        sys.exit()
    except (OSError, ConnectionError): # Handle other errors
        print(f"{Fore.LIGHTRED_EX}Host is not responding.")
        sys.exit()

    scan_end_time = time.time() # Record end time of scan
    duration = scan_end_time - scan_start_time # Calculate duration for scan to complete
    return duration

# Function to display scan completion and duration
def scan_complete(duration):
    print("")
    print("-" * 50)
    print(f"{Fore.GREEN}Scan complete for target!")
    print(f"Time taken for scan: {duration:.2f}")
    print("-" * 50)

# MAIN fucntion to run the port scanner
def run_scanner():
    print_banner()
    target = input("Target IP to scan: ") # Get target from user
    duration = scan_ports(target)
    scan_complete(duration)

# Execute main function
run_scanner()