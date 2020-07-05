from django.urls import path
from .views import (rubrics_list,
                    post_of_rubric,
                    index,
                    posts_list,
                    )
app_name = 'mapp'

urlpatterns = [
    path('', index, name='index'),
    path('rubric/', rubrics_list, name='rubrics_list'),
    path('rubric/<slug>', post_of_rubric, name='post_of_rubric'),
    path('posts/', posts_list, name='all_posts'),
]
