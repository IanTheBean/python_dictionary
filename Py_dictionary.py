## import the dictionary python library
from PyDictionary import PyDictionary
dictionary = PyDictionary()

#pass through a word and return a string iwth the definition
def get_definition(word):
	meaning = str(dictionary.meaning(word))
	if "Adjective" in meaning:
		meaning = meaning.replace('Adjective', '')
	if "Noun" in meaning:
		meaning = meaning.replace('Noun', '')
		
	elif "Verb" in meaning:
		meaning = meaning.replace('Verb', '')
		
	if "Adverb" in meaning:
		meaning = meaning.replace('Adjective', '')
	if "Preposition" in meaning:
		meaning = meaning.replace('Preposition', '')
	if "Conjunction" in meaning:
		meaning = meaning.replace('Conjunction', '')
	if "Interjection" in meaning:
		meaning = meaning.replace('Interjection', '')
	
	
	meaning = meaning.replace('{', '')
	meaning = meaning.replace('}', '')
	meaning = meaning.replace('\'', '')
	meaning = meaning.replace(']', '')
	meaning = meaning.replace('[', '')
	meaning = meaning.replace(': ', '')
	meaning = meaning.replace(',', ', or')
	sep = ','
	meaning = meaning.split(sep, 1)[0]
	meaning = meaning + "."
	return meaning

##very optional##
## just a console display for finding a word
while 1 == 1:	
	dictionary_word = input("Enter a word to be defined:\n")
	print(get_definition(dictionary_word))
