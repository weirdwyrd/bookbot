def generateReport(bookPath, wordCount, charDict):
    print(f'--- Begin report of {bookPath} ---')
    print(f'{wordCount} words found in the document \n')
    # transform to sorted list
    charList = list(charDict.items())
    #lambda function grabs 2nd value of tuples produced by dict.items()
    charList.sort(key=lambda x: (x[1]), reverse=True)    
    #loop over list
    for char in charList:
        #if .isalpha() then print
        if(char[0].isalpha()): print(f"The '{char[0]}' character was found {char[1]} times")
    print('--- End report ---')

def countCharacters(contents):
    charCounter = {}
    # for each char in contents
    for char in contents:
        # make lowercase
        char = char.lower()
        # check if in dict
        if char in charCounter:
            #increment count
            charCounter[char] += 1
        else:
            #add to dict with init count of 1
            charCounter[char] = 1
    return charCounter

def countWords(contents):
    words = contents.split()
    return len(words)

def printBook(contents):
    print(contents)

def main():
    bookPath = 'books/frankenstein.txt'
    with open(bookPath) as file:
        contents = file.read()
        # printBook(contents)
        wordCount = countWords(contents)
        charDict = countCharacters(contents)
        generateReport(bookPath, wordCount, charDict)

main()