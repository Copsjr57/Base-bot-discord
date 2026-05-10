import discord
from discord.ext import commands

class CustomHelp(commands.HelpCommand):
    """
    Custom help command that automatically updates.
    """

    async def send_bot_help(self, mapping):
        """
        Send general bot help.
        """
        embed = discord.Embed(
            title="Bot Help",
            description="Here is a list of available commands. Use `!help <command>` for more details.",
            color=discord.Color.blue()
        )
        for cog, commands_list in mapping.items():
            if cog and commands_list:  # Ignore commands without cog
                cog_name = cog.qualified_name if cog else "Other"
                command_names = [cmd.name for cmd in commands_list if not cmd.hidden]
                if command_names:
                    embed.add_field(
                        name=cog_name,
                        value="`" + "`, `".join(command_names) + "`",
                        inline=False
                    )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        """
        Send help for a specific cog.
        """
        embed = discord.Embed(
            title=f"Help - {cog.qualified_name}",
            description=cog.description or "No description.",
            color=discord.Color.blue()
        )
        commands_list = [cmd for cmd in cog.get_commands() if not cmd.hidden]
        if commands_list:
            for cmd in commands_list:
                embed.add_field(
                    name=f"!{cmd.name}",
                    value=cmd.help or "No description.",
                    inline=False
                )
        else:
            embed.add_field(name="No commands", value="This cog has no visible commands.")
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        """
        Send help for a specific command.
        """
        embed = discord.Embed(
            title=f"Help - !{command.name}",
            description=command.help or "No description.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Usage", value=f"!{command.name} {command.signature}", inline=False)
        if command.aliases:
            embed.add_field(name="Aliases", value="`" + "`, `".join(command.aliases) + "`", inline=False)
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        """
        Send help for a group of commands.
        """
        embed = discord.Embed(
            title=f"Help - !{group.name}",
            description=group.help or "No description.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Usage", value=f"!{group.name} {group.signature}", inline=False)
        subcommands = [cmd for cmd in group.commands if not cmd.hidden]
        if subcommands:
            embed.add_field(
                name="Subcommands",
                value="`" + "`, `".join([cmd.name for cmd in subcommands]) + "`",
                inline=False
            )
        await self.get_destination().send(embed=embed)

    async def send_error_message(self, error):
        """
        Send an error message for help.
        """
        embed = discord.Embed(
            title="Error",
            description=error,
            color=discord.Color.red()
        )
        await self.get_destination().send(embed=embed)

class HelpCog(commands.Cog):
    """
    Cog for the custom help command.
    """

    def __init__(self, bot):
        self.bot = bot
        # Replace default help command
        bot.help_command = CustomHelp()

async def setup(bot):
    await bot.add_cog(HelpCog(bot))