def checkAnagrams(wordA, wordB):
    """
    变位词
    """
    word_dictA, word_dictB = {}, {}
    for i in wordA:
        word_dictA[i] = word_dictA.get(i, 0) + 1
    for j in wordB:
        word_dictB[j] = word_dictB.get(j, 0) + 1
    return word_dictA == word_dictB


if __name__ == '__main__':
    word1, word2 = 'map', 'aapam'
    rst = checkAnagrams(word1, word2)
    print(rst)
