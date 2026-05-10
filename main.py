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

@bot.event
async def on_ready():
    """
    Événement appelé lorsque le bot est prêt et connecté à Discord.
    """
    print(f'Bot connecté en tant que {bot.user}')
    print('Prêt à recevoir des commandes !')

@bot.command()
async def ping(ctx):
    """
    Commande simple qui répond "Pong!" pour tester si le bot fonctionne.
    """
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    """
    Commande qui salue l'utilisateur qui l'a appelée.
    """
    await ctx.send(f'Salut {ctx.author.mention} ! Comment ça va ?')

@bot.command()
async def info(ctx):
    """
    Commande qui donne des informations sur le serveur Discord.
    """
    server = ctx.guild
    embed = discord.Embed(
        title=f"Informations sur {server.name}",
        description=f"Voici quelques infos sur ce serveur.",
        color=discord.Color.blue()
    )
    embed.add_field(name="Membres", value=server.member_count, inline=True)
    embed.add_field(name="Créé le", value=server.created_at.strftime("%d/%m/%Y"), inline=True)
    owner_name = server.owner.mention if server.owner else "Inconnu"
    embed.add_field(name="Propriétaire", value=owner_name, inline=True)
    await ctx.send(embed=embed)

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