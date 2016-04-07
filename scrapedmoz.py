from bs4 import BeautifulSoup

import requests

foo = []

def recurseSearch(recurseURL):
	try:
		r = requests.get("http://"+recurseURL)
		data =  r.text
		soup=BeautifulSoup(data,"html.parser")
		for link in soup.find_all('a'):
			x = link.get('href')
			if str(x)[0] == '/':
				print("http://www.dmoz.org" + str(x))
				foo.append("dmoz.org" + str(x))
			else:
				print("http://www.dmoz.org/" + str(x))
				foo.append("dmoz.org/" + str(x))
	except requests.exceptions.ConnectTimeout as e:
		return

url=raw_input("Enter a website :")

r = requests.get("http://"+url)

data =  r.text
soup=BeautifulSoup(data,"html.parser")

for link in soup.find_all('a'):
	x = link.get('href')
	if str(x)[0] == '/':
		print("http://www.dmoz.org" + str(x))
		foo.append("dmoz.org" + str(x))
	else:
		print("http://www.dmoz.org/" + str(x))
		foo.append("dmoz.org/" + str(x))

while len(foo) > 0:
	recurseSearch(foo[0])
	foo.pop(0)