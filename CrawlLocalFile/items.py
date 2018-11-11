# -*- coding: utf-8 -*-
import scrapy


class CrawlLocalFileItem(scrapy.Item):
	# event_id
	event_id = scrapy.Field()
	# 比赛开始时间
	start_date = scrapy.Field()
	# 最后更新时间
	last_update = scrapy.Field()
	# sport_id
	sport_id = scrapy.Field()
	# league_id
	league_id = scrapy.Field()
	# 位置的ID
	location_id = scrapy.Field()
	# 主队名字
	home_team = scrapy.Field()
	# 客队名字
	away_team = scrapy.Field()
	# 状态
	status = scrapy.Field()
	# 投注选项
	bet1 = scrapy.Field()
	bet2 = scrapy.Field()
	# 开始价格
	start_price = scrapy.Field()
	# 当前价格
	current_price1 = scrapy.Field()
	current_price2 = scrapy.Field()
	# line
	line1 = scrapy.Field()
	line2 = scrapy.Field()
	# base_line
	base_line1 = scrapy.Field()
	base_line2 = scrapy.Field()
