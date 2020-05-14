# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    # allowed_domains = ['https://www.coursera.org/']
    start_urls = ['https://www.coursera.org//']

    def parse(self, response):
        self.log('Hello World! Scrapy Project')  