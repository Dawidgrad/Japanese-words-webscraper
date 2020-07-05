def getData(siteUrl):
    # Extract the content from specified list of urls
    driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver.exe"))  # can be Firefox(), PhantomJS() and more
    driver.get(siteUrl)


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

    return

def writeDataToXlsx(wordCount, rowCount, worksheet):
    numberOfWords = len(japaneseWords)

    if (len(englishWords) == numberOfWords and len(sentenceExample1) == numberOfWords and len(sentenceExample2) == numberOfWords and 
        len(transliteration1) == numberOfWords and len(transliteration2) == numberOfWords and len(translation1) == numberOfWords and
        len(translation2) == numberOfWords and len(partOfSpeech) == numberOfWords):
        
        # Save the result in the XLSX file
        worksheet.write(rowCount, 0, 'Top {}'.format(wordCount))
        rowCount += 2

        worksheet.write(rowCount, 0, 'Japanese word')
        worksheet.write(rowCount, 1, 'English word')
        worksheet.write(rowCount, 2, 'Part of speech')
        worksheet.write(rowCount, 3, 'Sentence example 1')
        worksheet.write(rowCount, 4, 'Transliteration')
        worksheet.write(rowCount, 5, 'Translation')
        worksheet.write(rowCount, 6, 'Sentence example 2')
        worksheet.write(rowCount, 7, 'Transliteration')
        worksheet.write(rowCount, 8, 'Translation')
        rowCount += 1

        for i in range(0, numberOfWords):
            worksheet.write(rowCount, 0, japaneseWords[i])
            worksheet.write(rowCount, 1, englishWords[i])
            worksheet.write(rowCount, 2, partOfSpeech[i])
            worksheet.write(rowCount, 3, sentenceExample1[i])
            worksheet.write(rowCount, 4, transliteration1[i])
            worksheet.write(rowCount, 5, translation1[i])
            worksheet.write(rowCount, 6, sentenceExample2[i])
            worksheet.write(rowCount, 7, transliteration2[i])
            worksheet.write(rowCount, 8, translation2[i])
            rowCount += 1

    else:
        print("Number of items don't match between arrays")

    return rowCount

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

rowCount = 0
wordCount = 100

workbook = xlsxwriter.Workbook('Most common words.xlsx')
worksheet = workbook.add_worksheet()

for subpage in subpages:
    fullUrl = baseUrl + str(subpage)
    print(fullUrl + "\n")

    japaneseText = []
    japaneseWords = []
    englishWords = []
    transliteration = []
    translation = []
    partOfSpeech = []
    sentenceExample1 = []
    sentenceExample2 = []
    transliteration1 = []
    transliteration2 = []
    translation1 = []
    translation2 = []
    
    # Get the page data
    getData(fullUrl)
    
    # Remove the word instances from the array
    transliteration = [item for item in transliteration if not item.startswith('[')]

    # Split the japaneseText array into words and sentence examples
    # japaneseWords = japaneseText[0::3]
    # sentenceExample1 = japaneseText[1::3]
    # sentenceExample2 = japaneseText[2::3]

    processedExample2 = False

    for element in japaneseText:
        if '[' in element:
            japaneseWords.append(element)
            processedExample2 = False
        elif len(japaneseWords) != len(sentenceExample1):
            sentenceExample1.append(element)
        elif processedExample2 == False:
            sentenceExample2.append(element)
            processedExample2 = True
        else:
            continue

    transliteration1 = transliteration[0::2]
    transliteration2 = transliteration[1::2]
    translation1 = translation[0::2]
    translation2 = translation[1::2]

    # Write the data to the file    
    rowCount = writeDataToXlsx(wordCount, rowCount, worksheet)
    rowCount += 4
    wordCount += 100

workbook.close()

input("Press Enter to continue...")