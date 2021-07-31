from gensim.models import word2vec
import re

model = word2vec.Word2Vec.load('wiki.vec.pt')

# 
results = model.most_similar("日本")

results = model.most_similar(positive=['男性','おば'], negative=['女性']) 

for result in results:
    print(result)