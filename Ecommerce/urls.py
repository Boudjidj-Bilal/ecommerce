"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login_user, logout_user, signup
from store.views import index, cart, detailProduct, ChoixCouleurOuTaille


from django.conf.urls.static import static

from Ecommerce import settings

urlpatterns = [
    path('', index, name='index'), # page par defaut
    path('admin/', admin.site.urls),
    path('product/<int:productId>/<int:articleId>/', detailProduct, name='detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('choixArticle/<int:CouleurId>/<int:tailleId>/<int:productId>/', ChoixCouleurOuTaille, name='choixArticle'),
    path('cart/', cart, name='cart'),


    # ajouter la fonctionnalité pour augmenter ou diminuer la quantité des articles
    # ajouter une fonctionnalité qui stipule qu'on ne peux commander plus de produit qu'il y en a en stock
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # On donne le chemin d'accès vers le dossier media pour que les images puisse être stocké dedans

