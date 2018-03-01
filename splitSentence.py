import nltk.data
import fnmatch
import os
import sys
import re
reload(sys)  
sys.setdefaultencoding('utf8')


#  python splitSentence.py ~/TREC/classfication/Corpus/20ng ~/Project/20ngSentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

if __name__ == '__main__':
    folder = sys.argv[1]
    output = sys.argv[2]
    sentTotalCnt = 0
    for root, dirnames, filenames in os.walk(folder):
        for filename in filenames:        
            fp = open(os.path.join(root, filename))
            data = fp.read()
            data = unicode(data.strip(), errors='ignore')
            data = clean_html(data)
            count = 0
            for sentence in tokenizer.tokenize(data):
                sentence= sentence.strip()
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