import scrapy, json

# inherits all of the properties and methods of the 'Spider' class
class QuoteSpider(scrapy.Spider):
    # names the spider
    # must be unique across all projects
    def __init__(self):
        self.processed_data = set()
    name = "quotes"
    start_urls = [
        'https://www.politico.com/news/2023/04/17/kevin-mccarthy-wall-street-debt-limit-00092324'
    ]
    # returns parsed data as dicts
    # scrapy's default callback method, which is called for requests w/o explicitly assigned callback
    # similar to java, .get() unpacks a JSON object, allowing you to interact with individual parts similar to a 
    # dictionary
    def parse(self, response):
        divs = response.xpath('//div')
        for para in divs.xpath('.//p[normalize-space(@class)="story-text__paragraph"]'):
            data = para.get()
            if data not in self.processed_data:
                self.processed_data.add(data)
                yield {
                    'text': data,
                }
        # Write items to output file
        with open("output.json", 'w') as f:
            for item in self.processed_data:
                f.write(json.dumps(item) + '\n')


    
