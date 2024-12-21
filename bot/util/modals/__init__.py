from nextcord import Interaction
import pytz
from datetime import datetime, timedelta
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

ROBCOUNT_TABLE = {
    "Peluquería": "∞",
    "Tienda de tatuajes": "∞",
    "Badulaque": "20",
    "Licoreria": "20",
    "Robo a casas": "15",
    "Coche de importación": "15",
    "Pawnshop": "2"
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
        spain_tz = pytz.timezone("Europe/Madrid")
        monday = datetime.now(spain_tz) - timedelta(days=datetime.now(spain_tz).weekday())  # Lunes actual
        sunday = monday + timedelta(days=6)
        channel_id = CHANNEL_TABLES.get(self.type)
        rob_limit = ROBCOUNT_TABLE.get(self.type)
        channel = await interaction.guild.fetch_channel(channel_id)
        message_count = await count_messages_in_date_range(channel, monday, sunday)
        embed = nextcord.Embed(
            title= "Robo realizado",
            description=(
                f"**Tipo de establecimiento:** {self.type}\n"
                f"**Sobre qué hora:** {self.time.value}\n"
                f"**Qué has conseguido?:** {self.obtained.value}\n"
                f"**Armamento utilizado:** {self.used.value}\n"
                f"**Te ha pillado la policía?:** {self.captured}\n"
                f"**Robos realizados esta semana:** {message_count + 1}/{rob_limit}"
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
        if channel is None:
            await interaction.response.send_message(embed=embed)
        else:
            await channel.send(embed=embed)


async def count_messages_in_date_range(channel, start_date, end_date):
    """
    Cuenta los mensajes en un canal dentro de un rango de fechas.
    
    :param channel: El canal de Discord donde buscar mensajes.
    :param start_date: Fecha de inicio (datetime con tzinfo).
    :param end_date: Fecha de fin (datetime con tzinfo).
    :return: El número de mensajes en el rango de fechas.
    """
    message_count = 0

    # Iterar sobre los mensajes en el canal
    async for message in channel.history(limit=None, after=start_date, before=end_date):
        message_count += 1

    return message_count