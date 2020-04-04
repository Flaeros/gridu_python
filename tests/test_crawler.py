import sys
sys.path.append("../griducrawler")

import unittest
import os

from scrapy.crawler import CrawlerProcess
from storage import get, change_storage
from crawler import Crawler


file_name = 'test_storage.txt'


class TestCrawler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.prepare_storage()

    def test_crawler(self):
        crawler = Crawler()

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            # 'LOG_LEVEL': 'DEBUG'
        })

        process.crawl(crawler)
        process.start()

        authors, articles = get(crawler.get_authors(), crawler.get_articles())
        self.assertTrue(len(authors) > 20)
        self.assertTrue(len(articles) > 20)

    @staticmethod
    def prepare_storage():
        if os.path.exists(file_name):
            os.remove(file_name)
        change_storage(file_name)


if __name__ == '__main__':
    unittest.main()
