from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import requests
import time

valid = 0
pages = int(input("From what page do you want to start?"))
while(valid != 1):
	t=0
	r ='http://betweenfailures.com/comics1/'+str(pages)
	headers = {'User-Agent': 'Mozilla/5.0'}
	print(r)
	try:
		start_url = requests.get(r,headers=headers)
		t=1
		print(t)
		pass
	except:
		print("Connection Error - Retrying")
	print(t)
	
	if t==1:
		print("passes if")
		if start_url.status_code == "404":
			valid = 0
		soup = BeautifulSoup(start_url.text, 'html.parser')
		image_url = soup.find('div', class_='webcomic-image').img
	)
		Striped=image_url['src']
		fname=str(pages)+".png"
		urllib.request.urlretrieve(Striped, "F:\Between Failures/"+fname)
		pages=pages+1
		time.sleep(5)
		