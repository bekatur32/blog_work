from django.urls import path
from .views import PostListView, post_search, post_detail, post_share, post_comment
from .feed import LatestPostsFeed


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
   # path('tag/<slug:tag_slug>/', PostListView, name='pot_list_by_tag'),
    path('<int:day>/<int:month>/<int:year>/<str:slug>/',
          post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment', post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),
]