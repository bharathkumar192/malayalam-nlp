# import requests
# test_url = "http://127.0.0.1:5000/suggestions"
# test_response = requests.post(test_url, data = 'മടങ്ങിപ്പോവുക'.encode('utf-8'))
# print(test_response)



from SpellCheck import load1stCluster, loadLastCluster, loadcharIndex, readForwardFSA, readReverseFSA, loadTrigramFreqHash, loadTrigramOpt, loadCiC, spellchk, split_chars,suggestionGeneration


load1stCluster()
loadLastCluster()
loadcharIndex()
readForwardFSA()
readReverseFSA()
loadTrigramFreqHash()
loadTrigramOpt()
loadCiC()


def spell(mal_word):
    errorWords = []
    if mal_word:
        for word in mal_word.split(' '):
            if spellchk(word) == 0:
                errorWords.append(word)
   
    print(errorWords)

spell('ആഗ്രക്കുന്ണ്ട')
spell('ആഗ്രഹിക്കുന്നുണ്ടോ')