# Port Scanner

## Overview

This Port Scanner is a Python-based tool that allows users to scan a target host for open and closed ports. It supports scanning single ports, a range of ports, or specific ports separated by commas. The program runs multi-threaded scans, making it efficient for checking multiple ports quickly.

## Features

- **Single port scanning**: Check if a specific port is open or closed.
- **Range of ports scanning**: Define a range of ports to scan.
- **Multiple specific ports scanning**: Specify a list of ports separated by commas.
- **Multi-threaded scanning**: Optimized with threading for faster results.

## Requirements

- **Python 3.x**
- **Socket Library**: Included in Python's standard library, so no additional installation is required.
- **Queue Library**: Also part of Python’s standard library.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dawishcyber/Port-Scanner-Project
   cd Port-Scanner-Project
   ```

2. **Run the Program**:
   Ensure that the script has execution permissions and then run it using Python.

   ```bash
   python port_scanner.py <host> <ports> <timeout>
   ```

## Usage

### Arguments

- `<host>`: The IP address or domain name of the target host to scan.
- `<ports>`: Specify a single port (e.g., `80`), a range of ports (e.g., `20-100`), or multiple ports separated by commas (e.g., `22,80,443`).
- `<timeout>`: Optional. Sets the timeout duration in seconds for each port connection attempt. Defaults to `1` second if not specified.

### Examples

1. **Scan a single port**:
   ```bash
   python port_scanner.py 192.168.1.1 80
   ```

2. **Scan a range of ports**:
   ```bash
   python port_scanner.py 192.168.1.1 20-100
   ```

3. **Scan multiple specific ports**:
   ```bash
   python port_scanner.py 192.168.1.1 22,25,80,443
   ```

4. **Scan with a custom timeout**:
   ```bash
   python port_scanner.py 192.168.1.1 80-100 0.5
   ```

## Program Structure

- **`welcome_banner`**: Displays a banner with instructions when the script starts.
- **`scan_port()`**: Attempts to connect to a specified port and checks if it is open or closed.
- **`scanner()`**: Manages port parsing, threading, and starting port scans.
- **`main()`**: Manages user inputs, validates host IP, and starts the scanning process.

## Example Output

When the scan completes, the program will display a list of open and closed ports. The output will look something like this:

```plaintext
****************************************************
*                                                  *
*            Scan Completed Successfully!          *
****************************************************
Time Ended: 12:34:56

Port 22 is open
Port 80 is closed
Port 443 is open
```

## Notes

- **IP Validation**: The program validates the provided IP or domain before scanning. It also attempts to resolve domain names to IP addresses.
- **Threading**: Each port is scanned in a separate thread to reduce scanning time, especially for large ranges or multiple ports.
```

