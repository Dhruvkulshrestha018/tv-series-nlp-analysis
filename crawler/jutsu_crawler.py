import scrapy
from bs4 import BeautifulSoup

class NarutoJutsuSpider(scrapy.Spider):
    name = 'naruto_jutsu'
    start_urls = [
        'https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu'
    ]

    def parse(self, response):
        for href in response.css('.smw-columnlist-container a::attr(href)').getall():
            full_url = response.urljoin(href)
            yield scrapy.Request(full_url, callback=self.parse_jutsu)

        next_page = response.css('a.mw-nextlink::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_jutsu(self, response):
        jutsu_name = response.css("span.mw-page-title-main::text").get()
        div_html = response.css("div.mw-parser-output").get()
        soup = BeautifulSoup(div_html, 'html.parser')

        jutsu_type = ""
        aside = soup.find('aside')
        if aside:
            for cell in aside.find_all('div', {'class': 'pi-data'}):
                label = cell.find('h3')
                if label and 'Classification' in label.text:
                    jutsu_type = cell.find('div').text.strip()
            aside.decompose()

        jutsu_description = soup.text.strip()
        jutsu_description = jutsu_description.split('Trivia')[0].strip()

        yield {
            'jutsu_name': jutsu_name.strip() if jutsu_name else None,
            'jutsu_type': jutsu_type,
            'jutsu_description': jutsu_description
        }
