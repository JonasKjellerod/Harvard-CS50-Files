import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Define a regular expression pattern to match the word "um" case-insensitively
    pattern = re.compile(r'\bum\b', re.IGNORECASE)

    # Find all matches in the input string
    matches = pattern.findall(s)

    # Return the number of matches
    return len(matches)

if __name__ == "__main__":
    main()
