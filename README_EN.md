# Discord Bot Tutorial - English

[Back to Main](README.md) | [Version Francaise](README_FR.md)

## Overview

This is a complete Discord bot starter template built with Python and discord.py. It includes modular command architecture, moderation tools, channel management, and security best practices.

## Prerequisites

- Python 3.8 or later
- A Discord account
- A Discord server for testing
- VS Code or any text editor
- Basic Python knowledge

## Step 1: Discord Developer Setup

### Create Application
1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Enter your bot name and click "Create"
4. Copy the Application ID

### Create Bot User
1. Go to the "Bot" tab
2. Click "Add Bot"
3. Copy your token (keep it secret!)

### Invite Bot to Server
1. Go to "OAuth2" > "URL Generator"
2. Select "bot" in scopes
3. Select necessary permissions (Send Messages, Read Messages, Manage Channels, etc.)
4. Open the generated URL to invite the bot

## Step 2: Project Setup

### Create Project Structure
```
my_discord_bot/
    main.py
    general.py
    moderation.py
    channels.py
    help_cog.py
    requirements.txt
    .env
    .gitignore
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

File: requirements.txt
```
discord.py==2.3.2
python-dotenv==1.0.0
```

### Configure Token
Create a `.env` file:
```
DISCORD_TOKEN=your_token_here
```

## Step 3: Understanding the Bot Structure

### Main Entry Point (main.py)
The main.py file:
- Loads environment variables from .env
- Creates the bot instance
- Loads all cogs when the bot is ready
- Handles global errors

### Cogs System
Each cog is a separate module containing related commands:
- general.py: Basic commands (ping, hello, info)
- moderation.py: Moderation commands (kick, ban, mute, etc.)
- channels.py: Channel management (lock, unlock)
- help_cog.py: Custom help system

## Available Commands

### General Commands
- `!ping` - Bot responds with "Pong!"
- `!hello` - Bot greets the user
- `!info` - Displays server information (members, creation date, owner)

### Moderation Commands
- `!kick @member [reason]` - Kicks a member from the server
- `!ban @member [reason]` - Permanently bans a member
- `!unban name#tag` - Unbans a previously banned member
- `!mute @member [reason]` - Mutes a member (requires "Muted" role)
- `!unmute @member [reason]` - Unmutes a member

### Channel Management Commands
- `!lock [#channel]` - Locks a channel (no one can write)
- `!unlock [#channel]` - Unlocks a channel
- `!lockall` - Locks all channels on the server
- `!unlockall` - Unlocks all channels on the server

### Help Commands
- `!help` - Show all available commands
- `!help <command>` - Show help for specific command
- `!help <category>` - Show help for command category

## How to Run

1. Activate virtual environment (if using one)
2. Run: `python main.py`
3. Check console for "Bot connected as [BotName]"
4. Test commands on your Discord server

## Understanding Each Command

For detailed explanations of how each command works internally, see:
[TUTORIAL_DISCORD_BOT_EN_DETAILED.pdf](TUTORIAL_DISCORD_BOT_EN_DETAILED.pdf)

This PDF includes:
- Step-by-step setup instructions
- How each command is implemented
- Understanding Cogs and permissions
- Security best practices
- Ideas for extending the bot

## Security Best Practices

1. Never hardcode your token
2. Always use .env files for secrets
3. Add .env to .gitignore
4. Use environment variables for all sensitive data
5. Limit bot permissions to only what's needed
6. Regenerate token if compromised
7. Test on private server before production

## Customization

Each cog can be easily modified or extended:

### Adding a New Command
```python
@commands.command()
async def mycommand(self, ctx):
    """My custom command description"""
    await ctx.send("Hello!")
```

### Adding Permissions Check
```python
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member):
    # Your command code
```

## Troubleshooting

### Bot not responding
- Check if token is correct in .env
- Verify bot is invited to server
- Check bot permissions on server

### Commands not working
- Use `!help` to see available commands
- Ensure you have required permissions
- Check bot has necessary Discord permissions

### Permission errors
- Make sure bot has higher role than target member
- Check channel permissions
- Verify bot token has correct scopes

## Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Documentation](https://discord.com/developers/docs)
- [Python Official Documentation](https://docs.python.org/3/)

## Future Enhancements

Ideas to extend your bot:
- Welcome messages for new members
- Logging system for moderation actions
- Fun commands (joke, quote, etc.)
- Database integration
- Automated moderation (spam detection)
- Role assignment system
- Message reactions
- Scheduled tasks

## License

This project is open source and available for educational purposes.

