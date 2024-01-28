from csv_reader import read_csv_file
from scrapper import scrap

links = read_csv_file('data.csv')

for link in links:
    scrap(link)