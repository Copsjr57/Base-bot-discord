import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """
    Cog for moderation commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kicks a member from the server.
        Usage: !kick @member [reason]
        """
        if member == ctx.author:
            await ctx.send("You cannot kick yourself!")
            return
        if member.top_role >= ctx.author.top_role:
            await ctx.send("You cannot kick someone with a role equal to or higher than yours.")
            return
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="Member Kicked",
                description=f"{member.mention} has been kicked.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Reason", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to kick this member.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Bans a member from the server.
        Usage: !ban @member [reason]
        """
        if member == ctx.author:
            await ctx.send("You cannot ban yourself!")
            return
        if member.top_role >= ctx.author.top_role:
            await ctx.send("You cannot ban someone with a role equal to or higher than yours.")
            return
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Member Banned",
                description=f"{member.mention} has been banned.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Reason", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to ban this member.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name):
        """
        Unbans a member from the server.
        Usage: !unban name#tag
        """
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member_name.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Member Unbanned",
                    description=f"{user.mention} has been unbanned.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
                return
        await ctx.send("Member not found in ban list.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """
        Mutes a member (requires a 'Muted' role).
        Usage: !mute @member [reason]
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("The 'Muted' role does not exist. Create it first.")
            return
        if muted_role in member.roles:
            await ctx.send("This member is already muted.")
            return
        try:
            await member.add_roles(muted_role, reason=reason)
            embed = discord.Embed(
                title="Member Muted",
                description=f"{member.mention} has been muted.",
                color=discord.Color.orange()
            )
            if reason:
                embed.add_field(name="Reason", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to manage roles.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """
        Unmutes a member.
        Usage: !unmute @member [reason]
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("The 'Muted' role does not exist.")
            return
        if muted_role not in member.roles:
            await ctx.send("This member is not muted.")
            return
        try:
            await member.remove_roles(muted_role, reason=reason)
            embed = discord.Embed(
                title="Member Unmuted",
                description=f"{member.mention} is no longer muted.",
                color=discord.Color.green()
            )
            if reason:
                embed.add_field(name="Reason", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to manage roles.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))