word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]

def anagrams(word, word_list):
    word = word.lower().replace(" ", "")
    sorted_word = sorted(word)
    anagram_list = []
    for wrd in word_list:
        wrd = wrd.lower().replace(" ", "")
        if sorted(wrd) == sorted_word:
            anagram_list.append(wrd)
    return anagram_list

anagram_list = anagrams(word, word_list)
print(anagram_list)
