# -*- coding: utf-8 -*-
import sqlite3
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class OlxSqlitePipeline:

    def process_item(self, item, spider):

        tables = 'title, price, category, kind, engine, direction, plate, model, year, fuel, color, brand, km, gearbox, doors'
        values = ':title, :price, :category, :kind, :engine, :direction, :plate, :model, :year, :fuel, :color, :brand, :km, :gearbox, :doors'
        insert = f'insert into cars({tables}) values ({values})'

        self.conn.execute(insert, item)
        self.conn.commit()

        return item

    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "cars"'
        )
        try:
            value = next(result)
        except StopIteration as ex:
            create_table =  """
                create table cars(id integer primary key, 
                title text,
                price text,
                category text,
                kind text,
                engine text,
                direction text,
                plate text,
                model text,
                year text,
                fuel text,
                color text,
                brand text,
                km text,
                gearbox text,
                doors text)

            """.replace('\n', '')

            self.conn.execute(create_table)

    def open_spider(self, spider):
        # criar bando de dados e se conectando
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider(self, spider):
        # fechando o banco de dados
        self.conn.close()


class MongoPipeline:

    collection_name = 'cars'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
