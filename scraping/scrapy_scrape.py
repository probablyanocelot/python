import scrapy

class PoESpider(scrapy.Spider):
    name = 'poe_spider'
    start_urls = ['https://poe.trade/']

    # def parse(self, response):
    #     TBODY_SELECTOR = '.tbody'
    #     for tbody in response.css(TBODY_SELECTOR):

    #         DATA_SELECTOR = 'tbody ::text'
    #         NAME_SELECTOR = 'h1 ::text'
    #         PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'




    def parse(self, response):
        for item in response.css('.tbody'):
            yield {
                'results': item.xpath('div').get(),
                # 'tbody': quote.xpath('span/small/text()').get(),
                # 'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('input.search.button.value ').get()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

            # data-buyout="1 jewellers"
            # data-ign="Xylth"
            # data-league="Ultimatum"
            # data-name="Vaal Power Siphon"
            # data-tab="Sell"

            #     data-level="1"
            #     data-quality="0"


            #     data-x="2"
            #     data-y="11"


            # data-opt=
            # MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            # IMAGE_SELECTOR = 'img ::attr(src)'
            # yield {
            #     'name': brickset.css(TBODY_SELECTOR).extract_first(),
            #     'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            #     # 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
            #     'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            # }

        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )
        
        # SEARCH_PAGE_SELECTOR = '.search.button a ::attr(href)'
        # submit = response.css(SEARCH_PAGE_SELECTOR).extract_first()
        # if submit:
        #     yield scrapy.Request(
        #         response.urljoin(submit),
        #         callback=self.parse
        #     )
    # https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3.v