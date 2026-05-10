import discord
from discord.ext import commands

class General(commands.Cog):
    """
    Cog for general commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Simple command that responds with Pong! to test if the bot is working.
        """
        await ctx.send('Pong!')

    @commands.command()
    async def hello(self, ctx):
        """
        Command that greets the user who called it.
        """
        await ctx.send(f'Hello {ctx.author.mention}! How are you doing?')

    @commands.command()
    async def info(self, ctx):
        """
        Command that provides information about the Discord server.
        """
        server = ctx.guild
        embed = discord.Embed(
            title=f"Information about {server.name}",
            description=f"Here is some info about this server.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Members", value=server.member_count, inline=True)
        embed.add_field(name="Created on", value=server.created_at.strftime("%d/%m/%Y"), inline=True)
        owner_name = server.owner.mention if server.owner else "Unknown"
        embed.add_field(name="Owner", value=owner_name, inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))