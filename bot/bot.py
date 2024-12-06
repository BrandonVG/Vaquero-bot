import os, json, nextcord, logging, datetime, random, time
from pathlib import Path
from nextcord.ext import commands

from util.loaders import json
from util.constants import Client
from util.messages import DeleteMessage

#Config

cwd = Path(__file__).parents[0]
cwd = str(cwd)


activity = nextcord.Game(name=f"Vaquereando")

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(commands_prefix=Client.prefix, case_insensitive=True, activity=activity, intents=intents)

client.bot_version = Client.bot_version
client.guild_id = Client.guild_id
logging.basicConfig(level=logging.INFO)

# Events

@client.event
async def on_read():
    client.start_time = time.time()

    for cog in client.cogs:
        print(f"Loaded cog: {cog}")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.startswith(f"<@{client.user.id}>") and len(message.content) == lent(f"<@{client.user.id}>"):
        data = await client.config.find(message.guild.id)
        prefix = data.get("prefix", client.prefix)
        await message.channel.send(f"El prefix es{prefix}", delete_after=20)
    
    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    view = DeleteMessage(ctx)
    
    errorEmbed = nextcord.Embed(
        title="❌ Estoy mal hecho compadre", description="😞 No pude hacer el comando compadre, me hicieron mal", color=0xFF5733)
    errorEmbed.set_author(
        name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
        errorEmbed.add_field(
            name="Descripción del error", value=f"**Type:** {type(error)}\n\n ```Faltó un argumento del comando```")
    else:
        errorEmbed.add_field(
            name="Descripción del error", value=f"**Type:** {type(error)}\n\n ```py\n{error}\n```")
        
    errorEmbed.set_footer(
        text=f"Comando solicitado por {ctx.author.name}", icon_url=ctx.author.avatar.url)
    
    await ctx.send(embed=errorEmbed, view=view)
            
@client.event
async def on_application_command_error(interaction, error):
      
    errorEmbed = nextcord.Embed(
        title="❌ Error del bot", description="😞 No pude hacer el comando compadre, me hicieron mal", color=0xFF5733)
    errorEmbed.set_author(
        name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar)
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
        errorEmbed.add_field(
        name="Descripción del error", value=f"**Type:** {type(error)}\n\n```Faltó un argumento del comando```") 
    else:    
       errorEmbed.add_field(
        name="Descripción del error", value=f"**Type:** {type(error)}\n\n ```py\n{error}\n```")
       
    errorEmbed.set_footer(
        text=f"Command requested by {interaction.user.name}", icon_url=interaction.user.display_avatar)
   
    await interaction.response.send_message(embed=errorEmbed, ephemeral=True)


if __name__ == "__main__":

    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("__pycache"):
            client.load_extension(f"cogs.{file[:-3]}")
    
    client.run(Client.token)