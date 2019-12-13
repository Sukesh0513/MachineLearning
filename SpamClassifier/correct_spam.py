import pandas as pd
list_heading = []
for x in range(0 , 58):
    list_heading.append(str(x))
myDataframe = pd.read_csv("spambase.data", names = list_heading)
k = int(4601*0.8)


training_set = myDataframe.sample(k)
r, c = training_set.shape
list_and = [None]*57
list_or_duplicate = [None]*r
for x in range(0 , 57):
    c = 0
    for y in range(0 , r):
        if training_set[str("57")].iloc[y] == 1:
            list_or_duplicate[c] = training_set[str(x)].iloc[y]
            c = c + 1
    list_and[x] = list(dict.fromkeys(list_or_duplicate))
    list_and[x].pop()


list_valued = []

for x in range(0 , 57):
     if len(list_and[x]) < 60:
            list_valued.append(x)

l = int(4601*0.2)
testing_set = myDataframe[0:4600]
r, c = testing_set.shape
n = 0
for y in range(0, r):
    count = 0
    for x in range(0, len(list_valued)):
        if testing_set[str(list_valued[x])].iloc[y] in list_and[list_valued[x]]:
            count = count + 1
    if count != len(list_valued) and testing_set["57"].iloc[y] == 1:
        n = n + 1
    if count == len(list_valued) and testing_set["57"].iloc[y] == 0:
        n = n + 1



print(100 - (n/r)*100)






