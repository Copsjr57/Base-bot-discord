import discord
from discord.ext import commands

class General(commands.Cog):
    """
    Cog pour les commandes générales.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Commande simple qui répond "Pong!" pour tester si le bot fonctionne.
        """
        await ctx.send('Pong!')

    @commands.command()
    async def hello(self, ctx):
        """
        Commande qui salue l'utilisateur qui l'a appelée.
        """
        await ctx.send(f'Salut {ctx.author.mention} ! Comment ça va ?')

    @commands.command()
    async def info(self, ctx):
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

async def setup(bot):
    await bot.add_cog(General(bot))