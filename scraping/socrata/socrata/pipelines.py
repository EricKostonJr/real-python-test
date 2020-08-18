# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
from itemadapter import ItemAdapter


class SocrataPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('project.db')
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):
        self.cur.execute(
            "INSERT INTO data (text, url, views) VALUES(?,?,?)",
            (item['text'], item['url'], item['views'])
        )
        self.conn.commit()
        return item