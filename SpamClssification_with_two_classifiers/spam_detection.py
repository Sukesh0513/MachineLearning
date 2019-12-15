import pandas as pd
list_heading = []
# hedings for thr coloumns
for x in range(1 , 59):
    list_heading.append(str(x))
myDataset1 = pd.read_csv("spambase.data", names = list_heading)
r,c = myDataset1.shape

# trainig the classifier for the instances in the spam
def spam_tain():
    myDataset = myDataset1[0:1500]
    r, c = myDataset.shape
    list_and = [None]*c
    list_or = [None]*r
    for x in range(1 , c):
        for y in range(0, r):
            list_or[y] = myDataset[str(x)].iloc[y]
        list_and[x-1] = list(dict.fromkeys(list_or))
        count = 0
    mean_list = []
    sd_list = []
    classifier_list = []
    for x in range(1, 58):
        mean_list.append(myDataset[str(x)].mean())
        sd_list.append(myDataset[str(x)].std())
        classifier_list.append([mean_list[x-1]-(sd_list[x-1]), mean_list[x-1]+(sd_list[x-1])])
    return classifier_list

# trainig the classifier for the instances in the spam
def ham_train():
    myDataset = myDataset1[2000:3500]
    r, c = myDataset.shape
    list_and = [None] * c
    list_or = [None] * r
    for x in range(1, c):
        for y in range(0, r):
            list_or[y] = myDataset[str(x)].iloc[y]
        list_and[x - 1] = list(dict.fromkeys(list_or))
        count = 0
    mean_list = []
    sd_list = []
    classifier_list = []
    for x in range(1, 58):
        mean_list.append(myDataset[str(x)].mean())
        sd_list.append(myDataset[str(x)].std())
        classifier_list.append([mean_list[x - 1] - (sd_list[x - 1]), mean_list[x - 1] + (sd_list[x - 1])])
    return classifier_list
# comparing the results for the training set from both the classsifiers and calculating the accuracy
spam_hyp_list = spam_tain()
ham_hyp_list = ham_train()
print(len(spam_hyp_list))
n = 0
test_set = myDataset1.sample(int(r*0.3))
r,c = test_set.shape;
bug = 0
for x in range(0,r):
    spam_prob, ham_prob = 0, 0
    for y in range(1, c):
        if spam_hyp_list[y-1][0]< test_set[str(y)].iloc[x] < spam_hyp_list[y-1][1]:
            spam_prob = spam_prob + 1
        if ham_hyp_list[y-1][0]< test_set[str(y)].iloc[x] < ham_hyp_list[y-1][1]:
            ham_prob = ham_prob + 1
    if spam_prob > ham_prob:
        if test_set[str("58")].iloc[x] == 0:
            n = n + 1
    if spam_prob < ham_prob:
        if test_set[str("58")].iloc[x] == 1:
            n = n + 1
    print("count at {0} , {1} , {2}".format(str(x), str(spam_prob), str(ham_prob)))
print("Accuracy : "+str(100-n/r*100))