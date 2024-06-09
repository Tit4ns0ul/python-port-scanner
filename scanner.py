#!/bin/python3

import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import os

# Define port ranges for different options
PORT_RANGES = {
    "well-known": (0, 1023),
    "registered": (1024, 49151),
    "dynamic": (49152, 65535),
    "wnr": (0, 49151),
    "full": (0, 65535),
}


def print_help():
    print("\033[1;32;40mSimple Port Scanner Help\033[0m")
    print("\033[1;37;40mUsage:\033[0m python3 scanner.py <IP_Address> [Option]")
    print("\033[1;34;40mOptions:\033[0m")
    print("  -wn, --well-known   Scan for well-known ports (0-1023)")
    print("  -r, --registered    Scan for registered ports (1024-49151)")
    print("  -d, --dynamic       Scan for dynamic/private ports (49152-65535)")
    print("  -wnr                Scan for well-known and registered ports (0-49151)")
    print("  -f, --full          Scan for all ports (0-65535)")
    print("  -h, --help          Show this help message and exit")
    print(
        "  -o, --output        Save the results to a specified path Example -o /home/user/output.txt"
    )
    print("\033[1;34;40mExample:\033[0m python3 scanner.py 192.168.1.1 --well-known")
    print(
        "\033[1;31;40mNote:\033[0m Ensure you have the necessary permissions to scan the target system."
    )


def scan_port(ip, port, output_file=None):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Adjust timeout as needed
            result = s.connect_ex((ip, port))
            if result == 0:
                open_port_info = f"Port {port} is open\n"
                print(open_port_info, end="")
                if output_file:
                    with open(output_file, "a") as file:
                        file.write(open_port_info)
    except socket.error:
        pass  # Handle errors if needed


# Parse arguments and set port range
if len(sys.argv) < 2:
    print("Invalid number of arguments.")
    print_help()
    sys.exit()
elif sys.argv[1] in ("-h", "--help"):
    print_help()
    sys.exit()

target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
port_range = PORT_RANGES["full"]  # Default to full range
output_path = None

# Parse arguments and set port range
if len(sys.argv) < 2:
    print("Invalid number of arguments.")
    print_help()
    sys.exit()
elif sys.argv[1] in ("-h", "--help"):
    print_help()
    sys.exit()

target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
port_range = PORT_RANGES["well-known"]  # Default to well-known range
output_path = None

# Check for additional options
for arg in sys.argv[2:]:
    if arg in ("-wn", "--well-known"):
        port_range = PORT_RANGES["well-known"]
    elif arg in ("-r", "--registered"):
        port_range = PORT_RANGES["registered"]
    elif arg in ("-d", "--dynamic"):
        port_range = PORT_RANGES["dynamic"]
    elif arg == "-wnr":
        port_range = PORT_RANGES["wnr"]
    elif arg in ("-f", "--full"):
        port_range = PORT_RANGES["full"]
    elif arg in ("-o", "--output"):
        output_flag = "-o" if "-o" in sys.argv else "--output"
        output_index = sys.argv.index(output_flag)
        try:
            output_path = sys.argv[output_index + 1]
            # Resolve the relative path to an absolute path
            output_path = os.path.abspath(output_path)
            # Check if the provided path includes a filename
            if not os.path.splitext(output_path)[1]:
                print("Please provide a file name with the extension for the output.")
                sys.exit()
        except IndexError:
            print("Please provide a specific path with a file name for the output.")
            sys.exit()


# Adding a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("Scanning port range: {}-{}".format(port_range[0], port_range[1]))
print("-" * 50)

# Start the port scan
with ThreadPoolExecutor(max_workers=100) as executor:  # Adjust max_workers as needed
    for port in range(port_range[0], port_range[1] + 1):
        executor.submit(scan_port, target, port, output_path)

# Handle keyboard interrupt
try:
    pass
except KeyboardInterrupt:
    print("\nExiting program!")
    sys.exit()

# Handle exceptions
except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
