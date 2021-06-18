# extraMetaPy
The Python3 powered google dorker and metadata extractor.  
Use Google Dorks against a target domain to scrape URLs containing common filetypes. Download files from scraped URLs. Extract metadata from files into an output file.  

### About
extraMetaPy has two main modes: Google Dork mode or URL list mode.  
Google Dork mode: Designated by setting the `-d (--domain)` argument to a valid domain name.
- In this mode, extraMetaPy will use Google Dorks to scan a domain for common file types, it will then scrape them into a file called 'urls.txt', then it will proceed to download all of the files, unless `-nd y (--nodownload y)` is set, finally, it will extract all of the metadata from the files into an output file.  

URL list mode: Designated by setting the `-u (--urllist)` argument to a valid list of URLs.  
- In this mode, extraMetaPy will read an existing list of URLs, skipping Google Dorks as a result, then proceed with the standard process of downloading the files and extracting their metadata.  

Errors?  
- extraMetaPy creates a log file called `empy.log` by default, it will timestamp relative logs and information into the log, along with exceptions.  
- extraMetaPy will attempt to download a file a maximum of three times before it counts it as failed, but it will continue down the list and download the rest of the files.  
- extraMetaPy will also print out an error if an issue is detected when attempting a Google Dork, this error is usually not because of the tool, but rather because Google has detected you have been making too many requests.  

#### Usage
```bash
git clone https://github.com/jessisec/extraMetaPy
cd extraMetaPy
pip3 install -r requirements.txt

./extraMetaPy.py -d <domain>
Ex: ./extraMetaPy.py -d yahoo.com -o yahoo_meta.txt -f files/ -l 50
```


#### Screenshots  
![image](https://user-images.githubusercontent.com/28818635/122490794-c61e4b80-cfb0-11eb-8bc0-7274209167d9.png)
  
![image](https://user-images.githubusercontent.com/28818635/122491092-61afbc00-cfb1-11eb-860e-76ba15c84c78.png)

![image](https://user-images.githubusercontent.com/28818635/122491264-a63b5780-cfb1-11eb-8676-4839adeec751.png)
