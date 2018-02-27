import nltk.data
import fnmatch
import os
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

#  python splitSentence.py ~/TREC/classfication/Corpus/20ng ~/Project/20ngSentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

folder = sys.argv[1]
output = sys.argv[2]
for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:        
        fp = open(os.path.join(root, filename))
        data = fp.read()
        data = unicode(data.strip(), errors='ignore')
        count = 0
        for sentence in tokenizer.tokenize(data):
            writeF = open(output+'/'+filename+'.'+str(count), 'w')
            # sentence = unicode(sentence.strip(), errors='ignore')
            writeF.write(sentence.strip())             
            count = count + 1