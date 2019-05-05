import os, sys

bot_name = "Eve Bot"

# Log channels for servers in the form (guild_id : channel id), one per guild.
# Message edits and deletes for each guild will be posted here.
log_channels = {
    384144475229782037: 574416190802231316, # Test server
    354565059675947009: 499292048097148928  # TMHC
}

# Whether or not to run in debug mode is determined by the presence of an environment variable
DEBUG = os.environ.get('BOT_DEBUG', False) is not False

# If running in debug mode, the bot will be restricted to channel ids in the following array.
debug_channel_ids = [384144475670446081,574416190802231316]

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
RESPONSE_DIR = os.path.join(ROOT_DIR, "responses")
COMMAND_DIR = os.path.join(ROOT_DIR, "commands")
