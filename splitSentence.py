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
sentTotalCnt = 0
for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:        
        fp = open(os.path.join(root, filename))
        data = fp.read()
        data = unicode(data.strip(), errors='ignore')
        count = 0
        for sentence in tokenizer.tokenize(data):
            sentence= sentence.strip()
            # Remove tags <>
            if sentence[0] == '<' and sentence[-1] == '>'
                continue
            diretory = str(sentTotalCnt/10000).zfill(5)
            pathname = output+'/'+diretory+'/'+filename+'.'+str(count)
            if not os.path.exists(os.path.dirname(pathname)):
                try:
                    os.makedirs(os.path.dirname(pathname))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            writeF = open(pathname, 'w')
            # sentence = unicode(sentence.strip(), errors='ignore')
            writeF.write(sentence.strip())             
            count += 1
            sentTotalCnt += 1