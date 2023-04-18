import os
import subprocess
from scrapy.crawler import CrawlerProcess
from scrap.tutorial.tutorial.spiders.quotes_spider import QuoteSpider

# TODO: 
# 1) increase usability by prompting the user to add URL to be scraped at CL
# 2) Cache text stream or save in files?
# 3) Website agnostic scraper?

# Run quotes_spider.py
process = CrawlerProcess()
process.crawl(QuoteSpider)
process.start()
# Run formatter.py
subprocess.run(["python", "formfix.py"])
# Run chunkAlgo.py
subprocess.run(["python", "chunkAlgo.py"])
# Run practiceLLM.py
subprocess.run(["python", "practiceLLM.py"])

# Gargabe Collection
os.remove('formattedData.txt')
os.remove('output.json')