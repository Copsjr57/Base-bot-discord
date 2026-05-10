import discord
from discord.ext import commands

class CustomHelp(commands.HelpCommand):
    """
    Commande d'aide personnalisée qui se met à jour automatiquement.
    """

    async def send_bot_help(self, mapping):
        """
        Envoie l'aide générale du bot.
        """
        embed = discord.Embed(
            title="Aide du Bot",
            description="Voici la liste des commandes disponibles. Utilisez `!help <commande>` pour plus de détails.",
            color=discord.Color.blue()
        )
        for cog, commands_list in mapping.items():
            if cog and commands_list:  # Ignore les commandes sans cog
                cog_name = cog.qualified_name if cog else "Autres"
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
        Envoie l'aide pour un cog spécifique.
        """
        embed = discord.Embed(
            title=f"Aide - {cog.qualified_name}",
            description=cog.description or "Pas de description.",
            color=discord.Color.blue()
        )
        commands_list = [cmd for cmd in cog.get_commands() if not cmd.hidden]
        if commands_list:
            for cmd in commands_list:
                embed.add_field(
                    name=f"!{cmd.name}",
                    value=cmd.help or "Pas de description.",
                    inline=False
                )
        else:
            embed.add_field(name="Aucune commande", value="Ce cog n'a pas de commandes visibles.")
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        """
        Envoie l'aide pour une commande spécifique.
        """
        embed = discord.Embed(
            title=f"Aide - !{command.name}",
            description=command.help or "Pas de description.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Utilisation", value=f"!{command.name} {command.signature}", inline=False)
        if command.aliases:
            embed.add_field(name="Alias", value="`" + "`, `".join(command.aliases) + "`", inline=False)
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        """
        Envoie l'aide pour un groupe de commandes.
        """
        embed = discord.Embed(
            title=f"Aide - !{group.name}",
            description=group.help or "Pas de description.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Utilisation", value=f"!{group.name} {group.signature}", inline=False)
        subcommands = [cmd for cmd in group.commands if not cmd.hidden]
        if subcommands:
            embed.add_field(
                name="Sous-commandes",
                value="`" + "`, `".join([cmd.name for cmd in subcommands]) + "`",
                inline=False
            )
        await self.get_destination().send(embed=embed)

    async def send_error_message(self, error):
        """
        Envoie un message d'erreur pour l'aide.
        """
        embed = discord.Embed(
            title="Erreur",
            description=error,
            color=discord.Color.red()
        )
        await self.get_destination().send(embed=embed)

class HelpCog(commands.Cog):
    """
    Cog pour la commande d'aide personnalisée.
    """

    def __init__(self, bot):
        self.bot = bot
        # Remplacer la commande help par défaut
        bot.help_command = CustomHelp()

async def setup(bot):
    await bot.add_cog(HelpCog(bot))