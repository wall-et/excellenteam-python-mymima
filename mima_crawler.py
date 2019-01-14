from bs4 import BeautifulSoup
import requests
import re
# from mymima import settings


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


def get_sub_pages_from_link(link, re_sub_page_name):
    info = []
    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    pages = page_content.find_all("a", attrs={"href": re_sub_page_name})
    for page in pages:
        info.append({
            'name': page.text,
            'link': page['href'],
            # 'get_param': re_param.match(page['href']).group(1)
        })
        # print(page)
    return info


facts_re = re.compile("#CCFFCC|#EDF3FE")


def get_facts(song_url):
    page_response = requests.get(song_url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    facts = page_content.find_all("tr", attrs={"bgcolor": facts_re})
    clean_facts = []
    for fact in facts:
        # print(fact.text)
        clean_facts.append({
            'text': fact.text,
            'publisher': fact.find("font").text if fact.find("font") else None
        })
    return clean_facts


site_url = "https://www.mima.co.il/"

# letters_pages = get_sub_pages_from_link(site_url, re.compile(rf'^artist_letter'))
# print(len(letters_pages))
# artist_pages = []
# artist_re = re.compile(rf'^artist_page')
# for letter in letters_pages:
#     artist_pages.extend(get_sub_pages_from_link(site_url + letter['link'], artist_re))
# print(len(artist_pages))
# songs_pages = []
# song_re = re.compile(rf'^fact_page')
# i = 0
# for artist in artist_pages:
#     print(i)
#     i += 1
#     ar = models.Artist.objects.create(
#         full_name=ar['name'])
#     ar.save()
#     # artist['songs_list'] = get_sub_pages_from_link(site_url + artist['link'],song_re)
#     songs = get_sub_pages_from_link(site_url + artist['link'], song_re)
#     for song in songs:
#         so = models.Song.objects.create(
#             title=song['name'],
#             artist=ar)
#         so.save()
#         facts = get_facts(song['link'])
#         for fact in facts:
#             fa = models.Fact.objects.create(
#                 publisher_name=fact['publisher'],
#                 text=fact['text'],
#                 song=so)
#
#     songs_pages.extend(get_sub_pages_from_link(site_url + artist['link'], song_re))
# print(len(songs_pages))


facts_re = re.compile("#CCFFCC|#EDF3FE")

song_url = "https://mima.co.il/fact_page.php?song_id=25"
page_response = requests.get(song_url, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
facts = page_content.find_all("tr", attrs={"bgcolor": facts_re})
inner_text_re = re.compile("<td>(.*)<br\/>")
font_text_re = re.compile('<font.* נכתב ע"י (.*) <\/')
for fact in facts:
    # f = fact
    # print(fact)
    f = inner_text_re.search(repr(fact)).group(1)
    # f = font_text_re.search(repr(fact))
    # f1 = re.match(inner_text_re,f)
    # print(f)
    print({
        'text':inner_text_re.search(repr(fact)).group(1),
        'publisher':font_text_re.search(repr(fact)).group(1) if font_text_re.search(repr(fact)) else None
     })
