import discord
import os

# Set the ID of the server you want to dump messages from
server_id = 100000000000000000
# Set the message limit to be dumped, or None to dump all available
limit = None
# Set the bot token
BOT_TOKEN = "ODUaaaaaaaaaaaaaaaaaaaaa.aaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaap-aaaaaa"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

    # Get the server object by ID
    server = client.get_guild(server_id)
    print(server.name)
    for ch in server.text_channels:
        print("  "+ch.name)

    # Iterate over each channel in the server
    for channel in server.text_channels:
        # Create the directory for the channel if it does not exist
        # Examples: server_Name/Channel_Name
        #           server_Name/Category/Channel_Name
        if channel.category:
            directory = channel.category.name + "/" + channel.name
        else:
            directory = channel.name
        directory = server.name + "/" + directory
        os.makedirs(directory, exist_ok=True)

        # Actual dumping - try to get access to channel and dump EVERYTHING from it
        try:
            #Open log file for writing messages, embed jsons, and attachment links
            with open(directory + '/log.txt', 'w', encoding='utf-8') as f:
                print("Dumping "+channel.name+"...")
                # Iterate over each message in the channel and write it to the file
                async for message in channel.history(limit=limit):
                    attachments = ""
                    for attachment in message.attachments:
                        filename = attachment.filename.replace(" ", "_")
                        filename = message.created_at.strftime("%d.%m.%Y_%H-%M-%S") + '_' + message.author.name.replace(" ", "-") + '_' + filename
                        try:
                            await attachment.save(directory + "/" + filename)
                            attachments += f" [Attachment saved to {directory}/{filename}]"
                        except Exception as e:
                            print("  Failed to save attachment("+str(e)+")")
                            attachments += " [Failed to save attachment]"
                    if message.embeds:
                        embeds = "\n" + "\n".join(str(embed.to_dict()) for embed in message.embeds)
                    else:
                        embeds = ""
                    f.write(f"{message.created_at} {message.author.name}: {message.content} {attachments} {embeds}\n")
        except Exception as e:
            print("Failed to dump "+channel.name+"("+str(e)+")")
    print("Done!")
    exit()
client.run(BOT_TOKEN)
