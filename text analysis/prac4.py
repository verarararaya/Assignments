import nltk
from nltk.corpus import stopwords
from nltk.text import TextCollection
from nltk.corpus import wordnet
import numpy as np
from math import log
def get_wordnet_pos(tag):
   if tag.startswith('J'):
      return wordnet.ADJ
   elif tag.startswith('V'):
        return wordnet.VERB
   elif tag.startswith('N'):
       return wordnet.NOUN
   elif tag.startswith('R'):
       return wordnet.ADV
   else:
       return None
f1 = open("kurds.txt")
lines1 = f1.read()
f1.close()
documents1 = lines1.split('I.')
# documents2 = lines1.split('I.')
list_stopWords=list(set(stopwords.words('english')))
for i in range(0,len(documents1)):
    documents1[i] = documents1[i].strip().replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(':',' ').replace('&',' ').replace('(',' ').replace(')',' ').replace('“',' ').replace('”',' ').replace('\’',' ')
    GAP_PATTERN = r'\s+'
    regex_wt = nltk.RegexpTokenizer(pattern=GAP_PATTERN,gaps=True)
    documents1[i] = regex_wt.tokenize(documents1[i])
    documents1[i] = [w.lower() for w in documents1[i]]
    tagged_sent = nltk.pos_tag(documents1[i])
    wn = nltk.WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wn.lemmatize(tag[0], pos=wordnet_pos))
    documents1[i] = lemmas_sent
    documents1[i] = [w for w in documents1[i] if not w in list_stopWords]
# tfd = []
# for i in range(0,len(documents1)):
#     tf = {}
#     for j in range(0,len(documents1[i])):
#         sum = documents1[i].count(documents1[i][j])
#         tfnumber = sum / len(documents1[i])
#         tf.setdefault(documents1[i][j], tfnumber)
#     tfd.append(tf)
# print(tfd)
tfd1 = []
idf1 = []
# wordlist = []
copurs = TextCollection(documents1)
for i in range(0,len(documents1)):
    tf1 = {}
    tf2 = {}
    for j in range(0,len(documents1[i])):
        tf = copurs.tf(documents1[i][j],documents1[i])
        idf = copurs.idf(documents1[i][j])
        tfidf = tf*idf
        tf2.setdefault(documents1[i][j], idf)
        tf1.setdefault(documents1[i][j], round(tfidf,2))
        # wordlist.append((documents1[i][j]+',')*int(round(tfidf,2)*100))
    tfd1.append(tf1)
    idf1.append(tf2)
# print(documents1)
# print(idf1)
# print(tfd1)
pmi1 = []
for i in range(0,len(documents1)):
    bgm = nltk.collocations.QuadgramAssocMeasures()
    finder = nltk.collocations.QuadgramCollocationFinder.from_words(documents1[i])
    scored = finder.score_ngrams(bgm.likelihood_ratio)
    pmi1.append(scored)
# print(pmi1)
f2 = open("spam.txt")
lines2 = f2.read()
documents2 = lines2.split('I.')
data1 = np.array(documents2)
f3 = open("random.txt")
lines3 = f3.read()
documents3 = lines3.split('I.')
for i in range(0,len(documents2)):
    documents2[i] = documents2[i].strip().replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(':',' ').replace('&',' ').replace('(',' ').replace(')',' ').replace('“',' ').replace('”',' ').replace('\’',' ')
    GAP_PATTERN = r'\s+'
    regex_wt = nltk.RegexpTokenizer(pattern=GAP_PATTERN,gaps=True)
    documents2[i] = regex_wt.tokenize(documents2[i])
    documents2[i] = [w.lower() for w in documents2[i]]
    tagged_sent = nltk.pos_tag(documents2[i])
    wn = nltk.WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wn.lemmatize(tag[0], pos=wordnet_pos))
    documents2[i] = lemmas_sent
    documents2[i] = [w for w in documents2[i] if not w in list_stopWords]
for i in range(0,len(documents3)):
    documents3[i] = documents3[i].strip().replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(':',' ').replace('&',' ').replace('(',' ').replace(')',' ').replace('“',' ').replace('”',' ').replace('\’',' ')
    GAP_PATTERN = r'\s+'
    regex_wt = nltk.RegexpTokenizer(pattern=GAP_PATTERN,gaps=True)
    documents3[i] = regex_wt.tokenize(documents3[i])
    documents3[i] = [w.lower() for w in documents3[i]]
    tagged_sent = nltk.pos_tag(documents3[i])
    wn = nltk.WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wn.lemmatize(tag[0], pos=wordnet_pos))
    documents3[i] = lemmas_sent
    documents3[i] = [w for w in documents3[i] if not w in list_stopWords]
documents4 = documents2+documents3
data1 = np.array(documents2)
data2 = np.array(documents3)
data3 = np.array(documents4)
def calc_ent(x):
    """
        calculate shanno ent of x
    """

    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        logp = np.log2(p)
        ent -= p * logp

    print(ent)

def calcShannonEnt(dataSet):
    numEntries = len(dataSet) # 样本数
    labelCounts = {} # 该数据集每个类别的频数
    for featVec in dataSet:  # 对每一行样本
        currentLabel = featVec[-1] # 该样本的标签
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries # 计算p(xi)
        shannonEnt -= prob * log(prob, 2)  # log base 2
    return shannonEnt

print(calcShannonEnt(data1))
print(calcShannonEnt(data2))
print(calcShannonEnt(data3))

