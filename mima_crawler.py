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

page_link = "https://www.mima.co.il/artist_letter.php?let=%D7%90"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

artists = page_content.find_all("a",attrs={"href":re.compile(r'^artist_page')})
for a in artists:
    print(a.text)
    print(a['href'])
