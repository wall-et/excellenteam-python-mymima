from bs4 import BeautifulSoup
import requests
import re
from facts import models

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


# def get_artists_by_letters_pages(main_page_link,letter_page_name):
#     # page_link = "https://www.mima.co.il/"
#     page_response = requests.get(main_page_link, timeout=5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")
#
#     letters = page_content.find_all("a", attrs={"href": re.compile(rf'^{letter_page_name}')})
#     for let in letters:
#         # print(a.text)
#         # print(a['href'])
#         letters_pages.add(let['href'])

# def get_artist_from_letter_page(letter_link,artist_page_name):
#     page_response = requests.get(letter_link, timeout=5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")
#
#     artists = page_content.find_all("a",attrs={"href":re.compile(rf'^{artist_page_name}')})
#     for a in artists:
#         # print(a.text)
#         artists_names.add(a.text)
#         artists_pages[re.search('=([0-9]*)',a['href']).group(1)] = a['href']
#         # artists_pages.add(,(a['href']))
        # print(a['href'])
        # print(re.search('=([0-9]*)',a['href']).group(1))

# def get_sub_pages_from_link(link,sub_page_name):
#     info = []
#     page_response = requests.get(link, timeout=5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")
#     pages = page_content.find_all("a", attrs={"href": re.compile(rf'^{sub_page_name}')})
#     for i,page in enumerate(pages):
#         info.append({
#             'name':page.text,
#             'link':page['href'],
#             'get_param': re.search('=([0-9\W]*)', page['href']).group(1)
#         })
#         # print(page)
#     return info

re_param = re.compile('=([0-9\W]*)')

def get_sub_pages_from_link(link,re_sub_page_name):
    info = []
    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    pages = page_content.find_all("a", attrs={"href": re_sub_page_name})
    for page in pages:
        info.append({
            'name':page.text,
            'link':page['href'],
            # 'get_param': re_param.match(page['href']).group(1)
        })
        # print(page)
    return info


site_url = "https://www.mima.co.il/"

letters_pages = get_sub_pages_from_link(site_url,re.compile(rf'^artist_letter'))
print(len(letters_pages))
artist_pages = []
artist_re = re.compile(rf'^artist_page')
for letter in letters_pages:
    artist_pages.extend(get_sub_pages_from_link(site_url + letter['link'],artist_re))
print(len(artist_pages))
songs_pages = []
song_re = re.compile(rf'^fact_page')
i = 0
for artist in artist_pages:
    # print(i)
    # i+=1
    artist['songs_list'] = get_sub_pages_from_link(site_url + artist['link'],song_re)
    # songs_pages.extend(get_sub_pages_from_link(site_url + artist['link'],song_re))
print(len(songs_pages))