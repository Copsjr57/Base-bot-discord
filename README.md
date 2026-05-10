# bot_discord_tuto
# Tutoriel pour créer un bot Discord en Python

## Prérequis
- Python 3.8 ou plus récent
- Un compte Discord
- Un serveur Discord pour tester le bot

## Étape 1 : Créer une application Discord
1. Allez sur le [Portail des Développeurs Discord](https://discord.com/developers/applications)
2. Cliquez sur "New Application" et donnez un nom à votre bot
3. Dans l'onglet "Bot", cliquez sur "Add Bot"
4. Copiez le "Token" du bot (gardez-le secret !)

## Étape 2 : Inviter le bot sur votre serveur
1. Dans l'onglet "OAuth2" > "URL Generator"
2. Sélectionnez "bot" dans les scopes
3. Sélectionnez les permissions nécessaires (par exemple : Send Messages, Read Messages)
4. Copiez l'URL générée et ouvrez-la dans votre navigateur pour inviter le bot

## Étape 3 : Configuration du projet
1. Clonez ce repo ou téléchargez les fichiers
2. Créez un environnement virtuel : `python -m venv venv`
3. Activez l'environnement : `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
4. Installez les dépendances : `pip install -r requirements.txt`

## Étape 4 : Configuration du token
1. Créez un fichier `.env` dans le même dossier que `main.py`
2. Ajoutez votre token : `DISCORD_TOKEN=votre_token_ici`

## Étape 5 : Lancer le bot
Exécutez : `python main.py`

## Commandes disponibles
Utilisez `!help` pour voir toutes les commandes automatiquement mises à jour.

### Commandes générales
- `!ping` : Répond "Pong!"
- `!hello` : Dit bonjour à l'utilisateur
- `!info` : Donne des infos sur le serveur

### Commandes de modération (nécessitent des permissions)
- `!kick @membre [raison]` : Expulse un membre
- `!ban @membre [raison]` : Banni un membre
- `!unban nom#tag` : Débanni un membre
- `!mute @membre [raison]` : Rend un membre muet (nécessite un rôle "Muted")
- `!unmute @membre [raison]` : Rend un membre non-muet

### Aide
- `!help` : Affiche l'aide générale
- `!help <commande>` : Aide pour une commande spécifique
- `!help <catégorie>` : Aide pour une catégorie de commandes

## Structure du projet
- `main.py` : Fichier principal du bot
- `general.py` : Cog pour les commandes générales
- `moderation.py` : Cog pour les commandes de modération
- `help_cog.py` : Cog pour l'aide personnalisée et automatique
- `requirements.txt` : Dépendances Python
- `.env.example` : Exemple de fichier de configuration
- `README.md` : Ce fichier

## Personnalisation
Modifiez les fichiers `.py` pour ajouter vos propres commandes. Chaque cog est indépendant, ce qui facilite l'ajout de nouvelles fonctionnalités. Consultez la documentation de discord.py pour plus d'idées.

## Sécurité
- Ne partagez jamais votre token Discord
- Utilisez un fichier `.env` pour stocker les secrets
- Ajoutez `.env` à votre `.gitignore`

## Ressources
- [Documentation discord.py](https://discordpy.readthedocs.io/)
- [Guide officiel Discord](https://discord.com/developers/docs/intro)