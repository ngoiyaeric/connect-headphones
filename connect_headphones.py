import time
import os
import subprocess

# Define the path to the shared directory
shared_dir = "/path/to/shared_dir"

def get_paired_devices():
    # Use the blueutil command to get a list of paired devices
    output = subprocess.run(["blueutil", "--paired"], capture_output=True, text=True)
    devices = output.stdout.strip().split("\n")
    return devices

def connect_headphones(mac_address):
    # Use the blueutil command to connect a specific device by MAC address
    subprocess.run(["blueutil", "--connect", mac_address], check=True)

def check_headphones():
    state = "OFF"  # Initial state

    while True:
        if state == "OFF":
            # Check if the headphones are connected
            if os.path.exists(os.path.join(shared_dir, "headphones_connected")):
                state = "CONNECTED"

        elif state == "DISCONNECTED":
            # Check if the headphones are disconnected
            if not os.path.exists(os.path.join(shared_dir, "headphones_connected")):
                devices = get_paired_devices()
                if devices:
                    most_recent_device = devices[-1]
                    connect_headphones(most_recent_device)
                    state = "CONNECTED"

        elif state == "CONNECTED":
            # Check if the headphones are disconnected
            if not os.path.exists(os.path.join(shared_dir, "headphones_connected")):
                state = "DISCONNECTED"

        time.sleep(1)

if __name__ == "__main__":
    check_headphones()
