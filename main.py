import requests
from bs4 import BeautifulSoup


def main(artist):
    r = requests.get('https://thedrumninja.com/drum-transcriptions/')
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')

    l = [tag.attrs.get('href') for tag in soup('a')]
    cl = [link for link in l if link is not None and artist in link]

    if len(cl) > 0:
        for item in cl:
            print(item)
        download(cl)
    else:
        print("No matches found")
        quit()

def download(list_of_songs):
    song_choice = input("Would you like to download a song?: ").lower().replace(" ", "-")
    if song_choice.lower() != "no":
        for item in list_of_songs:
            if song_choice in item:
                file_name = f"{song_choice}.pdf"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/91.0.4472.124 Safari/537.36'
                }
                try:
                    response = requests.get(item, headers=headers)
                    response.raise_for_status()
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded {file_name}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                pass
    else:
        quit()


if __name__ == "__main__":
    user_input = input('Please enter a band: ')
    main(user_input.lower().replace(" ", "-"))
