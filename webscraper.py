from selenium import webdriver
import os
import sys
import xlsxwriter

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

# Remove the word instances from the array
transliteration = [item for item in transliteration if not item.startswith('[')]

# Split the japaneseText array into words and sentence examples
japaneseWords = japaneseText[0::3]
sentenceExample1 = japaneseText[1::3]
sentenceExample2 = japaneseText[2::3]
transliteration1 = transliteration[0::2]
transliteration2 = transliteration[1::2]
translation1 = translation[0::2]
translation2 = translation[1::2]

numberOfWords = len(japaneseWords)

if (len(englishWords) == numberOfWords and len(sentenceExample1) == numberOfWords and len(sentenceExample2) == numberOfWords and 
    len(transliteration1) == numberOfWords and len(transliteration2) == numberOfWords and len(translation1) == numberOfWords and
    len(translation2) == numberOfWords and len(partOfSpeech) == numberOfWords):
    
    # Save the result in the XLSX file
    workbook = xlsxwriter.Workbook('Most common words.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Japanese word')
    worksheet.write(0, 1, 'English word')
    worksheet.write(0, 2, 'Part of speech')
    worksheet.write(0, 3, 'Sentence example 1')
    worksheet.write(0, 4, 'Transliteration')
    worksheet.write(0, 5, 'Translation')
    worksheet.write(0, 6, 'Sentence example 2')
    worksheet.write(0, 7, 'Transliteration')
    worksheet.write(0, 8, 'Translation')

    for i in range(0,numberOfWords):
        worksheet.write(i, 0, japaneseWords[i])
        worksheet.write(i, 1, englishWords[i])
        worksheet.write(i, 2, partOfSpeech[i])
        worksheet.write(i, 3, sentenceExample1[i])
        worksheet.write(i, 4, transliteration1[i])
        worksheet.write(i, 5, translation1[i])
        worksheet.write(i, 6, sentenceExample2[i])
        worksheet.write(i, 7, transliteration2[i])
        worksheet.write(i, 8, translation2[i])
    
    workbook.close()
else:
    print("Number of items don't match between arrays")


input("Press Enter to continue...")


worksheet.write('B3', u'Это фраза на русском!')
