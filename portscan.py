# PA 1
# Karina Yakubisin

import socket
import datetime

def get_inputs(): # gather user input
    target = input("Enter a target to scan: ") # target host ip or domain
    print("Please enter the range of ports you would like to scan on the target")
    start = int(input("Enter a start port: ")) # port user wants to begin scanning at
    end = int(input("Enter a end port: ")) # port user wants to scan until
    return target, start, end

def main():

    target, start, end = get_inputs()

    # timeout if target is not responding. checks if the target is reachable, if not, exists
    try:
        test_sock = socket.create_connection((target, 80), timeout=3)
        test_sock.close()
    except socket.error as err:
        print("Connection timeout. Target not responding.")
        return False

    # use datetime to get the timestamp of when the scanning started
    scan_start_time = datetime.datetime.now()

    print(f"Scanning started at: {scan_start_time}")

    # loop through to scan every port within the range (including the end)
    for port in range(start, end + 1):
        try:
            # use the socket library to create a sock so that the program can communicate with the ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # timeout
            # socket.settimeout(1)
            result = sock.connect_ex((target, port)) # scan.
            if result == 0: # port is open is the result is 0
                print(f"Port {port} is open")
            elif result != 0:
                print(f"Port {port} is closed")
            sock.close()
        except socket.error as err: # catch
            print(f"Error scanning port {port}: {err}")
            return False
        
    print("Port Scanning Completed")

main()

    


