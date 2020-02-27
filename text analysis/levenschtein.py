__author__ = 'user'

from nltk.metrics import edit_distance


#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),
s=[]
s.append('he is so handsome I can not help drooling')
s.append('how crazy today is')
s.append('wow I really like spam guys, come and eat it')
s.append('this looks fucking phenomenal')
s.append('Batman war on healthy shake lol')
sp = []
sp.append('wow come and eat spam')
sp.append('come and eat#spam, I really like it')
sp.append('come on guys, let’s eat spam')
sp.append('#spam I really like it guys')
sp.append('wow I really like #spam guys, come and eat it#ad')
sp.append('come and eat spam,guys')
sp.append('come and eat #spam,guys like it')
sp.append('guys come and eat spam, I really like it')
sp.append('really like it, #spam')
sp.append('really like it, spam, come and eat it')
sp.append('you guys like spam? come and eat it ')
sp.append('eat #spam, like #spam, come on guys')
sp.append('like spam? come and eat it')
sp.append('come on guys, #spam you will like it ')
sp.append('#spam, like it, eat it')
sp.append('I like spam, I eat spam')
sp.append('wow you like spam? come and eat it')
sp.append('#spam, what you like, what you eat')
sp.append('guys you will like spam, if you eat it')
sp.append('come and eat it,guys you would not regret')

# ans = edit_distance(s1, s2, transpositions=False)
# print(ans)
#
# ans = edit_distance(s3, s4, transpositions=False)
# print(ans)
#
# ans = edit_distance(s5, s6, transpositions=False)
# print(ans)
list1=[]
list2 = []
list3=[]
list4=[]
list5=[]
for n in range(20):
    ans = edit_distance(s[0], sp[n])
    list1.append(ans)
for n in range(20):
    ans = edit_distance(s[1], sp[n])
    list2.append(ans)
for n in range(20):
    ans = edit_distance(s[2], sp[n])
    list3.append(ans)
for n in range(20):
    ans = edit_distance(s[3], sp[n])
    list4.append(ans)
for n in range(20):
    ans = edit_distance(s[4], sp[n])
    list5.append(ans)
for n in range(5):
    ans = edit_distance(s[0], s[n])
    list1.append(ans)
for n in range(5):
    ans = edit_distance(s[1], s[n])
    list2.append(ans)
for n in range(5):
    ans = edit_distance(s[2], s[n])
    list3.append(ans)
for n in range(5):
    ans = edit_distance(s[3], s[n])
    list4.append(ans)
for n in range(5):
    ans = edit_distance(s[4], s[n])
    list5.append(ans)
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
# ans = distance.levenshtein(s1, s2)
# print(ans)
#
# ans = distance.levenshtein(s3, s4)
# print(ans)
#
# ans = distance.levenshtein(s5, s6)
# print(ans)
