import scrapy


class CoopsUKEvents(scrapy.Spider):
    name = 'coopsukevents'
    download_delay = 5
    start_urls = ['https://www.uk.coop/events-and-training/events-calendar?f%5B0%5D=event_organiser%3Acuk']

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.uk.coop/events-and-training/events-calendar?f%5B0%5D=event_organiser%3Acuk',
            callback=self.parse_list
        )

    def parse_list(self, response):
        for link in response.xpath("//article[contains(@class, 'node--type-event')]"):
            url = 'https://www.uk.coop' + link.xpath('section/span/h2/a').xpath('@href').extract()[0]
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
        next_page = response.xpath("//li[contains(@class, 'pager__item--next')]").xpath('a').xpath('@href').extract()
        if next_page:
            yield scrapy.Request(
                url='https://www.uk.coop/events-and-training/events-calendar' + next_page[0],
                callback=self.parse_list
            )

    def parse(self, response):

        url_bits = response.request.url.split("/")

        out = {
            'id': url_bits[5],
            'data': {
                'title': response.xpath("//h1").xpath('string(.)').extract()[0].strip(),
                'url': response.request.url,
                'description': response.xpath("//section[contains(@class, 'main-content')]").xpath('string(.)').extract()[0].strip(),
            }
        }

        meta_data = response.xpath("//h2[contains(text(), 'Event')]/../div[1]/div")
        for div in meta_data:
            div_content = div.xpath("string()").extract()[0].strip()
            if div_content.startswith("Start date / time"):
                bits = div_content[len("Start date / time"):].split("End date / time")
                out['data']['start'] = bits[0].strip()
                out['data']['end'] = bits[1].strip()
            elif div_content.startswith("Location"):
                out['data']['location'] = div_content[len("Location"):].strip()
            elif div_content.startswith("Price"):
                out['data']['price'] = div_content[len("Price"):].strip()
            elif div_content.startswith("Event type"):
                out['data']['event_type'] = div_content[len("Event type"):].strip()

        return out

