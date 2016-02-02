import random
import string
import collections

analiste=[]

howmanywords=500000


def createword():
    for i in range(howmanywords):
        X=random.randint(2,8)
        word=''.join(random.choice(string.ascii_lowercase) for _ in range(X))
        analiste.append(word)
    print(analiste)




createword()
print(collections.Counter(analiste).most_common())
collections.Counter