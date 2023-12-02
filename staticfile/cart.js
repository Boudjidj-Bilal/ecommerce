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

function AfficheProductCart(){ 
    let basket = getBasket(); // appel la fonction getBasket() qui récupère le panier et affecte la a la variable basket
    let balisePrincipalProduits = document.getElementById("produits"); // récupère la balise qui contient l'id produits dans la page html
    for(let product of basket) // fait une boucle sur chaque élément(product) du panier(basket), product représente à chaque boucle un produit du panier(basket)
    {
        console.log(product)


//      div produit:
        var newDivProduit = document.createElement("div"); //créer une balise div dans le html
        newDivProduit.setAttribute("id",product.id); // ajoute à la div un attribut id qui représente l'id du produit
        newDivProduit.classList.add("produit"); // ajoute à la div un attribus class (pour le css) qui ce nomme produit


        // h2 name
        var newBaliseNameProduct = document.createElement("h2"); //créer une balise h2 dans le html
        newBaliseNameProduct.innerHTML = product.name; // dans la balise h2 que l'on viens de créer, on lui donne comme texte le name du product
        newDivProduit.appendChild(newBaliseNameProduct); // ajoute la balise newBaliseNameProduct (qui représente h2 product.name) dans la div newDivProduit 


        // img
        var newBaliseImageProduct = document.createElement("img"); //créer une balise img dans le html
        newBaliseImageProduct.src= MEDIA_URL+product.image; // on ajoute à cette balise img un attribus source qui pointe vers l'url de l'image (product.image)
        newBaliseImageProduct.classList.add("image"); // ajoute à la balise img un attribus class (pour le css) qui ce nomme image
        newDivProduit.appendChild(newBaliseImageProduct); // ajoute la balise newBaliseImageProduct (qui représente img product.image) dans la div newDivProduit 


        
        // p quantity

        var newBaliseQuantityProduct = document.createElement("input"); //créer une balise img dans le html
        newBaliseQuantityProduct.type = "number"; // dans la balise h2 que l'on viens de créer, on lui donne comme texte le name du product
        newBaliseQuantityProduct.min = 1;
        newBaliseQuantityProduct.max = product.stock;
        newBaliseQuantityProduct.default = product.quantity;
        newBaliseQuantityProduct.classList.add("quantity"); // ajoute à la balise img un attribus class (pour le css) qui ce nomme image
        newBaliseQuantityProduct.setAttribute("id",product.slug)
        newDivProduit.appendChild(newBaliseQuantityProduct); // ajoute la balise newBaliseImageProduct (qui représente img product.image) dans la div newDivProduit 




        // p prix



        // prix 
        var newBalisePrixProduct = document.createElement("p"); //créer une balise img dans le html
        newBalisePrixProduct.innerHTML = "€"+product.prix; // dans la balise h2 que l'on viens de créer, on lui donne comme texte le name du product
        newBalisePrixProduct.classList.add("prix"); // ajoute à la balise img un attribus class (pour le css) qui ce nomme image
        newDivProduit.appendChild(newBalisePrixProduct); // ajoute la balise newBaliseImageProduct (qui représente img product.image) dans la div newDivProduit 

        // total

        // button qui appel la fonction removeFromBasket avec en parametre l'id


        var newButtonRemoveProduct = document.createElement("button"); //créer une balise button dans le html

        newButtonRemoveProduct.addEventListener("click", function() {removeFromBasket(product)}) // ajoute au boutton un événement click qui mène à la fonction removeFromBasket

        newButtonRemoveProduct.innerHTML = "Suprimer l'artcile"; // dans la balise button que l'on viens de créer, on lui donne comme texte "Suprimer l'artcile"
        newDivProduit.appendChild(newButtonRemoveProduct); // ajoute la balise newButtonRemoveProduct (qui représente button) dans la div newDivProduit 





        balisePrincipalProduits.appendChild(newDivProduit); // ajoute la div newDivProduit avec toute les balise qui y sont à l'intérieur dans la div principal balisePrincipalProduits (balise avec l'id #produits)
    }

    // let foundProduct = basket.find(p => p.id == basket.product.id) // find permet d'aller chercher un élément d'un tableau par rapport à une condition, si il trouve un élément il retourne l'élément en question, sinon undefined
}


function totalPrixCart(){
    let total = 0;
    return total;
}

function prixProduct(prix){

}

AfficheProductCart() // on appel la fonction AfficheProductCart() dans la même page pour qu'elle se lance automatiquement au chargement de la page
