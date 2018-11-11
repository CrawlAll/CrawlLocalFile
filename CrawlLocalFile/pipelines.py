# -*- coding: utf-8 -*-
import json


class CrawlLocalFilePipeline(object):
	def __init__(self):
		self.filename = open('Odds.json', 'w')

	def process_item(self, item, spider):
		# 中文默认使用ascii码来存储，禁用后默认为Unicode字符串
		text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
		self.filename.write(text.encode("utf-8"))
		return item

	def close_spider(self, spider):
		self.filename.close()
