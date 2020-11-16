from django.urls import path
from pd import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'pd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    path('search/', views.search, name='search'),
    path('<slug:cat_slug_name>/', views.cat_page, name='cat_page'),
    path('<slug:cat_slug_name>/<slug:post_slug_name>/', views.posts, name='posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
