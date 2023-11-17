from django.urls import path

from .views.ForumViews import ForumView
from .views.ForumsLikesDislikesView import DislikesView,LikesView,DislikesCommentView,LikesCommentView
from .views.CommentsViews import CommentView
urlpatterns = [
    path('', ForumView.as_view(),name='forum-list'),
    path('<int:id>', ForumView.as_view(),name='forum-detail'),
    path('like/', LikesView.as_view(),name='like'),
    path('dislike/', DislikesView.as_view(),name='dislike'),
    path('comment/', CommentView.as_view(),name='comments'),
    path('comment/like/', LikesCommentView.as_view(),name='comments'),
    path('comment/dislike/', DislikesCommentView.as_view(),name='comments'),
]
