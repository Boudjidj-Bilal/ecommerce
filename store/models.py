from django.db import models

from Ecommerce.settings import AUTH_USER_MODEL

# Create your models here.



class Taille(models.Model):
    taille = models.CharField(max_length=32) # on créer un champ taille de type string avec 32 caractère maximum
    
    def __str__(self) -> str:
        return f"{self.taille}" # dans l'interface admin, on affiche les tailles


class Categorie(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self) -> str:
        return f"{self.name}" # dans l'interface admin, on affiche les tailles

class Produit(models.Model):
    name = models.CharField(max_length=128, default="")
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, default="")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}" # dans l'interface admin, on affiche les tailles


class Image_Couleur(models.Model):
    name = models.CharField(max_length=128, default="")
    image = models.ImageField(upload_to="images")
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product.name} {self.name}" # dans l'interface admin, on affiche les tailles


class Article(models.Model):
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    couleur = models.ForeignKey(Image_Couleur, on_delete=models.CASCADE)
    taille = models.ForeignKey(Taille, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    prix_unitaire = models.FloatField(default=0)
    produit_defaut = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.product.name} {self.couleur.name} {self.taille.taille}" # dans l'interface admin, on affiche les tailles




class Commande(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article) 
    information_paiement = models.CharField(default="", max_length=64)

    def __str__(self):
        return f"{self.user.username}" 



# class Pull(models.Model):
#     name = models.CharField(max_length=128) 
#     slug = models.SlugField(max_length=128) # mettre tout les caractère en minuscule et enlever les caractère spéciaux, car cela pourrais être problèmatique pour une url
#     taille = models.OneToOneField(Taille, on_delete=models.CASCADE)
#     prix = models.IntegerField(default=0) # ou floatField si on veut mettre des centimes dans le prix
#     stock = models.IntegerField(default=0) # créer un champ stock par defaut à 0
#     description = models.TextField(blank=True) # créer un champ description #blank=True pour que l'utilisateur ne soit pas obligé de mettre une description
#     image = models.ImageField(upload_to="images") # créer un champ image # null=True pour spécifier qu'on peu mettre une valeur null dans la base de donnée, upload_to nous permet de stocker ces images dans le dossier images qui se trouve dans le dossier media
#     def __str__(self) -> str:
#         return f"{self.name} {self.taille} ({self.stock})" # dans l'interface admin, pour différencier les produit on mets leur nom avec entre parenthèse leur stocks





# class Product(models.Model):
#     tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE) 
#     casquette = models.ForeignKey(Casquette, on_delete=models.CASCADE) 
#     jogging = models.ForeignKey(Jogging, on_delete=models.CASCADE) 
#     pull = models.ForeignKey(Pull, on_delete=models.CASCADE) 

#     def __str__(self) -> str:
#         return f"{self.name} ({self.stock})" # dans l'interface admin, pour différencier les produit on mets leur nom avec entre parenthèse leur stocks

    # def get_absolute_url(self):
    #     return reverse("product", kwargs={"slug": self.slug}) # le premier paramètre prend le nom de l'url(product), et en deuxième paramètre on ajoute le slug car l'url attend un paramètre slug, il nous permet de faire le liens vers la page detail d'un produit




# class Order(models.Model):
#     user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) # foreignkey: relation many to one, plusieurs articles pour un utilisateur, on recupère le model utilisateur qui lui représente dans le fichier settings en paramètre AUTH_USER_MODEL, en deuxieme argument on lui dit que si l'utilisateur suprimme son compte on va suprimer en cascade tout les élément relier à cette utilisateur(les artciles).
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)   # foreignkey: On peut avoir plusieurs produit qui sont relier à plusieurs artciles(du panier), on fait appel aux model Product car c'est un produit, en deuxieme argument on lui dit que si les produits son suprimer on va suprimer en cascade tout les artciles du panier qui représente ce produit.
#     quantity = models.IntegerField(default=1) # représente la quantité de produit voulue
#     prixOrder = models.IntegerField(default=0) # représente le prix du produits fois la quantité de produits voulue
#     ordered = models.BooleanField(default=False) # savoir si l'article a été commandé ou non 

#     def __str__(self):
#         return f"{self.product.name} ({self.quantity}) {self.prixOrder}€" # Dans l'interface admin, pour différencier les articles on mets leur nom avec entre parenthèse leur quantité


"""
(Panier) Cart
- Utilisateur
- Orders (articles)
- Commandé ou non boolean
- Date de la commande
"""


