from django.urls import path
from . import views

urlpatterns = [
    # Página principal (dias / concertos)
    path('', views.lista_dias, name='lista_dias'),

    # Concerto
    path('concertos/<int:concerto_id>/', views.concerto_detail, name='concerto_detail'),
    path('concertos/<int:concerto_id>/editar/', views.editar_concerto, name='editar_concerto'),
    path('concertos/<int:concerto_id>/apagar/', views.apagar_concerto, name='apagar_concerto'),

    # Criar concerto
    path('concertos/criar/', views.criar_concerto, name='criar_concerto'),

    # Palcos
    path('palcos/', views.lista_palcos, name='lista_palcos'),
    path('palcos/<int:palco_id>/editar/', views.editar_palco, name='editar_palco'),
]