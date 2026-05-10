import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer le token Discord depuis les variables d'environnement
TOKEN = os.getenv('DISCORD_TOKEN')

# Vérifier si le token est défini
if TOKEN is None:
    print("Erreur : Le token Discord n'est pas défini dans le fichier .env")
    exit(1)

# Créer une instance du bot avec un préfixe de commande '!'
# intents sont nécessaires pour certaines fonctionnalités
intents = discord.Intents.default()
intents.message_content = True  # Permet au bot de lire le contenu des messages

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    """
    Charge tous les cogs (extensions) du bot.
    """
    await bot.load_extension('help_cog')
    await bot.load_extension('general')
    await bot.load_extension('moderation')

@bot.event
async def on_ready():
    """
    Événement appelé lorsque le bot est prêt et connecté à Discord.
    """
    print(f'Bot connecté en tant que {bot.user}')
    print('Prêt à recevoir des commandes !')
    await load_cogs()  # Charger les cogs après connexion

# Gestion des erreurs
@bot.event
async def on_command_error(ctx, error):
    """
    Gestionnaire d'erreurs pour les commandes.
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande inconnue. Utilisez `!help` pour voir les commandes disponibles.")
    else:
        print(f"Erreur : {error}")

# Lancer le bot
if __name__ == "__main__":
    bot.run(TOKEN)