# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse

from django.shortcuts import render_to_response


# from django.shortcuts import render

import datetime

from app.models import Publisher, Author, Book
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

########## api imports ############

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import renderers


@login_required
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('time.html', locals())

def hours_ahead(request, offset):
    current_date = datetime.datetime.now()
    hour_offset = int(offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)  
    return render_to_response('hours_ahead.html', locals())


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers.html'
    context_object_name = 'publisher_list'
    queryset = Publisher.objects.all()
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(PublisherListView, self).get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context


########### api ###############

# serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'publisher', 'publication_date')
        depth = 1

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website')


# view sets

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
