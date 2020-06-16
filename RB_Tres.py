
with open('/home/Downloads/vocab.vi') as f:
    mylist = [line.rstrip('\n') for line in f]

dictOfWords = { i : 0 for i in mylist }
