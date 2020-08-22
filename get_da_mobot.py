from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import time
import re


def find_mobot_links():

	alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	for letter in alphabet_list:
		file_name = "link_list_" + letter + ".csv"
		g = open("mobot_entries/" + file_name, 'w')
		
		url = "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderListResults.aspx?letter=" + letter

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		for link in soup.findAll('a', id=lambda x: x and x.startswith("MainContentPlaceHolder_SearchResultsList_TaxonName_")):
			g.write(link.get('href') + "\n")
		g.close()

def scrape_and_save_mobot_links():

	alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	for letter in alphabet_list:
		file_name = "link_list_" + letter + ".csv"

		with open("./mobot_entries/" + file_name, 'r') as f:
			for link_path in f:
				url = "https://www.missouribotanicalgarden.org" + link_path

				html_page = requests.get(url)
				http_encoding = html_page.encoding if 'charset' in html_page.headers.get('content-type', '').lower() else None
				html_encoding = EncodingDetector.find_declared_encoding(html_page.content, is_html=True)
				encoding = html_encoding or http_encoding
				soup = BeautifulSoup(html_page.content, from_encoding=encoding)

				file_name = str(soup.title.string).replace("  - Plant Finder", "")
				file_name = re.sub(r'\W+', '', file_name)
	
	
				g = open("mobot_entries/scraped_results/" + file_name + ".txt", 'w')
				g.write(str(soup.title.string).replace("  - Plant Finder", "") + "\n")
				g.write(str(soup.find("div", {"class": "row"})))
				g.close()
	
				print("finished " + file_name)
	
			f.close()
			time.sleep( 5 )

if __name__ == '__main__':

    
    #Here is where we FINALLY check out the MOBOT's website

    #Note that the MOBOT Plant Finder has its webpages sorted in differnt ways to make it searchable. This includes an alphabetical list of webpages with links to all the pages.
    #Each list of links is accessed with the same address patter "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderListResults.aspx?letter=<LETTER>"
    #So we will take every letter, insert it into this pattern, and grab the information of every webpage listed in that link list.

    find_mobot_links()

    #Once we have all the links, we will grab all the content from their webpages. With any possible content we could want from MOBOT in one go, we don't have to constantly bother their servers for data.

    scrape_and_save_mobot_links()
