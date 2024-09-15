# lamudi_scraper
contains .py file to download html pages from lamudi website (area specific) and another .py file to parse the downloaded html and extract the data needed using XPATH

## Motivation
Scraping directly to online web will create request that may spike the workload of the server, I do not want to put heavy load to the server, hence I create 2 separate py files. [lamudi_download_html.py](https://github.com/brian-novp/lamudi_scraper/blob/main/lamudi_download_html.py) to download html pages to local machine and [lamudi_scraper.py](https://github.com/brian-novp/lamudi_scraper/blob/main/lamudi_scraper.py) to extract data from offline html pages using XPATH selector, clean the data (remove quotes and newlines) and then save them to master csv file.
