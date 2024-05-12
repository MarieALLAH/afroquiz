# Jeux de Quiz sur la Culture Noire :
# Développez un jeu de quiz interactif qui teste les connaissances des utilisateurs sur la culture noire, l'histoire africaine et la musique afro.

# Etape 1
# Créer une grande liste, dans laquelle il y a 3 dictionnaires appelés "questions".
# Pour chaque dictionnaire (question) dans la liste, il y a trois paires clé-valeur :
# 'question': Cette clé contient le texte de la question.
# 'options': Cette clé contient une liste des options de réponse possibles à la question.
# 'correct_answer': Cette clé contient la réponse correcte à la question.

questions = [
    {
        'question': "Quelle danse traditionnelle originaire du Brésil est associée à la culture afro-brésilienne?",
        'options': ["Samba", "Tango", "Flamenco", "Cha-Cha-Cha"],
        'correct_answer': "Samba"
    },
    {
        'question': "Quel est le nom du mouvement artistique et culturel qui a émergé dans les années 1920 à Harlem, New York, mettant en avant la culture noire?",
        'options': ["Cubisme", "Renaissance Harlem", "Impressionnisme", "Surréalisme"],
        'correct_answer': "Renaissance Harlem"
    },
    {
        'question': "Qui est la légendaire chanteuse de soul surnommée 'Queen of Soul'?",
        'options': ["Ella Fitzgerald", "Diana Ross", "Aretha Franklin", "Whitney Houston"],
        'correct_answer': "Aretha Franklin"
    }
]

# Etape 2 : Dans la deuxième étape, afficher le texte de la question, suivi de toutes ses options de réponse à l'utilisateur.

# Définition de la fonction afficher_question
def afficher_question(question):
    print(f"Question: {question['question']}")  # Cette ligne utilise une f-string pour afficher le texte de la question à l'utilisateur. La clé 'question' dans le dictionnaire question contient le texte de la question.
    afficher_reponses(question['options'])  # Cette ligne appelle la fonction afficher_reponses(options) avec les options de réponse de la question actuelle. Cela affiche ensuite toutes les options de réponse à la question.

# Cette fonction affiche chaque option de réponse avec son numéro à l'utilisateur.
def afficher_reponses(options):
    for i, option in enumerate(options, 1):  # Cette ligne parcourt chaque option dans la liste options, en attribuant un numéro i à chaque option, en commençant par 1.
        print(f"{i}. {option}")  # Cette ligne affiche chaque option avec son numéro correspondant à l'utilisateur.

# Parcourt chaque question dans la liste questions et appelle la fonction afficher_question(question) pour afficher chaque question avec ses options de réponse à l'utilisateur.
for question in questions:  # Cette ligne crée une boucle for qui parcourt chaque élément (dictionnaire représentant une question) dans la liste questions.
    afficher_question(question)  # Cette ligne appelle la fonction afficher_question pour chaque question dans la liste questions. Cela affiche le texte de chaque question avec ses options de réponse à l'utilisateur.


#Etape 3 : Gestion des réponses :
 # Saisie utilisateur : Utilise la fonction input pour permettre à l'utilisateur de saisir sa réponse.
    # La fonction gerer_reponse(question) sert a poser chaque question du jeu de quiz et gérer les réponses des utilisateurs
    
def gerer_reponse(question):
    afficher_reponses(question['options'])  # # Cette ligne affiche les différentes options de réponse disponibles pour la question en cours.
    reponse_utilisateur = input("Entrez le numéro de votre réponse : ") #  demande à l'utilisateur de choisir une réponse en saisissant le numéro correspondant à son choix, puis stocke cette réponse dans la variable reponse_utilisateur.

    if reponse_utilisateur.isdigit(): # vérifie si la réponse de l'utilisateur est composée uniquement de chiffres. , Elle (isdigit) est utilisée pour vérifier si tous les caractères de la chaîne sont des chiffres
        choix_utilisateur = int(reponse_utilisateur) - 1  # convertit la réponse de l'utilisateur en un nombre entier et soustrait 1 pour obtenir l'indice correspondant dans la liste des options de réponse (car les listes Python commencent à l'indice 0).
        if 0 <= choix_utilisateur < len(question['options']): #vérifie si l'indice de la réponse de l'utilisateur est valide par rapport à la liste des options de réponse pour la question donnée.
            if question['options'][choix_utilisateur] == question['correct_answer']:#  Cette ligne vérifie si la réponse de l'utilisateur correspond à la réponse correcte pour la question donnée.
                print("Bonne réponse!") # Si la réponse de l'utilisateur est correcte, cette ligne affiche "Bonne réponse!".
            else: # Si la réponse de l'utilisateur est incorrecte, cette ligne exécute le bloc de code suivant.
                print(f"Mauvaise réponse. La réponse correcte est : {question['correct_answer']}") #Cette ligne affiche un message indiquant que la réponse de l'utilisateur est incorrecte, en indiquant également la réponse correcte à la question.
        else: #Si l'indice de la réponse de l'utilisateur n'est pas valide (c'est-à-dire qu'il n'est pas dans la plage des indices valides des options de réponse), cette ligne exécute le bloc de code suivant.
            print("Numéro de réponse invalide.") #Cette ligne affiche un message indiquant que le numéro de réponse fourni par l'utilisateur est invalide.
    else: #Si la réponse de l'utilisateur n'est pas un nombre (c'est-à-dire qu'elle ne contient pas que des chiffres), cette ligne exécute le bloc de code suivant.
        print("Veuillez entrer un nombre.") # Cette ligne affiche un message demandant à l'utilisateur d'entrer un nombre valide.

# Enfin, la boucle for parcourt chaque question dans la liste questions, 
#affiche la question avec ses options à l'utilisateur, puis appelle la fonction gerer_reponse pour gérer la réponse de l'utilisateur à cette question.
for question in questions:
    afficher_question(question)
    gerer_reponse(question)