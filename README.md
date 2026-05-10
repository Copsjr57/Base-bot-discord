# bot_discord_tuto

[Version Francaise](README_FR.md) | [English Version](README_EN.md)

## Overview / Apercu

This is a complete Discord bot starter template in Python with modular commands and security best practices. Perfect for learning how to build a Discord bot!

Ceci est un template complet de bot Discord en Python avec des commandes modulaires et les meilleures pratiques de securite. Parfait pour apprendre a creer un bot Discord!

## Quick Start / Demarrage Rapide

### English
1. Create a `.env` file with your Discord token
2. Install dependencies: `pip install -r requirements.txt`
3. Run the bot: `python main.py`
4. Use `!help` to see all commands
5. See [README_EN.md](README_EN.md) for detailed setup

### Francais
1. Creez un fichier `.env` avec votre token Discord
2. Installez les dependances: `pip install -r requirements.txt`
3. Lancez le bot: `python main.py`
4. Utilisez `!help` pour voir toutes les commandes
5. Consultez [README_FR.md](README_FR.md) pour l'installation detaillee

## Documentation / Tutoriels

- [TUTORIAL_DISCORD_BOT_EN_DETAILED.pdf](TUTORIAL_DISCORD_BOT_EN_DETAILED.pdf) - Complete step-by-step tutorial explaining each command
- [TUTORIEL_BOT_DISCORD_FR_DETAILLE.pdf](TUTORIEL_BOT_DISCORD_FR_DETAILLE.pdf) - Tutoriel complet etape par etape expliquant chaque commande

## Features / Fonctionnalites

- General commands (ping, hello, info)
- Moderation commands (kick, ban, unban, mute, unmute)
- Channel management (lock, unlock, lockall, unlockall)
- Auto-updating help system
- Modular cog-based architecture
- Full security implementation

## Available Commands / Commandes Disponibles

### General / Generales
- `!ping` - Test bot responsiveness
- `!hello` - Greet the user
- `!info` - Server information

### Moderation
- `!kick @member [reason]` - Kick a member
- `!ban @member [reason]` - Ban a member
- `!unban name#tag` - Unban a member
- `!mute @member [reason]` - Mute a member
- `!unmute @member [reason]` - Unmute a member

### Channel Management / Gestion de Salons
- `!lock [#channel]` - Lock a channel
- `!unlock [#channel]` - Unlock a channel
- `!lockall` - Lock all channels
- `!unlockall` - Unlock all channels

## Project Structure / Structure du Projet

```
bot_discord_tuto/
    main.py                    - Bot entry point
    general.py                 - General commands cog
    moderation.py              - Moderation commands cog
    channels.py                - Channel management cog
    help_cog.py                - Custom help command
    requirements.txt           - Python dependencies
    .env.example               - Configuration example
    README.md                  - This file
    README_EN.md               - English readme
    README_FR.md               - French readme
```

## Security / Securite

- Never share your Discord token
- Always use `.env` file for secrets
- Add `.env` to `.gitignore`
- Test on private server before deployment

## Resources / Ressources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/)
- [Python Documentation](https://docs.python.org/3/)

