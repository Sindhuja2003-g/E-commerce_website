from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.cart,name='cart'),
    path('myorders/',views.orders,name='orders'),
    path('categories/',views.categories,name='categories'),
    path('fastrack/',views.fastrack,name='fastrack'),
    path('titan/',views.titan,name='titan'),
    path('sonata/',views.sonata,name='sonata'),
    path('kenneth/',views.kenneth,name='kenneth'),
    path('anne/',views.anne,name='anne'),
    path('edge/',views.edge,name='edge'),
    path('nebula/',views.nebula,name='nebula'),
    path('maritime/',views.maritime,name='maritime'),
     path('categories/men/',views.men,name='men'),
    path('categories/women/',views.women,name='women'),
    path('cart/',views.cart,name="cart")
]