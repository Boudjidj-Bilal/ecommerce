from django.contrib import admin
from store.models import Produit, Taille, Categorie, Image_Couleur, Article, Commande



# Register your models here.
# admin.site.register(Order) # représente les éléments order (artciles) que l'on souhaite afficher du coté admin
# admin.site.register(Tshirt) # représente les éléments TailleDisponible (tailles disponible d'un produit) que l'on souhaite afficher du coté admin
# admin.site.register(Casquette) # représente les éléments TailleProduct (taille d'un produit) que l'on souhaite afficher du coté admin
# admin.site.register(Jogging) # représente les éléments TailleProduct (taille d'un produit) que l'on souhaite afficher du coté admin
# admin.site.register(Pull) # représente les éléments TailleProduct (taille d'un produit) que l'on souhaite afficher du coté admin


admin.site.register(Taille) # représente les éléments Taille (taille) que l'on souhaite afficher du coté admin
admin.site.register(Produit) # représente les éléments produits que l'on souhaite afficher du coté admin
admin.site.register(Categorie) 
admin.site.register(Image_Couleur) 
admin.site.register(Article) 
admin.site.register(Commande) 

