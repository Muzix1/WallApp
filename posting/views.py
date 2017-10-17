# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from posting.models import Post
# Create your views here.
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['text']
    success_url = reverse_lazy('post-list')
    