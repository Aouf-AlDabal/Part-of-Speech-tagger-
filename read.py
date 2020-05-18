
########################## Reading Data to Dictionary wordTags#################
import os
from pip.utils import encoding

wordTags = {}

files = os.listdir('data')
for file in files:
    with open('data\\'+file,encoding='utf8',mode='r',errors='ignore') as f:
        s = f.read()
        s = s.split()

        try:
            for item in s:
                word, tag = item.split('/')

                if word in wordTags.keys():
                  if tag in wordTags[word].keys():
                       wordTags[word][tag]=wordTags[word][tag]+1
                  else:
                        wordTags[word][tag]=1
                else:
                    wordTags[word]={tag:1}
        except Exception:
            pass


# print(wordTags)



#
########################## Function to classify words #################
import unicodedata as ud


def mostTag(tags):
    tagcount=0
    tag=""
    for i in tags.keys():
        if tags[i]>tagcount:
            tagcount=tags[i]
            tag=i
    return tag,tagcount


def asstage(word,wordTags):
    word = ''.join(c for c in word if not ud.category(c).startswith('P'))

    if(word in wordTags.keys() ):
        if(len(wordTags[word].keys())==1):
            key, value = list(wordTags[word].items())[0]
            return  key , value
        else:
            return mostTag(wordTags[word])
    else:
        return "NN",1



##########################  testing #################

with open('test.txt','r',errors="ignore",encoding="utf8") as f:
    test = f.read()
    test = test.split()

for test_word in test:

    test_tag ,test_tag_count = asstage(test_word,wordTags)

  #  print(test_word,':',test_tag)

    with open('output.txt','a',errors="ignore",encoding="utf8") as f:
        #output = f.write('{test_word} : {test_tag} \n')
        #print(type(test_tag))
       # print(type(test_word))
      #  output = f.write(test_word+":"+str(test_tag)+"count:"+str(test_tag_count)+'\n')
        output = f.write(test_word+" : "+"("+str(test_tag)+":"+str(test_tag_count)+")"+'\n')