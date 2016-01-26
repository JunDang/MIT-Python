# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random
import re

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

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList) #built in function

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)]) 

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' '] #list comprehension
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	upperLetter = string.ascii_uppercase 
	lowerLetter = string.ascii_lowercase 
	dic = {}
	for letter in upperLetter:
		key = letter
		index = upperLetter.index(letter)
		newindex = (index + shift) % 26
		value = upperLetter[newindex]
		dic[key] = value
	for letter in lowerLetter:
		key = letter
		index = lowerLetter.index(letter)
		newindex = (index + shift) % 26
		value = lowerLetter[newindex]
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
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### This is a wrapper function.
    return applyCoder(text, buildCoder(shift))
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
	"""
	Finds a shift key that can decrypt the encoded text.

	text: string
	returns: 0 <= int < 26
	"""
	bestShift = 0
	max_count = 0
	for shift in range(26):
		coded_text = applyShift(text, shift)
		textwords = coded_text.split(' ')
		count = 0
		for word in textwords:
			if isWord(wordList, word):
				count = count + 1
		if count > max_count:
			max_count = count
			bestShift = shift
	return bestShift
				
		
	
def decryptStory():
	"""
	Using the methods you created in this problem set,
	decrypt the story given by the function getStoryString().
	Use the functions getStoryString and loadWords to get the
	raw data you need.

	returns: string - story in plain text
	"""
	wordList = loadWords()
	story = getStoryString()
	print story
	bestShift = findBestShift(wordList, story)
	print bestShift
	decryptStory = applyShift(story, bestShift)
	return decryptStory

    #wordList = loadWords()
   # story = getStoryString()
  #  bestshift =  findBestShift(wordList, story)
  #  return applyShift(story, bestshift)

# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
	#wordList = loadWords()
	#s = applyShift('I love you Ethan, my dearest son!', 10)
	#print s
	#bestShift = findBestShift(wordList, s)
	#print bestShift
	#print applyShift(s, bestShift)
	#assert applyShift(s, bestShift) == 'I love you Ethan, my dearest son!'
    # To test decryptStory, comment the above four lines and uncomment this line:
	print decryptStory()
