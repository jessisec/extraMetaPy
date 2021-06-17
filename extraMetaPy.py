#!/usr/bin/env python3
# Title: extraMetaPy
# Author: Jessi
# Usage: ./extraMetaPy.py -d <domain> -o <output> -f <filedir> -l <results_limit> (Ex: ./extraMetaPy.py -d domain.com -o results.txt -f downloads/ -l 150)

import os
import argparse
import time
import urllib.request
from googlesearch import search
import colorama
from colorama import Fore, Style


# Define parser and arguments.
parser = argparse.ArgumentParser(description=f'extraMetaPy: The Python3 powered google dorking and metadata extracting tool. Presented by {Fore.MAGENTA}Jessi{Style.RESET_ALL}')

parser.add_argument('-d', '--domain', help=f'Target domain {Fore.RED}{Style.BRIGHT}REQUIRED{Style.RESET_ALL}', default='', required=True)
parser.add_argument('-o', '--output', help=f'Output file name {Style.DIM}OPTIONAL Defualt: extracted_metadata.txt{Style.RESET_ALL}', default='extracted_metadata.txt', required=False)
parser.add_argument('-f', '--filedir', help=f'Downloads directory {Style.DIM}OPTIONAL Default: file_downloads/{Style.RESET_ALL}', default='file_downloads/', required=False)
parser.add_argument('-l', '--limit', type=int, help=f'Results limit {Style.DIM}OPTIONAL Default: 100{Style.RESET_ALL}', default=100, required=False)

args = parser.parse_args()


# Set args to variables
domain = args.domain
output = args.output
filedir = args.filedir
limit = args.limit


# Create filedir if not exists
if not os.path.exists(filedir):
    os.makedirs(filedir)


# Coloroma print test
#print(f'{Fore.GREEN}[+] {Fore.WHITE}{domain}{Style.RESET_ALL}')
#print(f'{Fore.GREEN}{Style.BRIGHT}{limit}')


# Define coloroma colors
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
CYAN = Fore.CYAN
PINK = Fore.MAGENTA
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORM = Style.NORMAL
RST = Style.RESET_ALL


# Define fileTypes dictionary
fileTypes = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']


# Open urls.txt to write scraped urls to
f = open('urls.txt', 'a')


# Define primary functions
def dork(domain, ft): # Google Dork function
    query = 'site:' + domain + ' filetype:' + ft
    print(f'{GREEN}{BRIGHT}[+] {NORM}{WHITE}Dorking {BRIGHT}{domain}{RST} {WHITE}for {BRIGHT}{ft} {NORM}files{RST}')
    try:
        for result in search(query, num_results=limit):
            f.write(f'{result}\n')
    except:
        print(f'{RED}{BRIGHT}[X]{RST} {WHITE}Dork failed for: {BRIGHT}{ft}{RST}')
        print(f'{DIM}Failure is likely due to too many requests...')
        print(f'Try again later\n{RST}')


def download_url(url,filename): # Download files function
    try:
        r = urllib.request.urlretrieve(url,filename)
        print(f'{GREEN}{BRIGHT}[+]{NORM} {WHITE}Downloading: {BRIGHT}{url}{RST}')
    except urllib.error.HTTPError as exception:
        print(f'{RED}{BRIGHT}[x]{DIM} Download failed for:{RST} {WHITE}{url}{RST}')


#def extract_meta(file): # Extract metadata function


# Begin Google Dork task
print(f'{CYAN}{BRIGHT}[!] {NORM}{WHITE}Starting Google Dork task{RST}')
time.sleep(2)
for ft in fileTypes:
    dork(domain,ft)


# Close urls.txt file and count urls scraped
f.close()
urlsFile = open('urls.txt', 'r')
urlsCount = 0
urls = urlsFile.read()
urlsList = urls.split('\n')
for num in urlsList:
    if num:
        urlsCount += 1
print(f'{GREEN}{BRIGHT}[+] {NORM}{WHITE}Scraped {BRIGHT}{urlsCount}{NORM} URLs{RST}')
print(f'{GREEN}{BRIGHT}[+] {NORM}{WHITE}Scraped URLs saved in {BRIGHT}urls.txt{RST}')


# Begin file download task
print(f'\n{CYAN}{BRIGHT}[!] {NORM}{WHITE}Starting files download task{RST}')
time.sleep(2)
with open('urls.txt') as urlsFile:
    for i in urlsFile:
        url = i.rstrip()
        name = url.rsplit('/', 1)[1]
        filename = filedir + name
        download_url(url,filename)


# Count downloaded files
dirCount = 0
dirListing = os.listdir(filedir)
for num in dirListing:
    if num:
        dirCount += 1
print(f'{GREEN}{BRIGHT}[+] {NORM}{WHITE}Downloaded {BRIGHT}{dirCount}{NORM} files{RST}')
