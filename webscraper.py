from bs4 import BeautifulSoup
import requests

baseUrl = "https://iknow.jp/courses/"
subpages = list(range(566921, 566933))
subpages += list(range(594768, 594781))
subpages += list(range(615865, 615878))
subpages += list(range(615947, 615960)) 
subpages += list(range(616077, 616087))
subpages += list(range(598422, 598435))

# for i in subpages:
fullUrl = baseUrl + str(566921)
print(fullUrl + "\n")
html_content = requests.get(fullUrl).text
soup = BeautifulSoup(html_content, "lxml")

print(soup.prettify())

input("Press Enter to continue...")
