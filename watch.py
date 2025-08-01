import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define a regular expression pattern to match the YouTube embed URL
    pattern = re.compile(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"')

    # Search for the pattern in the input string
    match = pattern.search(s)

    # If a match is found, construct the shorter URL
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()
