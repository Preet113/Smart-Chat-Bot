# scrape_data.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information from the webpage
            # For example, let's extract all the text within paragraph tags
            paragraphs = soup.find_all('p')
            extracted_data = [paragraph.text for paragraph in paragraphs]

            return extracted_data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error while scraping: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    website_url = input("Enter the URL of the website you want to scrape: ")
    scraped_data = scrape_website(website_url)

    if scraped_data:
        for i, data in enumerate(scraped_data, 1):
            print(f"Paragraph {i}: {data}")
    else:
        print("Failed to scrape the website.")
