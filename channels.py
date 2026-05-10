import discord
from discord.ext import commands

class Channels(commands.Cog):
    """
    Cog for channel management commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        """
        Locks a channel (no one can write except moderators).
        Usage: !lock [#channel]
        """
        channel = channel or ctx.channel
        
        try:
            # Create a permission overwrite for @everyone
            overwrite = discord.PermissionOverwrite(send_messages=False)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            
            embed = discord.Embed(
                title="Channel Locked",
                description=f"{channel.mention} has been locked.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to modify this channel.")
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        """
        Unlocks a channel (everyone can write again).
        Usage: !unlock [#channel]
        """
        channel = channel or ctx.channel
        
        try:
            # Remove permission overwrite for @everyone
            await channel.set_permissions(ctx.guild.default_role, overwrite=None)
            
            embed = discord.Embed(
                title="Channel Unlocked",
                description=f"{channel.mention} has been unlocked.",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to modify this channel.")
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockall(self, ctx):
        """
        Locks all channels on the server.
        Usage: !lockall
        """
        try:
            overwrite = discord.PermissionOverwrite(send_messages=False)
            count = 0
            
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                count += 1
            
            embed = discord.Embed(
                title="All Channels Locked",
                description=f"{count} channels have been locked.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to modify channels.")
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlockall(self, ctx):
        """
        Unlocks all channels on the server.
        Usage: !unlockall
        """
        try:
            count = 0
            
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, overwrite=None)
                count += 1
            
            embed = discord.Embed(
                title="All Channels Unlocked",
                description=f"{count} channels have been unlocked.",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to modify channels.")
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

async def setup(bot):
    await bot.add_cog(Channels(bot))
