import requests

def search_bing(query, api_key, count=5):
    endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count}

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        results = response.json().get("webPages", {}).get("value", [])
        return results
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt: 
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

if __name__ == "__main__":
    api_key = "YOUR_BING_API_KEY"
    
    while True:
        query = input("Enter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        search_results = search_bing(query, api_key)

        if search_results:
            for idx, result in enumerate(search_results, start=1):
                print(f"{idx}. {result['name']} - {result['url']}")
        else:
            print("No results found.")
