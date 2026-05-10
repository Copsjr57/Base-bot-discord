import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """
    Cog pour les commandes de modération.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Expulse un membre du serveur.
        Utilisation : !kick @membre [raison]
        """
        if member == ctx.author:
            await ctx.send("Tu ne peux pas te kicker toi-même !")
            return
        if member.top_role >= ctx.author.top_role:
            await ctx.send("Tu ne peux pas kicker quelqu'un avec un rôle supérieur ou égal au tien.")
            return
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="Membre expulsé",
                description=f"{member.mention} a été expulsé.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Raison", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("Je n'ai pas la permission d'expulser ce membre.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Banni un membre du serveur.
        Utilisation : !ban @membre [raison]
        """
        if member == ctx.author:
            await ctx.send("Tu ne peux pas te bannir toi-même !")
            return
        if member.top_role >= ctx.author.top_role:
            await ctx.send("Tu ne peux pas bannir quelqu'un avec un rôle supérieur ou égal au tien.")
            return
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Membre banni",
                description=f"{member.mention} a été banni.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Raison", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("Je n'ai pas la permission de bannir ce membre.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name):
        """
        Débanni un membre du serveur.
        Utilisation : !unban nom#tag
        """
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member_name.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Membre débanni",
                    description=f"{user.mention} a été débanni.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
                return
        await ctx.send("Membre non trouvé dans la liste des bannis.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """
        Rend un membre muet (nécessite un rôle 'Muted').
        Utilisation : !mute @membre [raison]
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("Le rôle 'Muted' n'existe pas. Crée-le d'abord.")
            return
        if muted_role in member.roles:
            await ctx.send("Ce membre est déjà muet.")
            return
        try:
            await member.add_roles(muted_role, reason=reason)
            embed = discord.Embed(
                title="Membre muet",
                description=f"{member.mention} a été rendu muet.",
                color=discord.Color.orange()
            )
            if reason:
                embed.add_field(name="Raison", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("Je n'ai pas la permission de gérer les rôles.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """
        Rend un membre non-muet.
        Utilisation : !unmute @membre [raison]
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("Le rôle 'Muted' n'existe pas.")
            return
        if muted_role not in member.roles:
            await ctx.send("Ce membre n'est pas muet.")
            return
        try:
            await member.remove_roles(muted_role, reason=reason)
            embed = discord.Embed(
                title="Membre non-muet",
                description=f"{member.mention} n'est plus muet.",
                color=discord.Color.green()
            )
            if reason:
                embed.add_field(name="Raison", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("Je n'ai pas la permission de gérer les rôles.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))