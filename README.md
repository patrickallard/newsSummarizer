# newsSummarizer
Scrapes data from news articles, formats, chunks, and then organizes the text into pithy, bite-sized summaries.

### Installation and Packages
Create a new python virtual environment, then install the necessary packages outlined [here](https://github.com/patrickallard/newsSummarizer/files/11264397/requirements.txt)

### Running the Program

Activate python environment.

Navigate to the ```quotes_spider.py``` file and insert the desired URL in the ```start_urls``` property array. URL must be a Politico article, as the scraper bot can only fish text data from that news site. 

Then run
```
$ python3 main.py
```
