from bs4 import BeautifulSoup
import atexit
import requests

foo = []
fooMain = []
count = 0
target = open("database.txt", 'w')

def exit_handler():
	target.close()
	global count
	print(count)
	#This will close the file before the python program exits

atexit.register(exit_handler)

def checkURL(candidateURL):
	if "search" not in candidateURL and "?" not in candidateURL and "dmoz" not in candidateURL:
		return 1
	else:
		return 0

def recurseSearch(recurseURL):
	try:
		r = requests.get("http://"+recurseURL)
		data =  r.text
		soup=BeautifulSoup(data,"html.parser")
		for link in soup.find_all('a'):
			x = link.get('href')
			if str(x)[0] == '/':
				# print("http://www.dmoz.org" + str(x))
				foo.append("dmoz.org" + str(x))
			elif str(x).startswith("http"):
				if x not in fooMain:
					if checkURL(x):
						print(x)
						fooMain.append(x)
						target.write(x)
						target.write("\n")
						global count
						count+=1
			else:
				# print("http://www.dmoz.org/" + str(x))
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
		# print("http://www.dmoz.org" + str(x))
		foo.append("dmoz.org" + str(x))
	elif str(x).startswith("http"):
		if x not in fooMain:
			if checkURL(x):
				print(x)
				fooMain.append(x)
				target.write(x)
				target.write("\n")
				global count
				count+=1
	else:
		# print("http://www.dmoz.org/" + str(x))
		foo.append("dmoz.org/" + str(x))

while len(foo) > 0:
	try:
		recurseSearch(foo[0].encode('utf-8'))
		# print(foo[0].encode('utf-8'))
		foo.pop(0)
	except:
		foo.pop(0)