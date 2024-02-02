import socket
import sys

#Pseudo code

print("---Port Scanner---")

def print_help_message():
    help_message = """
Usage: python3 port_scanner.py [OPTIONS]

Options:
  --help            show this help message and exit
  --target TARGET   specify the target IP address or hostname (required)
  --start-port N    specify the start of the port range to scan (default: 1)
  --end-port N      specify the end of the port range to scan (default: 1024)

Example:
  python3 port_scanner.py --target example.com --start-port 1 --end-port 1024
    """
    print(help_message)

#-t TCP (Default)
#-u UDP

def scan_port(ip, port, verbose):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the socket connection
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open.")
            else:
                if sys.argv == verbose: 
                    print(f"Port {port} is closed.")
            sock.close()
    except socket.error as err:
        print(f"Couldn't connect to server: {err}")

def parse_ports(port_arg):
    if '-' in port_arg:
        start_port, end_port = map(int, port_arg.split('-'))
        return range(start_port, end_port + 1)
    else:
        return [int(port_arg)]

def main(target, ports, Verbose=False):
    if "--help" in sys.argv or len(sys.argv) == 1:
        print_help_message()
        sys.exit()
    print(f"Starting scan on host: {target}")
    for port in ports:
        scan_port(target, port, verbose)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <IP address> [-v] [-p port/port-range]")
        sys.exit(1)

    target = sys.argv[1]
    verbose = '-v' in sys.argv
    
    # Default port range
    ports = range(1, 1025)

    # Parse custom port/port-range
    if '-p' in sys.argv:
        p_index = sys.argv.index('-p') + 1
        if p_index < len(sys.argv):
            ports = parse_ports(sys.argv[p_index])
        else:
            print("Error: No port or port range specified with -p option.")
    
    main(target, ports, verbose)
    

#MORE IDEAS
#asynchronous scanning (multi-threading), banner grabbing
