import string
# Problem 1: Encryption
#

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    L1 = list(string.ascii_lowercase)
    L2 = list(string.ascii_uppercase)
    L3 = L1 + L2
    dic = {}
    for key in L3:
        #print "This is count %s" % key
        if key in L1:
            pos = (L1.index(key) + shift) % len(L1)
            value = L1[pos]
        if key in L2:
            pos = (L2.index(key) + shift) % len(L2)
            value = L2[pos]

        dic[key] = value
    return dic
	
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    cWord = ''
    for letter in text:
        if letter in coder:
            cWord = cWord + coder[letter]
        else:
            cWord = cWord + letter
    return cWord
def applyShift(text, shift):
    return applyCoder(text, buildCoder(shift))
	
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #return "Not yet implemented." # Remove this comment when you code the function
    maxCount = 0
    shift = 0
    for s in range(26):
        cWords = applyshift(text, shift)
        for w in cWords:
            LWORD = cWords.split('w') 
            count = 0
            for word in LWORD:
                if isWord(wordList, word):
                    count = count + 1
            if count > maxCount:
                maxCount = count
                shift = s
    return shift

#print buildCoder(3)
#print buildCoder(9)
#print applyCoder("Hello, world!", buildCoder(3))
#print applyCoder("Khoor, zruog!", buildCoder(23))
#print applyShift('This is a test.', 8)
#print applyShift('Bpqa qa i bmab.', 18)
s = applyShift('Hello, world!', 8)
print s
print findBestShift(loadWords(), s)
