import pyttsx3
from rich.console import Console
from rich.table import Table
import requests
import pyfiglet
import unicodedata

def get_news(category='general', country='us'):
    # Replace with your NewsAPI key
    API_KEY = 'your_api_key_here'
    BASE_URL = 'https://newsapi.org/v2/top-headlines'

    url = f"{BASE_URL}?category={category}&country={country}&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        print("Error fetching news")
        return None


def clean_title(title):
    # Normalize the title to ensure there are no unexpected Unicode characters
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')

    # Remove everything after the last hyphen (including the hyphen)
    if "-" in title:
        return title.rsplit(" - ", 1)[0]
    return title  # Return the title as is if there's no hyphen


def display_news(articles):
    console = Console()

    if not articles:
        print("No news found.")
        return

    # Use pyfiglet to create a large ASCII title
    title = pyfiglet.figlet_format("Today's Top Headlines")
    console.print(title)  # Print the large title

    # Create a table with an extra column for the source and URL
    table = Table(show_header=True)

    # Define table columns with fixed widths
    table.add_column("No.", style="cyan", width=4)  # Narrower "No." column
    table.add_column("Source", style="green", width=20)  # Adjust width as needed
    table.add_column("Title", style="yellow", width=40)  # Adjust width as needed
    table.add_column("Description", style="magenta", width=60)  # Adjust width as needed
    table.add_column("URL", style="blue", width=50)  # Add the URL column with some width

    # Add articles to the table
    for i, article in enumerate(articles, start=1):
        # Ensure title, description, source, and URL are not None
        title = article['title'] if article['title'] else ""
        description = article['description'] if article['description'] else ""
        source = article['source']['name'] if article.get('source') else "Unknown source"
        url = article['url'] if article.get('url') else "No URL"

        # Clean up the title to remove text after the last hyphen (if present)
        clean_article_title = clean_title(title)

        table.add_row(str(i), source, clean_article_title, description, url)

        # Add a separator line after each article
        table.add_row("-" * 80, "-" * 15, "-" * 40, "-" * 60, "-" * 50)

    # Display the table
    console.print(table)

def read_news_aloud(news):
    engine = pyttsx3.init()

    # Get the current rate of speech
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Set slower speech rate

    for i, article in enumerate(news, start=1):
        # Ensure title and description are not None
        title = article['title'] if article['title'] else ""
        description = article['description'] if article['description'] else ""

        # Check if the source exists
        source = article['source']['name'] if article.get('source') else "Unknown source"

        # Clean the title to remove the source if it appears at the end
        clean_article_title = clean_title(title)

        # Announce the article number first
        engine.say(f"Article {i}")

        # Announce the source
        engine.say(f"Source: {source}")

        # Prepare the news text without including the source in the article content
        text = clean_article_title + ". " + description

        # Read out the news text (no need to mention the source again)
        engine.say(text)

    engine.runAndWait()

def choose_category():
    print("Choose a news category:")
    print("1. General")
    print("2. Business")
    print("3. Technology")
    print("4. Sports")
    print("5. Health")
    print("6. Entertainment")

    choice = input("Enter the number of your choice: ")

    categories = {
        '1': 'general',
        '2': 'business',
        '3': 'technology',
        '4': 'sports',
        '5': 'health',
        '6': 'entertainment'
    }

    return categories.get(choice, 'general')

def main():
    print("Welcome to the Morning News Update!")
    category = choose_category()
    articles = get_news(category=category)

    if articles:
        display_news(articles)

        read_option = input("Do you want me to read the news aloud? (y/n): ")
        if read_option.lower() == 'y':
            read_news_aloud(articles)
        else:
            print("Have a great day!")
    else:
        print("No news available at the moment.")

if __name__ == '__main__':
    main()
