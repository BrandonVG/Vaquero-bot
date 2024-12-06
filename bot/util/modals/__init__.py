import nextcord
class RobRegister(nextcord.ui.Modal):
  def __init__(self):
    super().__init__(timeout=None,title="Registrar robo")

    self.establecimiento = nextcord.ui.StringSelect(
        label="Tipo de establecimiento",
        placeholder="Seleccionar el tipo de establecimiento",
        options = [
            nextcord.SelectOption(label="Peluquería"),
            nextcord.SelectOption(label="Tienda de tatuajes"),
            nextcord.SelectOption(label="Badulaque"),
            nextcord.SelectOption(label="Licoreria"),
            nextcord.SelectOption(label="Robo a casas"),
            nextcord.SelectOption(label="Coche de importación"),
            nextcord.SelectOption(label="Pawnshop"),
        ],
        required=True
    )
    self.time = nextrecord.ui.TextInput(
        label="Hora del robo",
        placeholder="Hora del robo",
        required=True,
        style=nextcord.TextInputStyle.TIMESTAMP
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
    self.captured = nextcord.ui.StringSelect(
        label="Te atrapo la policia?",
        placeholder="Te atrapo la policia?",
        options=[
            nextcord.SelectOption(label="Si"),
            nextcord.SelectOption(label="No")
        ],
        required=True
    )
    self.add_item(self.establecimiento)
    self.add_item(self.time)
    self.add_item(self.obtained)
    self.add_item(self.captured)

    async def callback(self, interaction: Interaction):
       embed = nextcord.Embed(
          title= "Robo realizado",
          description=(
             "**Tipo de establecimiento:** {self.establecimiento.values[0]}\n"
             "**Sobre qué hora:** {self.time.value}\n"
             "**Qué has conseguido?:** {self.obtained.value}\n"
             "**Armamento utilizado:** {self.used.value}\n"
             "**Te ha pillado la policía?:** {self.captured.values[0]}"
          ),
          color=nextcord.Color.Brown()
       )
       embed.add_field(
          value=(
             "Tipo de establecimiento: {self.establecimiento.values[0]}\n"
             "Sobre qué hora: {self.time.value}\n"
             "Qué has conseguido?: {self.obtained.value}\n"
             "Armamento utilizado: {self.used.value}\n"
             "Te ha pillado la policía?: {self.captured.values[0]}"
          ),
          inline=False
       )
       embed.set_footer(
          text=f"Robo realizado por {interaction.user.name}",
       )

       await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="robo-realizado", description="Abre un formulario para registrar un robo.")
    async def robo_realizado(interaction: Interaction):
        await interaction.response.send_modal(RobRegister())
