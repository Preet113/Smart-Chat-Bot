import requests
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv
import os

# load_dotenv()

# my_password = os.getenv("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")

openai.api_key = os.getenv("Api_key")

def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            return text
        else:
            return None
    except Exception as e:
        print("Error while scraping:", str(e))
        return None

def ask_question(prompt, context):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Context: {context}\nQuestion: {prompt}\nAnswer:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# if __name__ == "__main__":
#     website_url = input("Enter the URL of the website you want to scrape: ")
#     website_text = scrape_website(website_url)

#     if website_text is not None:
#         while True:
#             question = input("Ask a question (or type 'exit' to quit): ")
#             if question.lower() == 'exit':
#                 break

#             answer = ask_question(question, website_text)
#             print("Answer:", answer)
#     else:
#         print("Failed to scrape the website.")