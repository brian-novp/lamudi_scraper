# import lxml.etree to parse sing xpath
from lxml import etree

# import pandas to save files to csv
import pandas as pd

# import glob to identify csv files
import glob



for i in range(1,51):
        with open(f".\export_lamudi\lamudi_solo_{i}.html", 'r', encoding="utf8") as hfile:
                parser = etree.HTMLParser()
                tree = etree.parse(hfile, parser)
                
                # === get general info using etree and XPATH ===
                # title
                title_obj = tree.xpath("//h3[@class='ListingCell-KeyInfo-title']/@title")
                
                # short description
                desc_obj = tree.xpath("//div[@class='ListingCell-shortDescription ']/text()")
                # result contain "\n" , clean using replace() method in a list comprehension
                desc_obj = [i.replace("\n", "") for i in desc_obj]
                  
                # area
                area_obj = tree.xpath("//span[@class='ListingCell-KeyInfo-address-text']/text()")
                area_obj = [i.replace("\n", "") for i in area_obj]
                 
                # === XPATH for properties' details ===
                
                # bedroom
                BR_obj = tree.xpath("//div[@class = 'ListingCell-AllInfo ListingUnit']/@data-bedrooms")
                
                # bathroom
                Bath_obj = tree.xpath("//div[@class='ListingCell-AllInfo ListingUnit']/@data-bathrooms")
                
                # land_size
                LS_obj = tree.xpath("//div[@class='ListingCell-AllInfo ListingUnit']/@data-land_size")
                 
                # building size
                BS_obj = tree.xpath("//div[@class='ListingCell-AllInfo ListingUnit']/@data-building_size")
                
                # price
                prices_obj = tree.xpath("//div[@class='ListingCell-AllInfo ListingUnit']/@data-price")
                
        # create dictionary to make a dataframe for each page scraped
        a = {'title': title_obj, 
        'desc': desc_obj, 
        'area': area_obj, 
        'bedroom':BR_obj,
        'bathroom': Bath_obj, 
        'land_size':LS_obj, 
        'building_size':BS_obj,
        'price_IDR_mio' :prices_obj}

        # create pandas dataframe based on the dictionary created
        df = pd.DataFrame(data=a)
        # save dataframe to csv using ";" as separator
        df.to_csv(f'./lamudi_csv/lamudi_{i}.csv', encoding='utf-8', index=False, header=True)
        # add print statement for process monitoring
        print(f"done processing lamudi_{i}.html, moving on to scrape next html")
        
# add print statement at the end of the whole loop for process monitoring        
print(f"Scraped {i} html in separate csvs, now concatting the csvs into a single csv")

# use glob to access csv files, store it in csv_files variable
csv_files = glob.glob('./lamudi_csv/*.csv')
# to check in terminal
print(csv_files) 

# concat all csvs detected in workspace folder using list comprehension
df_master = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
df_master.to_csv('./lamudi_csv/lamudi_master.csv', encoding='utf-8', index=False, header=True)
print(f"done processing {i} csv files and appending to single csv files")
print(df_master.info())