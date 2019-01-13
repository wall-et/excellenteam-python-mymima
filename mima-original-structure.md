# Original Website Structure: mima.co.il

## Pages
* Home page: https://www.mima.co.il/
* Artists by letter page: https://www.mima.co.il/artist_letter.php?let=xxx
* Songs by letter page: https://www.mima.co.il/song_letter.php?let=xxx
* Single artist page: https://www.mima.co.il/artist_page.php?artist_id=xxx
* Single song page: https://www.mima.co.il/fact_page.php?song_id=xxx
* Search all page: https://www.mima.co.il/search_result.php


## Entities and Relationships

### Artist
* artist_id (INT PRIMARY KEY)
* full_name (VARCHAR)

### Song
* song_id (INT PRIMARY KEY)
* artist_id (INT)
* title (VARCHAR)

### Fact
* fact_id (INT PRIMARY KEY)
* song_id (INT)
* text (TEXT)
* publisher_name (VARCHAR)
