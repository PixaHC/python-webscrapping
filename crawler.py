from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

tag_pesquisa = "raspberry+pi"


def price_spider():
	page = 1
	while 1:
		html = urlopen("http://pt.aliexpress.com/wholesale?initiative_id=SB_20160419024658&site=bra&shipCountry=br&SearchText=%s&%d=1" % (tag_pesquisa, page))
		bsObj = BeautifulSoup(html,"html.parser")
		print('[ # ] ===================  %d' % page)

		nameList = bsObj.findAll("a",{"class":"history-item"})
		priceList = bsObj.findAll("span",{"class":"value"})

		for name in nameList:
			print(name.get_text())

		for price in priceList:
			print(price.get_text())
		page += 1

price_spider()

