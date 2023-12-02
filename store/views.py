from store.models import Article, Image_Couleur, Produit, Taille
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    article_listes_defaut = Article.objects.filter(produit_defaut=True) # récupère tout les produits du model Product dans la variable products


    # on verifie si la somme des stocks des articles d'un produit est supérieur à 0

    return render(request, 'store/index.html', context={"article_listes_defaut":article_listes_defaut}) # retourne la page index.html avec en paramètre tout les produits dans la variable de type dictionnaire products

# def tshirtDetail(request, slug):
#     # products = get_object_or_404(Product.tshirt)
#     product = get_object_or_404(Tshirt, slug=slug)
#     products = Tshirt
#     return render(request, 'store/detail.html', context={"product":product, "products":products})



def cart(request):    
    return render(request, 'store/cart.html') # en paramètre on lui envoie tout les orders (articles) de l'utilisateur qui a fait la requette


def detailProduct(request, productId, articleId):
    # product = Produit.objects.filter(id=productId)

    # articleTest = Article.objects.filter(product__id = productId)
    # articleLenght = len(articleTest)

    articles_liste = Article.objects.all() # liste des articles
    articles_product = []
    for article in articles_liste:
        if article.product.id == productId:
            articles_product.append(article) # ajoute un élément dans le tableau

    # articleLen = len(articles_product)

    article = Article.objects.get(id=articleId)
    # couleur_liste = set(articles_product.couleur)
    couleur_liste = []
    for articleC in articles_product: 
        couleur_liste.append(articleC.couleur) 
    couleur_liste_sans_doublon = set(couleur_liste)
    return render(request, 'store/detail.html', context={"article":article, "articles_product":articles_product, "couleur_liste":couleur_liste_sans_doublon})


def ChoixCouleurOuTaille(couleurId, tailleId, productId):

    couleur = Image_Couleur.objects.get(id=couleurId)
    taille = Taille.objects.get(id=tailleId)

    article = Article.objects.get(couleur=couleur, taille=taille) 
    articleId = article.id

    return redirect('detail', productId=productId , articleId=articleId)








# def choixCouleurArticle(request, idCouleur, idArticle):
#     article = Article.objects.filter(id=idArticle)
#     couleur = Image_Couleur.objects.filter(id=idCouleur) # récupère tout les produits du model Product dans la variable products

# if article == product_defaut or article.couleur = couleur

# def add_to_cart(request, slug):
    # si l'utilisateur n'a pas de panier, créer le panier et ajouter l'élément dans ce panier
    # si l'utilisateur a deja un panier et que l'article existe deja dans son panier, modifier juste la quantité de l'article en l'incrémentant de 1
    # user = request.user # on récupère l'urilisateur car on en auras besoin plusieurs fois dans cette views
    # product = get_object_or_404(Product, slug=slug) # récupère le produit en question Product models grâce à son slug(deuxieme paramètre), on utilise get_object_or_404 au cas ou le produit n'existe pas, si il n'existe ps alors on ne vas pas plus loin dans le programme

    # cart, _ = Cart.objects.get_or_create(user=user) # récupérer le panier de l'utilisateur, on utilise la méthode get_or_create qui nous permet de créer un élément si il n'existe pas et de le récupérer si il existe, on lui met en paramètre l'utilisateur pour associé le panier à son utilisateur, on lui affecte deux variables car deux valeur: l'objet en question et également une information pour savoir si l'objet a été créer ou non.
    # on utilise un tiret du bas car on a pas besoin de cette information (si l'objet a été crée ou non), (c'est une convention)
    # donc cela veut dire que: si un utilisateur possède deja un panier, alors on ne fait rien, sinon on créer le panier pour cet utilisateur


    # order, created = Order.objects.get_or_create(user=user, product=product, ordered=False,) # Récupérer l'articles qui va être dans le panier de l'utilisateur, on utilise la méthode get_or_create qui nous permet de créer un élément si il n'existe pas et de le récupérer si il existe, on lui met en paramètre l'utilisateur pour associé l'artciles à son utilisateur et le produit qu'on a récupéré, on lui affecte deux variables car deux valeur: l'objet en question et également une information pour savoir si l'objet a été créer ou non.
    # Ici nous avons belle et bien besoin de cette information, donc nous l'a mettons dans une variable created
    # Donc cela veut dire que: si un objet contient dans le panier, le même utilisateur et le même produit, et que cette article n'a pas deja été commendé, alors on va seulement l'incrémenter et created = false, sinon on va le créer et created = true

    # if created == True: # Si l'objet viens d'être créer donc il n'existe pas deja dans le panier:
    #     # lorsqu'on créer l'order (l'article) dans le panier, dans le model Cart on dit que sa quantité est 1 par defaut
    #     prixArticle = order.product.prix
    #     order.prixOrder = prixArticle
    #     order.save()
        
    #     cart.orders.add(order) # Ici on récupère cart qui représente le panier de l'utilisateur récupérer un peu plus haut, orders représente le champs orders dans le model Cart, order représente l'objet que l'on vient de créer, on lui applique add pour le créer
        
    #     orders = cart.orders.all()
    #     total = cart.total
    #     for order in orders:
    #         total = total+order.prixOrder
    #     cart.total = total
    #     cart.save() # On sauvegarde le panier (cart)
    # else: # sinon, c'est qu'il existe déjà dans le panier, alors:
    #     order.quantity = order.quantity + 1 # On incrémente la quantité de l'article (quantity récupérer du model Order)
    #     NewprixArticle = order.product.prix * order.quantity
    #     order.prixOrder = NewprixArticle
    #     order.save() # On sauvegarde l'article


    #     orders = cart.orders.all()
    #     # if orders.count() == 1:
    #     #     total = cart.total
    #     # else:
    #     #     total = 0
    #     total = 0
    #     for order in orders:
    #         total = total+order.prixOrder

    #     cart.total = total
    #     cart.save() # On sauvegarde le panier (cart)


    #     # le problème est peut-être à cause du ordered et de la date order qui stock dans le model Carte les anciens order 


    # return redirect(reverse("product", kwargs={"slug": slug})) # L'url de product attend en paramètre un slug, on redirige vers la page du détail du produit



# def delete_cart(request):
#     cart = request.user.cart # récupère le panier de l'utilisateur (model=Cart)
#     if cart: # si le panier existe
    # ici au lieu de coder les deux lignes du dessus on aurais les assemblé en une seule ligne: if cart := request.user.cart:
        # cart.orders.all().delete() # récupère tout les articles (orders) qui se trouve à l'intérieur grace à cart.orders.all() (orders champs du model Cart), et suprime les artciles récupéré
    #     cart.orders.all().delete() # récupère le panier et suprime le avec la fonction delete() dans le model Cart
    #     cart.delete()
    # return redirect('index') # retourne à la page principal
