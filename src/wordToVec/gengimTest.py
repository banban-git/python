from gensim.models import word2vec
import re

model = word2vec.Word2Vec.load('wiki.vec.pt')


# results = model.most_similar("日本")
results = model.most_similar(positive=['夫婦'], negative=['思いやり']) 
print("--------------------------------")
print("WORD", "                類似度")
print("--------------------------------")
for result in results:
    print('{:　<10s}'.format(result[0]), str( round(result[1] * 100, 3)) + "%")