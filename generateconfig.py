"""
      Configuration file generator for SexualRhinoceros/MusicBot (review branch)
      To use, place this script inside the main directory of the bot and run it
      Designed to be a "fool proof" way of configuring the bot
"""

import configparser
import os
import sys
import traceback
from urllib import request
from urllib import error

def set_boolean(section, option, i):
    if i == "yes":
        config.set(section, option, 'yes')
    else:
        config.set(section, option, 'no')

print('\n\n==== options.ini Generator for MusicBot ====')

i = input("\nThis will overwrite existing options if they exist. Continue? [y/n] ")

if i == "y":
    print('\nRetrieving file from Github')
    try:
        if not os.path.isdir("config"):
            os.makedirs("config")
        request.urlretrieve('https://raw.githubusercontent.com/SexualRhinoceros/MusicBot/review/config/example_options.ini', 'config/options.ini')
    except error.ContentTooShortError:
        print('Unable to retrieve file. Download may have been interrupted. Check your firewall settings.')
        sys.exit()
    except Exception:
        print('Unable to retrieve file. Printing stack trace.')
        traceback.print_exc()
        sys.exit()

    print('Parsing default configuration.')
    config = configparser.ConfigParser(interpolation=None, allow_no_value=True)
    config.read('config/options.ini', encoding='utf-8')

    if input("\nWhich type of account are you going to use? [bot/user]: ") == "user":
        config.set('Credentials', 'Email', input("\n> Enter bot's email address: "))
        config.set('Credentials', 'Password', input("> Enter bot's password: "))
    else:
        print("\nYou need to create a bot account at https://discordapp.com/developers/applications/me")
        config.remove_option('Credentials', 'Email')
        config.remove_option('Credentials', 'Password')
        config.set('Credentials', 'Token', input("> Enter bot token: "))

    config.set('Permissions', 'OwnerID', input("> Enter owner ID (use \@username in Discord): "))

    print("\nThis is/are character(s) that is required to be before commands in chat")
    config.set('Chat', 'CommandPrefix', input("> Enter command prefix: "))

    print("\nThe bot can bind to text channels. This means it will only accept commands from those channels.\nTo get channel IDs, use \#channel-name in Discord\nUse space to separate IDs. Leave blank for none.")
    i = input("> Bound channel IDs: ")
    if input:
        config.set('Chat', 'BindToChannels', i)

    print("\nThe bot can autojoin voice channels (one per server).\nTo get voice channel IDs, use the 'listids' command of the bot\nUse space to separate IDs. Leave blank for none.")
    i = input("> Autojoin channel IDs: ")
    if input:
        config.set('Chat', 'AutojoinChannels', i)

    i = input("\n> Volume (leave blank for default): ")
    if i: config.set('MusicBot', 'DefaultVolume', i)
    i = input("> Use whitelist? (yes/no): ")
    set_boolean('MusicBot', 'WhitelistCheck', i)
    i = input("> Skips required to pass vote (leave blank for default): ")
    if i: config.set('MusicBot', 'SkipsRequired', i)
    i = input("> Skip ratio required to pass vote (leave blank for default): ")
    if i: config.set('MusicBot', 'SkipRatio', i)
    i = input("> Save videos locally? (yes/no): ")
    set_boolean('MusicBot', 'SaveVideos', i)
    i = input("> Mention users when their song is played? (yes/no): ")
    set_boolean('MusicBot', 'NowPlayingMentions', i)
    i = input("> Autosummon bot to owner's channel on start? (yes/no): ")
    set_boolean('MusicBot', 'AutoSummon', i)
    i = input("> Autoplay songs from 'config/autoplaylist.txt'? (yes/no): ")
    set_boolean('MusicBot', 'UseAutoPlaylist', i)
    i = input("> Autopause bot when no users are present? (yes/no): ")
    set_boolean('MusicBot', 'AutoPause', i)
    i = input("> Delete bot messages automatically after a while? (yes/no): ")
    set_boolean('MusicBot', 'DeleteMessages', i)
    i = input("> Delete invoking (e.g commands) messages? (yes/no): ")
    set_boolean('MusicBot', 'DeleteInvoking', i)

    # Save configuration to file
    print('\nSaving new configuration.')
    with open('config/options.ini', 'w') as file:
        try:
            config.write(file)
            print('Saved. You can now run the bot.')
        except Exception:
            print('Problem saving. Printing exception.\n')
            traceback.print_exc()
else:
    sys.exit()