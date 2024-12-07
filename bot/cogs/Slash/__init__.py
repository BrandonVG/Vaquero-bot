import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

from util.modals import RobRegister
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @nextcord.slash_command(name="robo-realizado", description="Abre un formulario para registrar un robo.", guild_ids=[1300528533529038931])
    async def robo_realizado(self, interaction: Interaction, establecimiento: str = SlashOption(
        name="establecimiento",
        description="Selecciona el tipo de establecimiento",
        choices=[
            "Peluquería",
            "Tienda de tatuajes",
            "Badulaque",
            "Licoreria",
            "Robo a casas",
            "Coche de importación",
            "Pawnshop",
        ],
        ),timezone: str = SlashOption(
            name="timezone",
            description="Selecciona tu zona horaria",
            choices=[
                "America/Puerto_Rico",
                "America/Mexico_City",
                "Europe/Madrid",
                "America/Argentina/Buenos_Aires",
            ],
        ),
        captured: str = SlashOption(
            name= "capturado",
            description="¿Te ha pillado la policía?",
            choices=[
                "Sí",
                "No"
            ],
        )
    ):
        modal = RobRegister(establecimiento, timezone, captured)
        await interaction.response.send_modal(modal)