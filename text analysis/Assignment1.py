import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
import urllib
import urllib.request
import bs4
# Q1:# file = open('harry.txt')
# # files = file.read()
# # token = nltk.word_tokenize(files)
# # print(token)
# # # GAP_PATTERN = r'\s+'
# # # regex_wt = nltk.RegexpTokenizer(pattern=GAP_PATTERN,
# # #                                 gaps=True)
# # # words = regex_wt.tokenize(files)
# # # print(words)
# # words = [w.lower() for w in token]
# # print(nltk.pos_tag(words))
#
# Q2:# def get_wordnet_pos(tag):
# #     if tag.startswith('J'):
# #         return wordnet.ADJ
# #     elif tag.startswith('V'):
# #         return wordnet.VERB
# #     elif tag.startswith('N'):
# #         return wordnet.NOUN
# #     elif tag.startswith('R'):
# #         return wordnet.ADV
# #     else:
# #         return None
# #  file1 = open('what.txt')
# # files1 = file1.read()
# # tokens = nltk.word_tokenize(files1)
# # tagged_sent = nltk.pos_tag(tokens)
# # stemmer = PorterStemmer()
# # # print([stemmer.stem(wd) for wd in tokens])
# # wn = nltk.WordNetLemmatizer()
# # lemmas_sent = []
# # for tag in tagged_sent:
# #     wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
# #     lemmas_sent.append(wn.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原
# #
# # print(lemmas_sent)
url = 'https://www.investopedia.com/comeback-stocks-how-ibm-has-become-a-growth-stock-again-4771589'
urllib.request.urlopen(url)
rawhtml = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(rawhtml)
print(soup.title)