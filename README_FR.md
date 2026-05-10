# Tutoriel Bot Discord - Francais

[Retour au Menu](README.md) | [English Version](README_EN.md)

## Apercu

Ceci est un template complet de bot Discord construit avec Python et discord.py. Il inclut une architecture modulaire de commandes, des outils de moderation, la gestion de salons, et les meilleures pratiques de securite.

## Prerequis

- Python 3.8 ou plus recent
- Un compte Discord
- Un serveur Discord pour les tests
- VS Code ou tout autre editeur de texte
- Connaissances basiques en Python

## Etape 1: Configuration Discord Developer

### Creer une Application
1. Allez sur https://discord.com/developers/applications
2. Cliquez sur "New Application"
3. Entrez le nom de votre bot et cliquez sur "Create"
4. Copiez l'ID d'application

### Creer l'Utilisateur Bot
1. Allez dans l'onglet "Bot"
2. Cliquez sur "Add Bot"
3. Copiez votre token (gardez-le secret!)

### Inviter le Bot au Serveur
1. Allez dans "OAuth2" > "URL Generator"
2. Selectionnez "bot" dans les scopes
3. Selectionnez les permissions necessaires (Send Messages, Read Messages, Manage Channels, etc.)
4. Ouvrez l'URL generee pour inviter le bot

## Etape 2: Configuration du Projet

### Creer la Structure du Projet
```
mon_bot_discord/
    main.py
    general.py
    moderation.py
    channels.py
    help_cog.py
    requirements.txt
    .env
    .gitignore
```

### Installer les Dependances
```bash
pip install -r requirements.txt
```

Fichier: requirements.txt
```
discord.py==2.3.2
python-dotenv==1.0.0
```

### Configurer le Token
Creez un fichier `.env`:
```
DISCORD_TOKEN=votre_token_ici
```

## Etape 3: Comprendre la Structure du Bot

### Point d'Entree Principal (main.py)
Le fichier main.py:
- Charge les variables d'environnement du fichier .env
- Cree l'instance du bot
- Charge tous les cogs quand le bot est pret
- Gere les erreurs globales

### Systeme de Cogs
Chaque cog est un module separe contenant des commandes liees:
- general.py: Commandes basiques (ping, hello, info)
- moderation.py: Commandes de moderation (kick, ban, mute, etc.)
- channels.py: Gestion de salons (lock, unlock)
- help_cog.py: Systeme d'aide personnalise

## Commandes Disponibles

### Commandes Generales
- `!ping` - Le bot repond avec "Pong!"
- `!hello` - Le bot salue l'utilisateur
- `!info` - Affiche les informations du serveur (membres, date de creation, proprietaire)

### Commandes de Moderation
- `!kick @membre [raison]` - Expulse un membre du serveur
- `!ban @membre [raison]` - Bannit definitivement un membre
- `!unban nom#tag` - Debanni un membre precedemment banni
- `!mute @membre [raison]` - Rend un membre muet (necessite le role "Muted")
- `!unmute @membre [raison]` - Rend un membre non-muet

### Commandes de Gestion de Salons
- `!lock [#salon]` - Verrouille un salon (personne ne peut ecrire)
- `!unlock [#salon]` - Deverrouille un salon
- `!lockall` - Verrouille tous les salons du serveur
- `!unlockall` - Deverrouille tous les salons du serveur

### Commandes d'Aide
- `!help` - Affiche toutes les commandes disponibles
- `!help <commande>` - Affiche l'aide pour une commande specifique
- `!help <categorie>` - Affiche l'aide pour une categorie de commandes

## Comment Lancer

1. Activez l'environnement virtuel (si vous en utilisez un)
2. Lancez: `python main.py`
3. Verifiez dans la console "Bot connected as [NomDuBot]"
4. Testez les commandes sur votre serveur Discord

## Comprendre Chaque Commande

Pour des explications detaillees sur le fonctionnement interne de chaque commande, consultez:
[TUTORIEL_BOT_DISCORD_FR_DETAILLE.pdf](TUTORIEL_BOT_DISCORD_FR_DETAILLE.pdf)

Ce PDF inclut:
- Instructions d'installation etape par etape
- Comment chaque commande est implementee
- Comprendre les Cogs et les permissions
- Bonnes pratiques de securite
- Idees pour etendre le bot

## Bonnes Pratiques de Securite

1. Ne codez jamais votre token en dur
2. Utilisez toujours des fichiers .env pour les donnees sensibles
3. Ajoutez .env a .gitignore
4. Utilisez des variables d'environnement pour toutes les donnees sensibles
5. Limitez les permissions du bot a ce qui est reellement necessaire
6. Regenerez le token s'il est compromis
7. Testez sur un serveur prive avant la production

## Personnalisation

Chaque cog peut etre facilement modifie ou etendu:

### Ajouter une Nouvelle Commande
```python
@commands.command()
async def macommande(self, ctx):
    """Description de ma commande personnalisee"""
    await ctx.send("Bonjour!")
```

### Ajouter une Verification de Permissions
```python
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member):
    # Votre code de commande
```

## Depannage

### Le bot ne repond pas
- Verifiez que le token est correct dans .env
- Verifiez que le bot est invite au serveur
- Verifiez les permissions du bot sur le serveur

### Les commandes ne fonctionnent pas
- Utilisez `!help` pour voir les commandes disponibles
- Assurez-vous d'avoir les permissions requises
- Verifiez que le bot a les permissions Discord necessaires

### Erreurs de permissions
- Assurez-vous que le bot a un role plus eleve que le membre cible
- Verifiez les permissions du salon
- Verifiez que le token du bot a les bons scopes

## Ressources

- [Documentation discord.py](https://discordpy.readthedocs.io/)
- [Documentation Discord Developer](https://discord.com/developers/docs)
- [Documentation Officielle Python](https://docs.python.org/3/)

## Ameliorations Futures

Idees pour etendre votre bot:
- Messages de bienvenue pour les nouveaux membres
- Systeme de journalisation pour les actions de moderation
- Commandes amusantes (blague, citation, etc.)
- Integration de bases de donnees
- Moderation automatisee (detection de spam)
- Systeme d'attribution de roles
- Reactions a des messages
- Taches programmees

## Licence

Ce projet est open source et disponible a des fins educatives.

