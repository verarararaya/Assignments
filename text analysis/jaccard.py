def JaccardIndex(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(len(set1 & set2)) / len(set1 | set2)
    return round(ans, 2)

def dicecoefficient(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(len(set1 & set2))*2 / (len(set1 | set2)+len(set1 & set2))
    return round(ans, 2)

base = "brexit delay request EU parliament"
target1 = "brexit chaos request EU extension"
target2 = "brexit delay react UK parliament"
target3 = "brexit delay referendum UK decision"
target4 = "brexit chaos react EU extension"
target5 = "brexit delay referendum EU extension"

ans1 = JaccardIndex(base, target1)
ans2 = JaccardIndex(base, target2)
ans3 = JaccardIndex(base, target3)
ans4 = JaccardIndex(base, target4)
ans5 = JaccardIndex(base, target5)
ans6 = JaccardIndex(target1, target2)
ans7 = JaccardIndex(target1, target3)
ans8 = JaccardIndex(target1, target4)
ans9 = JaccardIndex(target1, target5)
ans10 = JaccardIndex(target2, target3)
ans11 = JaccardIndex(target2, target4)
ans12 = JaccardIndex(target2, target5)
ans13 = JaccardIndex(target3, target4)
ans14 = JaccardIndex(target3, target5)
ans15 = JaccardIndex(target4, target5)
print([ans1, ans2, ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15])
print(JaccardIndex(target1,base))
answ1 = dicecoefficient(base, target1)
answ2 = dicecoefficient(base, target2)
answ3 = dicecoefficient(base, target3)
answ4 = dicecoefficient(base, target4)
answ5 = dicecoefficient(base, target5)
answ6 = dicecoefficient(target1, target2)
answ7 = dicecoefficient(target1, target3)
answ8 = dicecoefficient(target1, target4)
answ9 = dicecoefficient(target1, target5)
answ10 = dicecoefficient(target2, target3)
answ11 = dicecoefficient(target2, target4)
answ12 = dicecoefficient(target2, target5)
answ13 = dicecoefficient(target3, target4)
answ14 = dicecoefficient(target3, target5)
answ15 = dicecoefficient(target4, target5)
print([answ1, answ2, answ3,answ4,answ5,answ6,answ7,answ8,answ9,answ10,answ11,answ12,answ13,answ14,answ15])
print(dicecoefficient(target1,base))
print(dicecoefficient(target1,target1))


