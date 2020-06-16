
with open('/home/ad.msystechnologies.com/dprasad/Downloads/vocab.vi') as f:
    mylist = [line.rstrip('\n') for line in f]

dictOfWords = { i : 0 for i in mylist }
