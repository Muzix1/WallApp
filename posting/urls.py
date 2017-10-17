
from django.conf.urls import url
from posting.views import PostListView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post-list"),
    url(r'^add/', PostCreateView.as_view(), name="post-create"),
]