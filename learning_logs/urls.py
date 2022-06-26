"""Define padrões de URL para learning_logs"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # página inicial
    url(r'^$', views.index, name='index'),
    url(r"^topics/$", views.topics, name='topics'),
    # página de detalhes para um único assunto
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
