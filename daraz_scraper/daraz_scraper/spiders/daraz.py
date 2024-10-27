import scrapy

class DarazSpider(scrapy.Spider):
    name = "daraz"
    allowed_domains = ["daraz.com.bd"]
    start_urls = [
        "https://www.daraz.com.bd/catalog/?q=best+sellers"  # Example URL
    ]

    def parse(self, response):
        self.log(response.text)
        for product in response.css('.c2prKC'):  # Check the correct selector for product list
            yield {
                'name': product.css('.c16H9d::text').get(),
                'price': product.css('.c3gUW0::text').get(),
                'rating': product.css('.c3XbGZ::text').get(),
                'product_link': product.css('.c16H9d::attr(href)').get(),
            }

        # Follow pagination
        next_page = response.css('a.c3Y5Hf::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
