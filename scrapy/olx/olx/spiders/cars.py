# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    start_urls = ['http://pr.olx.com.br/?q=carros/']

    def parse(self, response):
        # items = response.xpath('//ul[@class="sc-1fcmfeb-1 iptkoI"]/li[@class="sc-1fcmfeb-2 ggOGTJ"]')
        items = response.xpath('//ul[@class="sc-1fcmfeb-1 iptkoI"]/li/a')

        self.log(len(items))

        for item in items:
            url = item.xpath('./@href').extract_first()
            yield scrapy.Request(url= url, callback=self.parse_detail)

        next_page = response.xpath('//a[@data-lurker-detail="next_page"]/@href')

        if next_page:
            self.log(f'Next Page: {next_page.extract_first()} \n\n\n\n\n\n')
            yield scrapy.Request(url= next_page.extract_first(), callback= self.parse)

    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        price = response.xpath('//h2[@class="sc-ifAKCX sc-1leoitd-0 buyYie"]/text()').extract_first()
        category = response.xpath('//span[contains(text(), "Categoria")]/following-sibling::a/text()').extract_first()
        kind = response.xpath('//span[contains(text(), "Tipo de veículo")]/following-sibling::span/text()').extract_first()
        engine = response.xpath('//span[contains(text(), "Potência do motor")]/following-sibling::span/text()').extract_first()
        direction = response.xpath('//span[contains(text(), "Direção")]/following-sibling::span/text()').extract_first()
        plate = response.xpath('//span[contains(text(), "Final de placa")]/following-sibling::span/text()').extract_first()
        model = response.xpath('//span[contains(text(), "Modelo")]/following-sibling::a/text()').extract_first()
        year = response.xpath('//span[contains(text(), "Ano")]/following-sibling::a/text()').extract_first()
        fuel = response.xpath('//span[contains(text(), "Combustível")]/following-sibling::a/text()').extract_first()
        color = response.xpath('//span[contains(text(), "Cor")]/following-sibling::span/text()').extract_first()
        brand = response.xpath('//span[contains(text(), "Marca")]/following-sibling::a/text()').extract_first()
        km = response.xpath('//span[contains(text(), "Quilometragem")]/following-sibling::span/text()').extract_first()
        gearbox = response.xpath('//span[contains(text(), "Câmbio")]/following-sibling::span/text()').extract_first()
        doors = response.xpath('//span[contains(text(), "Portas")]/following-sibling::span/text()').extract_first()

        yield{
            'title': title,
            'price': price,
            'category': category,
            'kind': kind,
            'engine': engine,
            'direction': direction,
            'plate': plate,
            'model': model,
            'year': year,
            'fuel': fuel,
            'color': color,
            'brand': brand,
            'km': km,
            'gearbox': gearbox,
            'doors': doors
        }
