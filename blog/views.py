#In default django looks for templates in templates/<appName>/ --folder


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post



#This is the the 'home' page of /blog (app)
#title is just the text title appearing on the tab of <localhost:8000>/
#The content is placed inside the . blog/home.html file inside the blog folder(kind of namespaceing the blog)
#context is taken from the database and put inside context dictionary 
def home(request):
	context = {
		'posts':Post.objects.all(),#taking all the post from Post table from the sqlite database
		'title':'Home'
	}
	return render(request, 'blog/home.html',context)



#This is view for viewing all the posts in 'localhost:8000/' url 
#template of the class is store in 'blog/home.html'
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	#context_object_name is name passed along as the return type of object_list
	#to the given 'blog/home.html' file 
	#here(html template) instead of using object_list we use 'posts' as the looping object_list
	#it does not have any relationship with the dictionary defined above in home function
	context_object_name = 'posts' 
	ordering = ['-date_posted']
	paginate_by = 2





#This is the view for viewing all the post by a particular user at 'localhost:8000/user/<username>'
#template of the file stored in 'blog/user_posts.html'
class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 2

	#filtering the database with posts only created by certain user
	#returns posts by a particular author ordered by descend ~ date_posted
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')






#This is the view for viewing all the post by a particular user at 'localhost:8000/<pk:of the post>
#template of the file stored in 'blog/post_details.html'
class PostDetailView(DetailView):
	model = Post




#This is to create a new post by a particular logged in user
#This is called by 'localhost:8000/post/new' by a tab on the base.html for 'New Post'
#template for the class is 'blog/post_form.html'
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)





#This is to update a post by a particular logged in user
#This is called by 'localhost:8000/post/<pk>/update' by a tab on 'update' viewed on 'post_details.html'
#it directs page to 'blog/post_forms.html'
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




#same as the update view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False





#This is the the about page of /blog (app)
#title is just the text title appearing on the tab of <localhost:8000>/about/
#The content is placed inside the . blog/about.html file inside the blog folder
def about(request):
	return render(request, 'blog/about.html', {'title':'About'}) 