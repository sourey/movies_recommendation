from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .recommendations import *
from .models import Movies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.

def get_recom(request):
	if request.method=='POST':
		input_title= request.POST.get("title")
		#capitalize the input
		input_title=input_title.title()
		print(input_title)
		m="a"
	else:
		input_title=""
		title=list(md['title'])
		genres=list(md['genres'])
		photo=list(md['poster_path'])
		imdb=list(md['imdb_score'])
		print(title)
		m=""

	try:
		dic=get_recommendations(input_title)[0:20]
		# dics=list(dic)
		title=list(dic['title'])
		genres=list(dic['genres'])
		photo=list(dic['poster_path'])
		imdb=list(dic['imdb_score'])
		
		
		# print(dic['title'])
		# print(dic['genres'])
		a="MOVIES SIMILAR TO"+" "+input_title
	except:
		a='We could not find the movie with title'+" "+input_title
		m=""
		title={}
		genres={}
		photo={}
		imdb={}
	
	
	    
	# return HttpResponse("Hello")
	return render(request,'movies/1st.html',{'title':title,'genres':genres,'photo':photo,'imdb':imdb,'a':a,'myvalue':m})

def index(request):
	movies_list=Movies.objects.all()[0:200]
	paginator = Paginator(movies_list, 21)
	page = request.GET.get('page')
	try:
		movies = paginator.page(page)
	except PageNotAnInteger:
		movies = paginator.page(1)
	except EmptyPage:
		movies = paginator.page(paginator.num_pages)
	
	context={
	'movies':movies
	}
	return render(request,"movies/index.html",context)
def detail(request,id):
	movie=get_object_or_404(Movies,pk=id)
	return render(request,'movies/detail.html',{'movie':movie})


# def get_recom(request):
# 	dics={}
# 	x=[]
# 	record=[]
# 	if request.method=='POST':
# 		input_title= request.POST.get("title")
# 		#capitalize the input
# 		#input_title=input_title.title()
# 		print(input_title)
# 	else:
# 		input_title="300"

# 	dic=get_recommendations(input_title)
# 	dics=list(dic)
# 	# print(dic.title)
# 	title=list(dic['title'])
# 	j=0
# 	for i in title:
# 		print(i)
# 		conn = sqlite3.connect(DB)
# 		cur = conn.cursor()
# 		record=cur.execute("SELECT * FROM movies where title='str(i)'").fetchall()
# 		j+=1
# 	print(record)

# 		# genres=list(dic['genres'])
# 		# x=[title,genres]
		
# 	a="MOVIES SIMILAR TO"+" "+input_title
# 	# except:
# 	# 	a='We could not find the movie with title'+" "+input_title
# 	# 	title={}
	
	
	    
# 	# return HttpResponse("Hello")
# 	return render(request,'1st.html',{'x':x,'a':a})

# #<img src="{%static 'posters/poster_'+str(123)+'.jpg'%}">