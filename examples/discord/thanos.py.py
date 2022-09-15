#!/usr/bin/python

# discord message deleter
# tested under WSL (win10 bash).
#
#  prerequisites:  Find the guild id and your auth token.
#   go to discord.gg and navigate to your server.
#   Your guild ID is in the URL:  https://discordapp.com/channels/GUILD_ID/CHANNEL_ID - take the guild_id
#   Hit ctrl-shift-I to open network inspector (network tab).  Reload the page.
#   Click on XHR, and on the messages?limit-50 item.  Scroll down to Request Headers, the one called "authorization".  The long random string there is your auth_token.
#  your username is the first part of your pete#1234 id, the discriminator is the second part.  So, this person's username would be pete and his discriminator is 1234.
#
# 1. put this script in an empty directory, call it ddelete.py.
# 2. Create a file in the same directory called secrets.json .  It should have this format:
# {
#   "username": "yourname"
#   "discriminator": "your_number"
#   "guild_id": "the ID of your server, copied from discord.gg URL"
#   "auth_token": "The auth token copied from google chrome network inspector"
# }
# 3. run "python ddelete.py"

import json, requests, sys, os, time, pprint
pp = pprint.PrettyPrinter(indent=4)

with open('secrets.json') as secrets:
    data = json.load(secrets)
    username = data['username']
    discriminator = data['discriminator']
    auth_token =  data['auth_token']
    guild_id = data['guild_id']

def get_messages_after_mark_for_channel(auth_token, channel_id, lastmark):
    last = lastmark
    all_messages = []
    done = False
    count = 0
    deleted = 0

    while not done:
        messages = json.loads(
            requests.get("https://discordapp.com/api/v6/channels/" +
                         channel_id + "/messages",
                         headers = { "authorization": auth_token },
                         params = { "limit": 100,
                                    "after": last })
            .content)

        count += len(messages)
        if len(messages):
            print ("got " + str(count) + " messages and deleted " + str(deleted))
            for message in messages:
                pp.pprint(message)
                try:
                  if (message["author"]["username"] == username and
                      message["author"]["discriminator"] == discriminator):
                      delete_message(auth_token, channel_id, message)
                      deleted += 1
                except Exception:
                    print ("couldn't for some reason\n")
                    pp.pprint(message)

            all_messages += messages
            newest = sorted(messages,
                            key=lambda x: x['timestamp'],
                            reverse=True)[0]

            if len(messages) < 100:
                done = True
            else:
                last = newest["id"]
        else:
            done = True

    return all_messages

def get_messages_for_channel(auth_token, channel_id):
    last = False
    all_messages = []
    done = False
    count = 0
    deleted = 0

    while not done:
        if last:
            messages = json.loads(
                requests.get("https://discordapp.com/api/v6/channels/" +
                             channel_id + "/messages",
                             headers = { "authorization": auth_token },
                             params = { "limit": 100,
                                        "before": last })
                .content)
        else:
            messages = json.loads(
                requests.get("https://discordapp.com/api/v6/channels/" +
                             channel_id + "/messages",
                             headers = { "authorization": auth_token },
                             params = { "limit": 100 })
                .content)


        count += len(messages)
        if type(messages) == type(dict()):
            done = True
            print ("Error, didn't get a list of messages!")
            break

        for message in messages:
            if (message["author"]["username"] == username and
                message["author"]["discriminator"] == discriminator):
                delete_message(auth_token, channel_id, message)
                deleted += 1

        if len(messages):
            print ("got " + str(count) + " messages and deleted " + str(deleted))
            all_messages += messages
            oldest = sorted(messages,
                            key=lambda x: x['timestamp'],
                            reverse=True)[-1]

            if len(messages) < 100:
                done = True
            else:
                last = oldest["id"]
        else:
            done = True

    return all_messages

def delete_message(auth, channel_id, message):
    done = False
    while not done:
        r = requests.delete("https://discordapp.com/api/v6/channels/"
                            + channel_id + "/messages/" + message["id"],
                            headers={"authorization": auth})
        if r.status_code == 204:
            done = True
        else:
            if r.status_code == 429:
                wait_time = (r.json()['retry_after'] / 1000) + 0.1
                print ("Rate limited, retrying in " + str(wait_time) + " seconds...")
                time.sleep(wait_time)
            else:
                print (r.text)
                time.sleep(1)
                print ("Retrying deletion...")
channels = json.loads(
    requests.get("https://discordapp.com/api/v6/guilds/" +
                 guild_id + "/channels",
                 headers = { "authorization": auth_token })
    .content)

for channel in channels:
    channel_id = channel["id"]
    last = False
    print ("Working channel " + channel["name"])
    if os.path.isfile('discorddelete_mark_' + str(channel_id)):
        with open('discorddelete_mark_' + str(channel_id)) as lastmark:
            last = lastmark.read()
            print ("Loaded mark " + last)
            messages = get_messages_after_mark_for_channel(auth_token,
                                                           channel_id,
                                                           last)
    else:
        messages = get_messages_for_channel(auth_token, channel_id)
    if len(messages) > 0:
        oldest = sorted(messages,
                        key=lambda x: x['timestamp'],
                        reverse=True)
        for message in oldest:
            if (message["author"]["username"] != username or
                message["author"]["discriminator"] != discriminator):
                last = message["id"]
                break
        print ("Saving mark at " + last)
        with open('discorddelete_mark_' + str(channel_id), 'w') as lastmark:
            lastmark.write(last)