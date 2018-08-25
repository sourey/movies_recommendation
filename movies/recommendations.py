import pandas
from numpy import  *
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
seterr(divide='ignore', invalid='ignore')
md= pandas.read_csv('final_movies.csv')
md.fillna(0, inplace=True)
#print(md.columns)

md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i.replace(" ","") for i in x] if isinstance(x, list) else [])
#print(md['genres'][0:20])

md['keywords'] = md['keywords'].fillna('[]').apply(literal_eval).apply(lambda x: [i.replace(" ","") for i in x] if isinstance(x, list) else [])
#print(md['keywords'][0:10])
md['cast'] = md['cast'].fillna('[]').apply(literal_eval).apply(lambda x: [i.replace(" ","") for i in x] if isinstance(x, list) else [])
md['cast'] = md['cast'].apply(lambda x: x[:3] if len(x) >=3 else x)
#print(md['cast'][0:10])
md['director'] = md['director'].fillna('[]').apply(literal_eval).apply(lambda x: [i.replace(" ","") for i in x ] if isinstance(x, list) else [])
#print(md['director'][0:10])
md['combined'] = md['keywords']+md['genres']+md['cast']+md['director']

c = CountVectorizer()
vect = c.fit_transform(md['combined'].astype(str))
# print(vect)
word=c.get_feature_names()
# print(word)
x=vect.toarray()
md['tagline']=md['tagline'].astype(str)
md['overview']=md['overview'].astype(str)

md['description'] = md['overview'] + md['tagline']

tf = TfidfVectorizer(analyzer='word',min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(md['description'])# print(x[1])

def calculate_similarity(m1=[]):
	magnitude_A=linalg.norm(m1)
	similarity=[]
	for i in range(len(md)):
		dot_product=(m1.dot(x[i]))
		magnitude_B=(linalg.norm(x[i]))
		try:
			product_magnitude_AB=magnitude_A*magnitude_B
			sim=dot_product/product_magnitude_AB
		except:
			sim=0
		similarity.append(sim)
	return array(similarity)

indices = pandas.Series(md.index, index=md['title'])

def get_recommendations(title):
		idx = indices[title]
		# print(idx)

		aaa=calculate_similarity(x[idx])
		y=linear_kernel(tfidf_matrix, tfidf_matrix)[idx]
		total_sim=y+aaa		
		md['sim']=total_sim
		hd=md
		hd=hd.sort_values('sim',ascending=False)
		hd=hd.head(20).sort_values('imdb_score',ascending=False)
		#print(hd['sim'][0:20])
		return hd

