function saveBasket(basket){ // sauvegarde du panier basket dans le local storage de type Json
    localStorage.setItem("basket",JSON.stringify(basket)); // On transforme le tableau en format JSON(chaine de caractère),car dans le local storage on ne peut que utiliser des donnée simple comme une chaine de caractère
}

function getBasket(){ // récupérer les valeur du panier basket
    let basket = localStorage.getItem("basket"); // On le récupère avec JSON.parse() pour le remettre sous forme de donnée complexe (tableau)
    if(basket==null) // basket == null veut dire si le panier est vide
    {
        return []; // on lui retourne un tableau vide
    }
    else
    {
        return JSON.parse(basket); // sinon on lui retourne le panier, on utilise json.parse pour mettre sous forme json le pannier dans le local storage car il ne supporte pas les tableau ainsi que les types complexe, cela reviens à convertir le tableau en une chaine de caractère
    }
}

function addBasket(product){ // ajouter le produit dans le panier (tableau)
    let basket = getBasket(); // On récupère le panier stocker dans le local storage
    let foundProduct = basket.find(p => p.id == product.id) // find permet d'aller chercher un élément d'un tableau par rapport à une condition, si il trouve un élément il retourne l'élément en question, sinon undefined
    // si il y a un produit dans le tableau (panier) d'ont l'id est égal à l'id du produit product (paramètre de la fonction addBasket) que l'on veut ajouter
    // p représente chaque valeur (produit) du tableau (panier), chaque valeur possède un id, on verrifie si l'un d'entre eux possède le même id que celui qu'on souhaite ajouter 

    if(foundProduct != undefined) // si il est différent de undefined, cela veut dire qu'il existe déjà dans le panier 
    {
        foundProduct.quantity++; // on incrémente de +1 la quantité
    }
    else // sinon c'est qu'il n'existe pas
    {
        product.quantity = 1; // On initialise la quantité du produit à 1
        basket.push(product); // On ajoute le produit au panier
    }
    saveBasket(basket); // On enregistre le panier dans le local storage
    modifierNombrePanier(); // On modifie le nombre d'élément dans le panier (dans le menu à coté de l'icone panier)
}


function removeFromBasket(product){
    let basket = getBasket();
    // filter: méthode qui filtre un tableau par rapport à une condition
    basket = basket.filter(p => p.id != product.id); // ici on garde tout les produits sauf celui qui est égal à l'id du produit que l'ont souhaite suprimer 
    // p représente chaque valeur (produit) du tableau (panier), chaque valeur possède un id, on verrifie si ils possèdent pas le même id que celui qu'on souhaite suprimer
    
    saveBasket(basket); // On enregistre le panier dans le local storage, sans le produit que l'ont souahite suprimmer
    

    let idProduct = document.getElementById(product.id); // on récupère

    idProduct.remove() // on suprime la balise qui contient l'id product.id coté html
    modifierNombrePanier(); // On modifie le nombre d'élément dans le panier (dans le menu à coté de l'icone panier)

    nbProductInBasket = getNumberProduct(); // on appel la fonction getNumberProduct() qui retourne le nombre de produit dans le panier
    if(nbProductInBasket == 0) // si nbProductInBasket cela veut dire qu'il n'ya aucun produit dans le panier
    {
        let balisePrincipalProduits = document.getElementById("produits"); // on récupère la balise (div) avec l'id produits


        var newBaliseCartVide = document.createElement("h2"); //créer une balise h2 dans le html
        newBaliseCartVide.innerHTML = "le panier est vide..."; // dans la balise h2 que l'on viens de créer, on lui donne comme texte 
        balisePrincipalProduits.appendChild(newBaliseCartVide); // ajoute la balise newBaliseCartVide (qui représente h2 ) dans la div balisePrincipalProduits
    }
}


function changeQuantity(product,quantity){
    let basket = getBasket(); // On récupère le panier stocker dans le local storage
    let foundProduct = basket.find(p => p.id == product.id); // find permet d'aller chercher un élément d'un tableau par rapport à une condition, si il trouve un élément il retourne l'élément en question, sinon undefined
    // si il y a un produit dans le tableau (panier) d'ont l'id est égal à l'id du produit product (paramètre de la fonction addBasket) que l'on veut ajouter
    // p représente chaque valeur (produit) du tableau (panier), chaque valeur possède un id, on verrifie si l'un d'entre eux possède le même id que celui qu'on souhaite ajouter 

    if(foundProduct != undefined) // si il est différent de undefined, cela veut dire qu'il existe déjà dans le panier 
    {
        foundProduct.quantity += quantity; // récupère le produit q
        if(foundProduct.quantity <= 0) // si la quantité du produit est inférieur ou égal à 0
        {
            removeFromBasket(foundProduct); // alors on le supprime avec la fonction removeFromBasket 
        }
        else // sinon
        {
            saveBasket(basket); // on sauvegarde sa nouvelle quantité dans le tableau grace à la variable saveBasket
        }
    }   
}

function getNumberArticle(){
    let basket = getBasket(); // appel la fonction getBasket() qui récupère le panier et affecte la a la variable basket
    let numberArticle = 0; // initialise la variable numberArticle à 0
    for(let product of basket){ // fait une boucle sur chaque produit du panier 
        numberArticle += product.quantity; // ajoute la quantité de tout les produits à la variable numberArticle
    }
    return numberArticle; // retourne la variable numberArticle qui contient le nombre de
}

function getNumberProduct(){
    let basket = getBasket(); // appel la fonction getBasket() qui récupère le panier et affecte la a la variable basket
    let numberProduct = basket.length; // récupère le nombre d'élément(produit) du panier et affecte le à la variable numberProduct
    return numberProduct; // retourne le nombre d'élément dans le panier 
}

function modifierNombrePanier(){
    let nbPanier = getNumberProduct(); // récupère le nombre d'élément dans le panier grâce à la fonction getNumberProduct()
    let baliseAPanier = document.getElementById("nbProductCart"); // récupère la balise (a) avec l'id nbProductCart
    if (nbPanier == 0) // si il le nbPanier = 0 cela veut dire qu'il n'y a aucun éléments dans le panier
    {
        baliseAPanier.innerHTML = "(0)"; // dans la balise h2 que l'on viens de créer, on lui donne comme texte le name du product
    }
    else // sinon il y a des éléments dans le panier, donc:
    {
        // baliseAPanier.title = "(" + nbPanier + ")";
        baliseAPanier.innerHTML = "("+ nbPanier +")"; // on ajoute dans la balise (a) récupérer le nombre entre parenthèse d'élément dans le panier
        baliseAPanier.href = "http://127.0.0.1:8000/cart/"; // TROUVER UNE SOLUTION POUR RECUPERER L'URL DU PANIER SANS LA METTRE EN DUR, on créer un lien href vers l'url suivante sur la balise récupéré
    }
        
}



modifierNombrePanier(); // on appel la fonction modifierNombrePanier() dans la même page pour qu'elle se lance automatiquement au chargement de la page


