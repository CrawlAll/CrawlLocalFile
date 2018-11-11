# -*- coding: utf-8 -*-
import re
import scrapy
from CrawlLocalFile.item import CrawlLocalFileItem


class LocalFileSpider(scrapy.Spider):
	name = 'local_file'
	start_urls = ['http://xx.com/']
	base_url = r'file:///c:\Users\Administrator\Desktop\dev\2635660\48242_odds_2635660_'

	def start_requests(self):
		for offset in range(1, 24403):
			url = self.base_url + str(offset) + '.xml'
			yield scrapy.Request(url=url, callback=self.parse, errback=self.errFunc)

	def parse(self, response):
		text = response.text
		item = CrawlLocalFileItem()
		try:
			# event_id
			item['event_id'] = re.findall('<EventID>(.*?)</EventID>', text)[0]
			# 比赛开始时间
			item['start_date'] = re.findall('<StartDate>(.*?)</StartDate>', text)[0]
			# 最后更新时间
			item['last_update'] = re.findall('<LastUpdate>(.*?)</LastUpdate>', text)[0]
			# SportID
			item['sport_id'] = re.findall('Basketball">(.*?)</SportID>', text)[0]
			# LeagueID
			item['league_id'] = re.findall('<LeagueID Name="NBA">(.*?)</LeagueID>', text)[0]
			# 位置的ID
			item['location_id'] = re.findall('<LocationID Name="United States">(.*?)</LocationID>', text)[0]
			# 主队名字
			item['home_team'] = re.findall('<HomeTeam(.*?)Name="(.*?)" />', text)[0][1]
			# 客队名字
			item['away_team'] = re.findall('<AwayTeam ID="(.*?)" Name="(.*?)" />', text)[0][1]
			# 状态
			item['status'] = re.findall('<Status>(.*?)</Status>', text)[0]
			# 投注选项
			bet = re.findall('bet="(.*?)"', text)
			item['bet1'] = bet[0]
			item['bet2'] = bet[1]
			# 开始价格
			item['start_price'] = re.findall('<startPrice>(.*?)</startPrice>', text)[0]
			# 当前价格
			currentPrice = re.findall('currentPrice="(.*?)"', text)
			item['current_price1'] = currentPrice[0]
			item['current_price2'] = currentPrice[1]
			# line
			line = re.findall('line="(.*?)"', text)
			item['line1'] = line[0]
			item['line2'] = line[1]
			# BaseLine
			BaseLine = re.findall('BaseLine="(.*?)"', text)
			# 该字段可能不存在
			item['base_line1'], item['base_line2'] = BaseLine if BaseLine else None, None

			yield item

		except Exception as e:
			self.logger.error(e)

	def errFunc(self, failure):
		self.logger.error(failure)
