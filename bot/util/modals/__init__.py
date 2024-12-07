from nextcord import Interaction
import nextcord
from util.constants import TimeConverter, CASAS_CHANNEL, COCHES_CHANNEL, BADULAQUE_CHANNEL, PELUQUERIA_CHANNEL, TATUAJE_CHANNEL, PAWNSHOP_CHANNEL

CHANNEL_TABLES = {
   "Peluquería": PELUQUERIA_CHANNEL,
    "Tienda de tatuajes": TATUAJE_CHANNEL,
    "Badulaque": BADULAQUE_CHANNEL,
    "Licoreria": BADULAQUE_CHANNEL,
    "Robo a casas": CASAS_CHANNEL,
    "Coche de importación": COCHES_CHANNEL,
    "Pawnshop": PAWNSHOP_CHANNEL
}
class RobRegister(nextcord.ui.Modal):
    def __init__(self, type, time_zone, captured):
        super().__init__(timeout=None,title="Registrar robo")

        self.type = type
        self.timezone = time_zone
        self.captured = captured
        self.time = nextcord.ui.TextInput(
            label="Hora del robo",
            placeholder="Hora del robo(en tu zona horaria) hh:mm",
            required=True,
        )
        self.obtained = nextcord.ui.TextInput(
            label="¿Qué se obtuvo?",
            placeholder="¿Qué se obtuvo?",
            required=True
        )
        self.used = nextcord.ui.TextInput(
            label="Armamento utilizado",
            placeholder="Armamento utilizado",
            required=True
        )
        self.add_item(self.time)
        self.add_item(self.obtained)
        self.add_item(self.used)

    async def callback(self, interaction: Interaction):
        utc_time = TimeConverter.time_to_utc(self.time.value, self.timezone)
        spain_time = TimeConverter.utc_time_to_timezone("Europe/Madrid", utc_time)
        channel_id = CHANNEL_TABLES.get(self.type)
        embed = nextcord.Embed(
            title= "Robo realizado",
            description=(
                f"**Tipo de establecimiento:** {self.type}\n"
                f"**Sobre qué hora:** {self.time.value}\n"
                f"**Qué has conseguido?:** {self.obtained.value}\n"
                f"**Armamento utilizado:** {self.used.value}\n"
                f"**Te ha pillado la policía?:** {self.captured}"
            ),
            color=nextcord.Color.dark_gold()
        )
        embed.add_field(
            name="**Plantilla ilegales llena:**",
            value=(
                f"```markdown\n"
                f"Tipo de establecimiento: {self.type}\n"
                f"Sobre qué hora: {spain_time.strftime('%H:%M')}\n"
                f"Qué has conseguido?: {self.obtained.value}\n"
                f"Armamento utilizado: {self.used.value}\n"
                f"Te ha pillado la policía?: {self.captured}"
                "```"
            ),
            inline=False
        )
        embed.set_footer(
            text=f"Robo realizado por {interaction.user.name}",
        )
        channel = await interaction.guild.fetch_channel(channel_id)
        if channel is None:
            await interaction.response.send_message(embed=embed)
        else:
            await channel.send(embed=embed)
