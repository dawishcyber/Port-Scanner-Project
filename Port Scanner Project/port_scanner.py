import socket
import sys
from datetime import datetime
import threading
from queue import Queue

# Banner to show upon script startup
welcome_banner = """
****************************************************
*                                                  *
*               Welcome to Port Scanner            *
*                                                  *
****************************************************
* Guide:                                           *
* - Scan a single port: e.g., 20                   *
* - Scan a range of ports: e.g., 20-100            *
* - Scan specific ports separated by commas: e.g., *
*   20,25,80                                       *
****************************************************
"""
# Display the welcome banner
print(welcome_banner)

# Queue for storing the results in a thread-safe manner
outputs = Queue()

# A function for socket client
def scan_port(host, port, timeout=1):
    try:
        # Open  a socket object
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a time to wait for each port to respond
        sk.settimeout(timeout)

        # Check if port is within valid range
        if port >= 1 and port <= 65535:
            result = sk.connect_ex((host, port))
            sk.close() 

            # If the connection was successful, the port is open
            if result == 0:
                outputs.put((port, f"Port {port} is open"))
            else:
                outputs.put((port, f"Port {port} is closed"))
        else:
            outputs.put(f"Port {port} is out of range.")
    
    except socket.error as e:
        # Socket errors like connection issues
        outputs.put(f"Socket Error on port {port}: {e} ")
                
    except Exception as e:
        # Catch all other unexpected errors
        outputs.put(f"Unexpected error on Port {port}: {e}")

 # Function to determine which ports to scan based on input   
def scanner(host, ports, timeout):
    ports_to_scan = []
    if "-" in ports:
        # Handle port ranges
        port_range = ports.split("-")
        ports_to_scan = range(int(port_range[0]), int(port_range[1]) + 1)
    elif "," in ports:
        # Handle comma-separated list of ports
        ports_to_scan = [int(port.strip()) for port in ports.split(",")]
    else:
        # Single port as a list
        ports_to_scan = [int(ports)]  
     
    # Start a thread for each port
    threads = []
    for port in ports_to_scan:
        thread = threading.Thread(target=scan_port, args=(host, int(port), timeout))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
# Main function to manage arguments and initiate the scan        
def main():
    # Get arguments or default values
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = sys.argv[2] if len(sys.argv) > 2 else "80"
    timeout = float(sys.argv[3]) if len(sys.argv) == 3 else 1.0 

    # Validate host IP format
    try:
        socket.inet_aton(host)
    except socket.error:
        try:
            host = socket.gethostbyname(host)  # Resolve domain to IP
            print(f"Resolved domain to IP: {host}")
        except socket.gaierror:
            print("Invalid domain name or IP address. Exiting...")
            sys.exit(1)

    print("\nOutput details")
    print(f"Scanning target: {host} \nTime started: {datetime.now().strftime('%H:%M:%S')} \n")
    
    # Call the scanner function
    scanner(host, port, timeout)

    # Sort outputs by port number before printing
    sorted_outputs = []
    while not outputs.empty():
        sorted_outputs.append(outputs.get())
    sorted_outputs.sort(key=lambda x: x[0])

    # Print the scan results
    for _, output in sorted_outputs:
        print(output)

    # Completed scan banner
    completed_banner = f"""
****************************************************
*                                                  *
*            Scan Completed Successfully!          *                                                  
****************************************************                             
Time Ended: {datetime.now().strftime('%H:%M:%S')}

"""
    print(completed_banner)

    # Exit the script
    sys.exit(1)

# Run the main function when script is executed
if __name__ == "__main__":
    main()