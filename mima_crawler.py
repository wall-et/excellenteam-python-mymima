from bs4 import BeautifulSoup
import requests
import re

# artist_collection = set()
# page_link = "https://www.mima.co.il/artist_page.php?artist_id=19"
# page_response = requests.get(page_link, timeout=5)
# page_content = BeautifulSoup(page_response.content, "html.parser")
#
# paragraphs = page_content.find_all("p")
# for p in paragraphs:
#     artist_name = p.find("font",attrs={"size":"+5"})
#     if artist_name:
#         print(artist_name.text)
#         artist_collection.add(artist_name.text)

# page_link = "https://www.mima.co.il/artist_letter.php?let=%D7%90"
# page_response = requests.get(page_link, timeout=5)
# page_content = BeautifulSoup(page_response.content, "html.parser")
#
# artists = page_content.find_all("a",attrs={"href":re.compile(r'^artist_page')})
# for a in artists:
#     print(a.text)
#     print(a['href'])


def get_artists_by_letters_pages(main_page_link,letter_page_name):
    # page_link = "https://www.mima.co.il/"
    page_response = requests.get(main_page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    letters = page_content.find_all("a", attrs={"href": re.compile(rf'^{letter_page_name}')})
    for let in letters:
        # print(a.text)
        # print(a['href'])
        letters_pages.add(let['href'])

def get_artist_from_letter_page(letter_link,artist_page_name):
    page_response = requests.get(letter_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    artists = page_content.find_all("a",attrs={"href":re.compile(rf'^{artist_page_name}')})
    for a in artists:
        # print(a.text)
        artists_names.add(a.text)
        artists_pages[re.search('=([0-9]*)',a['href']).group(1)] = a['href']
        # artists_pages.add(,(a['href']))
        # print(a['href'])
        # print(re.search('=([0-9]*)',a['href']).group(1))

site_url = "https://www.mima.co.il/"
letters_pages = set()
artists_pages = dict()
artists_names = set()
get_artists_by_letters_pages(site_url,"artist_letter")
for let in letters_pages:
    get_artist_from_letter_page(site_url + let,"artist_page")
print(len(artists_pages))
print(len(artists_names))