from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords as sw
from nltk.stem import WordNetLemmatizer

from gensim import corpora, models
import gensim
class LDAProcess:
    def loadData(self):
        tokenizer = RegexpTokenizer(r'\w+')

        # create English stop words list
        en_stop = get_stop_words('en')

        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()
            

        stopwords = sw.words('english')
        doc_set = []
        for i in range(10):
            with open(str(i) + '.txt','r') as f:
                docs = f.readlines()
            file = open('topic/topic' + str(i) +'.txt','a')
            # list for tokenized documents in loop
            texts = []

            # loop through document list
            for i in docs:
            
                # clean and tokenize document string
                raw = i.lower()
                tokens = tokenizer.tokenize(raw)

                # remove stop words from tokens
                #stopped_tokens = [i for i in tokens if not i in en_stop]
                lemma = WordNetLemmatizer()
                
                resultwords = [word.lower() for word in tokens
                            if word not in stopwords and wn.synsets(word)] # removes non-word
                
                resultwords = [lemma.lemmatize(word, wn.NOUN) for word in resultwords]

                # stem tokens
                #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
                #print(resultwords)
                # add tokens to list
                texts.append(resultwords)

            # turn our tokenized documents into a id <-> term dictionary
            dictionary = corpora.Dictionary(texts)
            
            # convert tokenized documents into a document-term matrix
            corpus = [dictionary.doc2bow(text) for text in texts]

            # generate LDA model
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=10)
            #print(ldamodel.print_topics(num_topics=50, num_words=10))
            #print(str(ldamodel.print_topics(num_topics=2, num_words=4)[0][1]).split('+')[1])
            for topic in ldamodel.print_topics(num_topics=50, num_words=10):
                words = ''
                print(topic)
                for word in str(topic[1]).split('+'):
                    words = words + ' ' + word.split('*')[1]

                file.write(words + '\n')