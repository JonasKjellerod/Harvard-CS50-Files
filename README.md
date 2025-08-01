# Morning News brief
#### Video Demo:  <https://youtu.be/2Wpy3gHQ3XY>
#### Description: This is my final project for the CS50´s introduction to programming with python. It displays several categories of news, and can also read them out loud if your are busy. I´m sorry for my voice, but I was really sick when I recorded the video!!


# Morning News Program

This project, called **Morning News Program**, is a Python-based application that fetches, displays, and optionally reads aloud the latest news headlines. It offers a simple yet effective way to stay updated with current events by pulling news from a reliable source (NewsAPI). The program allows users to select specific categories of news, making it customizable for individual preferences.

## Features

### 1. Fetch Top News Headlines
The program connects to the [NewsAPI](https://newsapi.org/) to retrieve top headlines from various categories, such as:
- General
- Business
- Technology
- Sports
- Health
- Entertainment

Users can select their preferred category via a menu.

### 2. Display News in Styled Format
The news articles are displayed in a visually appealing table format using the `rich` library. Each article includes:
- Article number
- Source name
- Title (cleaned of unnecessary parts)
- Description
- URL (for reading the full article)

### 3. Text-to-Speech Functionality
For convenience, the program can read news articles aloud using the `pyttsx3` library. This feature is especially helpful for multitasking users.The system must have a compatible TTS engine installed and configured. Users may need to ensure that their audio output devices are set up properly to hear the speech.


### 4. User-Friendly Options
- Users can choose whether to read the news aloud or just display it.
- The program provides clear prompts and fallback defaults for invalid inputs.

### 5. Robust Code Structure
The project includes modular functions for fetching news, displaying it, and handling user inputs. It also implements error handling for scenarios like network failures or invalid API keys.

## Prerequisites

### Python Version
Make sure you have **Python 3.8 or later** installed on your system.

### API Key
Sign up at [NewsAPI](https://newsapi.org/) to obtain a free API key. Replace the placeholder in `project.py`:
```python
API_KEY = 'your_api_key_here'
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/morning-news.git
cd morning-news
```

### 2. Install Dependencies
The project requires several Python libraries. Install them using:
```bash
pip install -r requirements.txt
```
The `requirements.txt` file includes:
- `requests` (HTTP requests to fetch news)
- `rich` (for styled console output)
- `pyttsx3` (text-to-speech functionality)
- `pyfiglet` (ASCII art for headings)
- `pytest` (for testing)

## Usage

### Running the Program
Start the program by running:
```bash
python project.py
```
Follow the on-screen instructions to select a news category and choose whether to hear the news aloud. The program will fetch and display the top headlines based on your selection.

### Example Output
The program outputs a styled table of news articles, such as:
```
Today's Top Headlines
+----+--------------------+--------------------------------+----------------------------------------------+-----------------------------------+
| No | Source             | Title                          | Description                                  | URL                               |
+----+--------------------+--------------------------------+----------------------------------------------+-----------------------------------+
| 1  | BBC News           | Breaking News                 | Description of the news headline.            | http://example.com               |
```

### Testing the Program
Run the test suite to verify functionality:
```bash
pytest test_project.py
```
The test suite checks critical functions like title cleaning, category selection, and API response handling.

## Project Structure

### Files
- `project.py`: Main program containing all functionality.
- `test_project.py`: Test suite for verifying program correctness.
- `requirements.txt`: Lists dependencies for the project.

### Key Functions
- **`get_news`**: Fetches news articles from NewsAPI.
- **`clean_title`**: Cleans article titles by removing unnecessary text.
- **`display_news`**: Displays articles in a formatted table.
- **`read_news_aloud`**: Reads news aloud using text-to-speech.
- **`choose_category`**: Handles user input for news category selection.

## Notes
- Ensure a stable internet connection to fetch news.
- The program depends on the system's text-to-speech engine. Ensure it is configured correctly.
- If no news articles are available, the program will notify you.

## Future Improvements
- Adding support for multiple languages and local news.
- Scheduling the program to run automatically at a specific time each day.
- Enhancing error handling for network and API-related issues.

## Contributing
Feel free to fork the repository and submit pull requests to enhance functionality or fix bugs. Feedback and suggestions are welcome.

## License
This project does not currently have a license and is proprietary. If you wish to use or distribute this project, please contact the author for permission.

