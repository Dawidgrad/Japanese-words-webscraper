from selenium import webdriver
import os
import sys

baseUrl = "https://iknow.jp/courses/"
subpages = list(range(566921, 566933))
subpages += list(range(594768, 594781))
subpages += list(range(615865, 615878))
subpages += list(range(615947, 615960)) 
subpages += list(range(616077, 616087))
subpages += list(range(598422, 598435))

fullUrl = baseUrl + str(566921)
print(fullUrl + "\n")
japaneseWords = []
englishWords = []

driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver.exe"))  # can be Firefox(), PhantomJS() and more
driver.get(fullUrl)

for element in driver.find_elements_by_class_name('text'):
    japaneseWords.append(element.text)

for element in driver.find_elements_by_class_name('response'):
    englishWords.append(element.text)

print(japaneseWords)
print(englishWords)
print(len(japaneseWords))
print(len(englishWords))

driver.close()


input("Press Enter to continue...")
