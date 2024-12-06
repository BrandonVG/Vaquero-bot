import nextcord
from nextcord.ext import commands

class CogSetup(commands.Cog, name="Extension Setup", description="Cargar, descargar y recargar cogs."):
     def __init__(self, bot):
        self.bot = bot
     
     COG_EMOJI = "⚙️"

    
    # Load Command
     @commands.command(name="load", description="Cargar cogs.", usage="<cog_name o extension_name>")
     async def load(self, ctx, extensions):
        self.bot.load_extension(f"cogs.{extensions}") 
        await ctx.send("Cogs cargados")

    # Unload Comamnd
     @commands.command(name="unload", description="Descargar cogs.", usage="<cog_name o extension_name>")
     async def unload(self, ctx, extensions):
        self.bot.unload_extension(f"cogs.{extensions}")
        await ctx.send("Cogs descargados")

    # Reload Command
     @commands.command(name="reload", description="Recargar cogs.", usage="<cog_name o extension_name>")
     async def reload(self, ctx, extensions):
        self.bot.reload_extension(f"cogs.{extensions}")
        await ctx.send("Recargar Cogs")

    