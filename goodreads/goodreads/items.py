# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# https://www.goodreads.com/list/show/702.Cozy_Mystery_Series_First_Book_of_a_Series
import scrapy


class GoodreadsItem(scrapy.Item):
    title = scrapy.Field()
    #comments = scrapy.Field()
    #rate = scrapy.Field()
    #noRatings = scrapy.Field()
    #noReviews = scrapy.Field()