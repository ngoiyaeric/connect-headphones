import time
import subprocess

def get_paired_devices():
    # Use the blueutil command to get a list of paired devices
    output = subprocess.run(["blueutil", "--paired"], capture_output=True, text=True)
    devices = output.stdout.strip().split("\n")
    return devices

def connect_headphones(mac_address):
    # Use the blueutil command to connect a specific device by MAC address
    subprocess.run(["blueutil", "--connect", mac_address], check=True)

def is_bluetooth_on():
    # Use the blueutil command to check if Bluetooth is on
    output = subprocess.run(["blueutil", "--power"], capture_output=True, text=True)
    return output.stdout.strip() == "1"

def check_headphones():
    state = "OFF"  # Initial state

    while True:
        bluetooth_on = is_bluetooth_on()

        if state == "OFF" and bluetooth_on:
            devices = get_paired_devices()
            if devices:
                most_recent_device = devices[-1]
                connect_headphones(most_recent_device)
                state = "CONNECTED"

        elif state == "CONNECTED" and (not bluetooth_on or not get_paired_devices()):
            state = "OFF"

        time.sleep(1)

if __name__ == "__main__":
    check_headphones()
