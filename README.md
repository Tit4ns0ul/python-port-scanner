Simple Port Scanner
This Python script is a simple port scanner that allows users to scan a target host for open TCP ports within a specified range. By providing an IP address or hostname as a command-line argument, users can initiate a scan to identify open ports on the target system.

Features:
Target Specification: Users can specify the target host either by providing an IP address or hostname as a command-line argument.
Port Scanning: The script scans a range of TCP ports (from 50 to 84 by default) on the target host to determine if they are open, closed, or filtered.
Banner Display: A banner is displayed before starting the scan, providing information about the target host and the time the scan started.
Error Handling: The script handles various exceptions gracefully, including KeyboardInterrupt, socket.gaierror, and socket.error, ensuring smooth execution and user-friendly error messages.
Efficient Socket Handling: The script efficiently creates and closes socket connections for each port to minimize resource consumption and improve performance.
Usage:
Ensure that Python 3.x is installed on your system.
Run the script (scanner.py) from the command line, providing the target IP address or hostname as a command-line argument:
php
Copy code
python3 scanner.py <target_ip_or_hostname>
The script will initiate a port scan on the specified target and display the results, indicating open ports if found.
Security Considerations:
Authorization: Ensure that you have proper authorization before scanning any network or system. Unauthorized port scanning may be considered intrusive and potentially illegal.
Use Responsibly: Port scanning should be performed responsibly and ethically, respecting the privacy and security of network owners and adhering to applicable laws and regulations.
Avoid Abuse: Do not misuse this script for malicious purposes, such as scanning systems without permission or launching attacks against vulnerable services.
Disclaimer:
This script is intended for educational and testing purposes only. The author assumes no liability for any misuse or damage caused by the use of this script. Users are solely responsible for their actions and must use this script responsibly and in compliance with applicable laws and regulations.
