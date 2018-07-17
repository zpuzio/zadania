def random_word():
    import random
    a = []
    with open('slownik.txt', 'r') as f:
      line = f.readline()
      while line:
        a.append(line)
        line = f.readline()
    word = random.randint(0,len(a))
    print a[word]
    return a[word]

if __name__=="__main__":
    random_word()