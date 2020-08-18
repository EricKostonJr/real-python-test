# -*- coding: utf-8 -*-
import scrapy


class HackernewsItem(scrapy.Item):
	title = scrapy.Field()
	url = scrapy.Field()