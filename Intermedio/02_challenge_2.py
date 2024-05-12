### is it anagram? ###

#  Escribe una función que reciba dos palabras (String) y retorne
#  verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS
#    las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.

def anagram(word1, word2):
  word1 = word1.lower()
  word2 = word2.lower()

  if word1 == word2:
    print("isn't an anagram")
  elif word1 == word2[::-1]:
    print("is an anagram")
  
anagram("Roma", "amor")