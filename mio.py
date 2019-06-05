import requests
import pandas as pd

def df_web():
	url = 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table'
	html = requests.get(url).content
	df_list = pd.read_html(html, index_col=0, skiprows=2)
	df = df_list[1]
	df.reset_index(drop=True)
	df.columns = ['#Summer', 'Gold', 'Silver','Bronze','Total','#Winter','Gold.1','Silver.1','Bronze.1','Total.1','#Games','Gold.2','Silver.2','Bronze.2','CTotal']
	names_ids = df.index.str.split('\s\(')       # split the index by '('
	df.index = names_ids.str[0]                  # the [0] element is the country name (new index) 
	df['ID'] = names_ids.str[1].str[:3]          # the [1] element is the abbreviation or ID (take first 3 characters from that)
	df = df.drop('Totals')                       # Eliminates the las row calles 'Totals'
	df.index.name =''
	return df

def df_csv():
	df = pd.read_csv('./countries.csv', sep=',', names=['country', 'continent'],skiprows = 2)
	df.set_index(['country'], inplace=True)
	return df