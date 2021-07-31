from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('C:/work/wikiextractor_test/wiki_wakati_second.text8')

model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
model.save("./wiki.vec.pt")