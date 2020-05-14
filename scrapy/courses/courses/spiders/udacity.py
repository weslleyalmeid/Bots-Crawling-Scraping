# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://www.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("//div[@class='card-wrapper is-collapsed']")
        for div in divs:
            link = div.xpath('.//h3/a')
            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()
            # yield {
            #     'title': title,
            #     'href' : href
            # }
            yield scrapy.Request(
                url='https://www.udacity.com%s' % href,
                callback= self.parse_detail
            )


    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        lis = response.xpath('//div[@class="contain nd-overview"]/ul/li')
        estimated = lis[0].xpath('./h5/text()').extract_first()
        requisites = lis[2].xpath('.//h5/text()').extract_first()
        yield {
            'title': title,
            'estimated': estimated,
            'requisites': requisites,
        }
