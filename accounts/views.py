from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render



from accounts.models import Shopper

import smtplib
from email.message import EmailMessage

# Create your views here.

User = get_user_model() # récupère dans settings AUTH USER MODEL qui mène vers le model de la app account

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username") # récupère la variable du formulaire de la page signup username (name)
        password = request.POST.get("password") # récupère la variable du formulaire de la page signup password (name)
        confirmPassword = request.POST.get("confirmerPassword")
        email = request.POST.get("email")

        if confirmPassword != password:
            return render(request, 'accounts/signup.html', context={'defaultUsername': username,'defaultEmail': email, 'messageErrorMdp': "Les mots de passes ne sont pas identiques. Veuillez recomencer."})
        else:
            if Shopper.objects.filter(username=username).exists(): # si l'utilisateur existe deja dans la base de donner
                return render(request, 'accounts/signup.html', context={'defaultUsername': username,'defaultEmail': email, 'messageErrorMdp': "Ce nom d'utilisateur existe déjà. Veuillez recomencer."})
            else:
                user = Shopper.objects.create_user(username=username, password=password, email=email) # créer un utilisateur, avec en paramètre son username, son password et son email récupéré du form signup
                
                login(request, user) # login fonction django pour connecter l'utilisateur

                sendEmail(email, username)

                return redirect('index')

    else:
        return render(request, 'accounts/signup.html')






    
def login_user(request):
    if request.method=="POST":
            username = request.POST.get("username") # récupère la variable du formulaire de la page signup username (name)
            password = request.POST.get("password") # récupère la variable du formulaire de la page signup password (name)

            
            if not User.objects.filter(username=username).exists():
                return render(request, 'accounts/login.html', context={'messageError': "Le nom d'utilisateur n'existe pas. Veuillez recommencer."})
            else:
                user = authenticate(username=username, password=password) # On connecte l'utilisateur, cela nous permet de vérifier que les information son bonne 
                if user: # si les informations son bonne
                    login(request, user) # login fonction django pour connecter l'utilisateur
                    return redirect('index')
                else:
                    return render(request, 'accounts/login.html', {'messageError': "Le mot de passe pour l'utilisateur "+username+" est incorrect! Veuillez recomencer."})
    else:
        return render(request, 'accounts/login.html')    















def logout_user(request):
    logout(request) # logout fonction django pour deconecter l'urtilisateur
    return redirect('index')





def sendEmail(emailDestinataire, user):
    pass
