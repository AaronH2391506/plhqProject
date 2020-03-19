
# coding: utf-8

# In[ ]:


from django.urls import path
from playerhq import views

app_name = 'playerhq'

urlpatterns = [
    path('playerhq/', views.index, name='index'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game/<slug:game_name_slug>/', views.game, name='game'),
    path('category/<slug:category_name_slug>/', views.category, name='category'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
]

