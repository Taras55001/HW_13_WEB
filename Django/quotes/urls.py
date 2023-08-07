from django.urls import path, include
from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.main, name='root'),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('tag/<str:tag_name>/page/<int:page>/', views.quotes_by_tag, name='quotes_by_tag_paginate'),
    path('author/<str:author_id>/', views.author_detail_view, name='author_detail'),
    path('<int:page>', views.main, name='root_paginate'),
    path('generate-quote/', views.generate_quote_view, name='generate_quote'),
    path('quote/', views.show_quote_view, name='show_quote'),
    path('feel_site/', views.feel_site, name='feel_site'),
    ]
