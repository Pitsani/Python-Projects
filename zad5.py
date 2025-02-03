def anagrami():
    word1 = input("Duma1: ")
    word2 = input("Duma2: ")
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    if sorted(word1) == sorted(word2):
        print("Anagrami sa")
    else:
        print("Ne sa anagrami")
anagrami()
