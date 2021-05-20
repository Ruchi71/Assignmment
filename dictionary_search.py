from PyDictionary import PyDictionary

dictionary = PyDictionary()
word = input('Word? ')
meaning = dictionary.meaning(word)

my_list = meaning['Noun'][0]
print(f'{word}.Noun.{my_list}')
  
