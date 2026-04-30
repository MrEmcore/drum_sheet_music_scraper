import requests
from bs4 import BeautifulSoup

def main(artist):
    r = requests.get('https://thedrumninja.com/drum-transcriptions/')
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')

    l = []
    cl = []

    for tag in soup('a'):
        l.append(tag.attrs.get('href'))

    for link in l:
        if link is not None and artist in link:
            cl.append(link)

    if len(cl) > 0:
        for item in cl:
            print(item)
    else:
        print("Could not find any matching objects")


if __name__ == "__main__":
    user_input = input('Please enter a band: ')

    main(user_input.lower().replace(" ", "-"))