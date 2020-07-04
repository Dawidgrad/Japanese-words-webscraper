from selenium import webdriver
import os
import sys

# Prepare the urls
baseUrl = "https://iknow.jp/courses/"
subpages = list(range(566921, 566933))
subpages += list(range(594768, 594781))
subpages += list(range(615865, 615878))
subpages += list(range(615947, 615960)) 
subpages += list(range(616077, 616087))
subpages += list(range(598422, 598435))

fullUrl = baseUrl + str(566921)
print(fullUrl + "\n")

japaneseText = []
englishWords = []
transliteration = []
translation = []
partOfSpeech = []

# Extract the content from specified list of urls
driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver.exe"))  # can be Firefox(), PhantomJS() and more
driver.get(fullUrl)

for element in driver.find_elements_by_class_name('text'):
    japaneseText.append(element.text)

for element in driver.find_elements_by_class_name('response'):
    englishWords.append(element.text)

for element in driver.find_elements_by_class_name('transliteration'):
    transliteration.append(element.text)

for element in driver.find_elements_by_class_name('translation'):
    translation.append(element.text)

for element in driver.find_elements_by_class_name('part-of-speech'):
    partOfSpeech.append(element.text)

driver.close()

# Split the japaneseText array into words and sentence examples
japaneseWords = japaneseText[0::3]
sentenceExample1 = japaneseText[1::3]
sentenceExample2 = japaneseText[2::3]
transliteration1 = transliteration[1::3]
transliteration2 = transliteration[2::3]

# Save the result in the CSV file
with open('Most common words.xlsx', 'w') as f:
    for line in s:
        f.write(line)



input("Press Enter to continue...")
