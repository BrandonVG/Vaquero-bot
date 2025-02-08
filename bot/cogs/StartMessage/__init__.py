import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button

class StartMessage(ommands.Cog, name="Start message setup", description="Enviar mensaje al iniciar el bot"):
  def __init__(self, bot):
    self.bot = bot

  async def send_get_role_message():
    channel = bot.get_channel("1333610185314533376")
    button_get = nextcord.Button(style=nextcord.ButtonStyle.success, label="Dame el rol :D", custom_id="get_role")
    button_remove = nextcord.Button(style=nextcord.ButtonStyle.danger, label="Quítame el rol :(", custom_id="remove_role")
    view = View()
    view.add_item(button_get)
    view.add_item(button_remove)
    embed = nextcord.Embed(title="Rol de notificaciones laboratorio", description="Obten el rol para recibir notificaciones del laboratorio")
    view.add_item(embed)
    await channel.send(view=view)

  