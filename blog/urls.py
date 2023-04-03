
from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed
app_name = 'blog'
urlpatterns = [
    #path("url adress" ,'view')
    path('' , blog_view,name='index'),
    path('<int:pid>' , blog_single,name='single'),
    path('category/<str:cat_name>' ,blog_view,name='category'),
    path('tag/<str:tag_name>' ,blog_view,name='tag'),
    path('author/<str:author_username>',blog_view,name='author'),
   # path('test' , test ,name='test'),
    path('rss/feed/', LatestEntriesFeed()),
    path('search/',blog_search,name='search'),
    

]