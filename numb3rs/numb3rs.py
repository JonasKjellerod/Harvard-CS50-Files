import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regular expression pattern for a valid IPv4 address
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    # Check if the input matches the pattern
    if pattern.match(ip):
        # Split the IP address into its components
        parts = ip.split('.')
        # Check if each part is between 0 and 255
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()

