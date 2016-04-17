# -*- coding: utf-8 -*-
import scrapy 
from scrapy import log
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader

from ..items import CrawaliItem

class AliexpressSpider(scrapy.Spider):
    name = "aliexpress"
    allowed_domains = ['pt.aliexpress.com']
    start_urls = ['http://pt.aliexpress.com/wholesale?catId=0&initiative_id=SB_20160417090024&SearchText=raspberrypy']
    	
    def parse(self, response):
    	ali_urls = self.get_ali_urls(response)
    	for ali_url in ali_urls:
 			yield Request(ali_url, callback=self.parse_ali)

  	def get_ali_urls(self, response):
  		hxs = HtmlXPathSelector(response)
        for path in hxs.select('//*[@id="hs-below-list-items"]/li[1]/div').extract():
        	protocol = 'http://'
        	domain = self.allowed_domains[0]
        	yield protocol + domain + path

    def parse_ali(self, response):
    	hxs = XPathItemLoader(item=CrawaliItem(), response=response)
    	loader.add_xpath('item_product_title','//*[@id="hs-below-list-items"]/li[1]/div/div[2]/h3/a/text()')
    	loader.add_xpath('item_product_price','//*[@id="hs-below-list-items"]/li[1]/div/div[2]/span/span[1]')
    	loader.add_xpath('item_product_stars','//*[@id="hs-below-list-items"]/li[1]/div/div[2]/div[2]/span[1]')

    	return loader.load_item()