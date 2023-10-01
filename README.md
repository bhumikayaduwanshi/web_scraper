# web_scraper

This projects aims at extracting articles from website "https://www.lawinsider.in"

### Tasks performed in the script:
1. Pagination till page 5.
2. Extraction of article links from all 5 pages.
3. Extraction of article content from each link.
4. Save the extracted data in json file with title as key and its content as value.

### To use this script simply follow the below instructions:
1. Clone the repo
2. Run below command in your project folder:
```"pip install -r requirements.txt"```
3. Finally execute the script:
```python3 scraper.py```