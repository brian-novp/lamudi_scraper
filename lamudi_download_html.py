# script download html pages at lamudi

# import playwright sync as automation browser
from playwright.sync_api import sync_playwright

# import time for time delay
import time

# import random for randomness in time delay
import random

# make a function to download pages that accept start to finish page and export location
def download_p( page_from=1, page_to=2, export_location='.'):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=35000)
        context = browser.new_context()
        page = context.new_page()

        for page_num in range(page_from, page_to+1):
            print('processing', f'https://www.lamudi.co.id/jual/jawa-tengah/surakarta-solo/rumah/?page={page_num}')
            page.goto(f'https://www.lamudi.co.id/jual/jawa-tengah/surakarta-solo/rumah/?page={page_num}', timeout=30000)
            # time.sleep(random.randint(10, 20)) >> use only if needed as a buffer
            page.wait_for_load_state('domcontentloaded')
            time.sleep(random.randint(4, 12))

            with open(f'{export_location}/lamudi_solo_{page_num}.html', 'w', encoding='utf-8') as f:
                      f.write(page.content())
            print(f'Success! html lamudi_solo page {page_num} is saved to ', export_location)
        context.close()
        browser.close()      
        
# if the file is called/executed, then perform download_p 
if __name__ == '__main__':
    export_location = './export_lamudi'
    download_p(page_from=4, page_to=50, export_location=export_location)


