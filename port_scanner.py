import socket
import threading
from queue import Queue
import sys
import time

# Get the target IP from the user
target = input("Enter the IP address: ")
queue = Queue()

# Fill the queue with all possible ports (1 to 65535)
for port in range(1, 65536):
    queue.put(port)

def scan_port():
    """
    Core function to pick a port from the queue and check its status.
    """
    while not queue.empty():
        # Retrieve the next port from the queue
        port = queue.get()
        try:
            # Create a TCP socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) # Time to wait for a response
            
            # Try to connect to the target port
            result = s.connect_ex((target.strip(), port))
            
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            
            s.close()
        except:
            # Skip any errors and continue to the next port
            pass
        finally:
            # Mark the task as finished in the queue
            queue.task_done()

def start_scanner():
    """
    Initializes threads and manages the scanning process.
    """
    print(f"\n--- Scanning all 65535 ports on: {target} ---")
    print("--- Press Ctrl + C to STOP the scan immediately ---\n")
    
    try:
        # Start 100 threads for high-performance scanning
        thread_count = 100
        for i in range(thread_count):
            t = threading.Thread(target=scan_port)
            t.daemon = True # Ensure threads close when the main program exits
            t.start()
        
        # Keep the main thread active to listen for Ctrl+C
        # Using a loop instead of queue.join() for better responsiveness
        while not queue.empty():
            time.sleep(0.1) # Small delay to reduce CPU usage while waiting
            
        print("\n[!] Scan completed successfully.")

    except KeyboardInterrupt:
        # Gracefully handle the manual stop (Ctrl + C)
        print("\n\n[!] User interrupted the process. Stopping all threads...")
        sys.exit()

# Main entry point of the script
if __name__ == "__main__":
    start_scanner()