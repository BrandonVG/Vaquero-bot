from util.constants import BADULAQUE_CHANNEL, TATUAJE_CHANNEL, PELUQUERIA_CHANNEL, CASAS_CHANNEL, COCHES_CHANNEL, PAWNSHOP_CHANNEL, AMMU_CHANNEL, MISSION_CHANNEL
from datetime import datetime, timedelta
from pytz import timezone


CHANNELS = [
    BADULAQUE_CHANNEL,
    TATUAJE_CHANNEL,
    PELUQUERIA_CHANNEL,
    CASAS_CHANNEL,
    COCHES_CHANNEL,
    PAWNSHOP_CHANNEL,
    AMMU_CHANNEL,
    MISSION_CHANNEL
]

class TimeScheduler:
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_week_range():
        """
        Returns the week range of the current week(monday to sunday)
        """
        spain_tz = timezone('Europe/Madrid')
        today = datetime.now(spain_tz)
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6)
        return monday.strftime("%d/%m"), sunday.strftime("%d/%m")
    
    
    async def send_weekly_message(self):
        """
        Send a weekly message to the specified channels
        """
        start_date, end_date = self.get_week_range()
        message = f"**SEMANA {start_date} - {end_date}**"
        for channel in CHANNELS:
            channel = await self.bot.fetch_channel(channel)
            if channel:
                await channel.send(message)

    

