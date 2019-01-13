from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import re
from facts.models import Artist,Song,Fact


class Command(BaseCommand):
    help = "Scrape mima.co.il and steal info"

    re_param = re.compile('=([0-9\W]*)')
    facts_re = re.compile("#CCFFCC|#EDF3FE")

    def get_sub_pages_from_link(self,link, re_sub_page_name):
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


    def get_facts(self,song_url):
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

    def handle(self, *args, **options):

        print("hello")
        # # Expense.objects.all().delete()
        #
        site_url = "https://www.mima.co.il/"

        letters_pages = self.get_sub_pages_from_link(site_url, re.compile(rf'^artist_letter'))
        print(len(letters_pages))
        artist_pages = []
        artist_re = re.compile(rf'^artist_page')
        for letter in letters_pages:
            artist_pages.extend(self.get_sub_pages_from_link(site_url + letter['link'], artist_re))
        print(len(artist_pages))
        # songs_pages = []
        song_re = re.compile(rf'^fact_page')
        i = 0
        for artist in artist_pages:
            print(i)
            i += 1
            ar = Artist.objects.create(
                full_name=ar['name'])
            ar.save()
            # artist['songs_list'] = get_sub_pages_from_link(site_url + artist['link'],song_re)
            songs = self.get_sub_pages_from_link(site_url + artist['link'], song_re)
            for song in songs:
                so = Song.objects.create(
                    title=song['name'],
                    artist=ar)
                so.save()
                facts = self.get_facts(song['link'])
                for fact in facts:
                    fa = Fact.objects.create(
                        publisher_name=fact['publisher'],
                        text=fact['text'],
                        song=so)

            # songs_pages.extend(get_sub_pages_from_link(site_url + artist['link'], song_re))
        # print(len(songs_pages))