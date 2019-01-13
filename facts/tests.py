from django.test import TestCase
from facts.models import Artist, Song, Fact


class FactsTestCase(TestCase):

    def setUp(self):
        Artist.objects.create(full_name="Adam Lambert")
        Artist.objects.create(full_name="My Chemical Romance")
        Artist.objects.create(full_name="FT Island")
        Artist.objects.create(full_name="Radiohead")
        Artist.objects.create(full_name="The Script")

        Song.objects.create(title="Whataya Want From Me", artist=Artist.objects.get(full_name="Adam Lambert"))
        Song.objects.create(title="Ghost Town", artist=Artist.objects.get(full_name="Adam Lambert"))
        Song.objects.create(title="Sure Fire Winner", artist=Artist.objects.get(full_name="Adam Lambert"))
        Song.objects.create(title="Welcome To The Black Parade", artist=Artist.objects.get(full_name="My Chemical Romance"))
        Song.objects.create(title="I Wish", artist=Artist.objects.get(full_name="FT Island"))
        Song.objects.create(title="Take Me Now", artist=Artist.objects.get(full_name="FT Island"))


        Fact.objects.create(text="The bridge is really good",
                            song=Song.objects.get(title="Ghost Town"))
        Fact.objects.create(publisher_name="sasaeng fan",
                            text="Beside this song all the songs in the albom were composed by the band members",
                            song=Song.objects.get(title="I Wish"))
        Fact.objects.create(publisher_name="kim min gyo",
                            text="the bridge has spanish guitars",
                            song=Song.objects.get(title="Take Me Now"))
        Fact.objects.create(text="I like this song",
                            song=Song.objects.get(title="I Wish"))
        Fact.objects.create(publisher_name="chris fan",
                            text="First song after \"American Idol\"",
                            song=Song.objects.get(title="Whataya Want From Me"))


    def test_insertion_totals(self):
        self.assertEqual(Artist.objects.count(), 5)
        self.assertEqual(Song.objects.count(), 6)
        self.assertEqual(Fact.objects.count(), 5)

    def test_insertion_singles(self):
        self.assertEqual(Artist.objects.get(full_name="The Script").__str__(), "The Script")
        self.assertEqual(Song.objects.get(title="I Wish").__str__(), "I Wish")
        self.assertEqual(Fact.objects.get(publisher_name="sasaeng fan").__str__(),
                         "Beside this song all the songs in the albom were composed by the band members")
#