import discord
from discord.ext import commands

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Nuevos emojis personalizados
EMOJI_SOPORTE = "<:emoji_11:1550144504990801930>"
EMOJI_TIENDA = "<:emoji_20:1550146329915949077>"
EMOJI_REPORTE = "<:emoji_10:1550144465765793792>"
EMOJI_REGALO = "<:emoji_14:1550144666618302525>"
EMOJI_MANTENIMIENTO = "<:emoji_9:1550144328540618882>"
EMOJI_VIPERFINDER = "<:emoji_12:1550144549412802631>"

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # El panel no expira

    # Fila 1 de botones
    @discord.ui.button(label="Soporte", style=discord.ButtonStyle.secondary, emoji=EMOJI_SOPORTE, custom_id="ticket_soporte", row=0)
    async def soporte_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "soporte")

    @discord.ui.button(label="Tienda", style=discord.ButtonStyle.secondary, emoji=EMOJI_TIENDA, custom_id="ticket_tienda", row=0)
    async def tienda_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "tienda")

    @discord.ui.button(label="Reporte", style=discord.ButtonStyle.secondary, emoji=EMOJI_REPORTE, custom_id="ticket_reporte", row=0)
    async def reporte_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "reporte")

    # Fila 2 de botones
    @discord.ui.button(label="Mantenimiento", style=discord.ButtonStyle.secondary, emoji=EMOJI_MANTENIMIENTO, custom_id="ticket_mantenimiento", row=1)
    async def mantenimiento_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "mantenimiento")

    # Fila 3 de botones
    @discord.ui.button(label="Regalo", style=discord.ButtonStyle.secondary, emoji=EMOJI_REGALO, custom_id="ticket_regalo", row=2)
    async def regalo_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "regalo")

    @discord.ui.button(label="Viperfinder", style=discord.ButtonStyle.secondary, emoji=EMOJI_VIPERFINDER, custom_id="ticket_viperfinder", row=2)
    async def viperfinder_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.crear_ticket(interaction, "viperfinder")

    async def crear_ticket(self, interaction: discord.Interaction, tipo: str):
        await interaction.response.send_message(f"¡Has creado un ticket de **{tipo}** con éxito!", ephemeral=True)

@bot.event
async def on_ready():
    print(f'Bot conectado correctamente como {bot.user}')

@bot.command(name="panel")
@commands.has_permissions(administrator=True)
async def panel(ctx):
    # Crear el Embed con los nuevos emojis
    embed = discord.Embed(
        title="Lunar Market — Crear un Ticket",
        description=(
            f"{EMOJI_SOPORTE} **soporte** — Ayuda general con compras, problemas técnicos o preguntas sobre la tienda.\n"
            f"{EMOJI_TIENDA} **tienda** — Consultas relacionadas con productos, pagos, envíos o inventario.\n"
            f"{EMOJI_REPORTE} **reporte** — Reportes de usuarios, fraudes o comportamientos inapropiados.\n"
            f"{EMOJI_REGALO} **regalo** — Consultas sobre cajas/regalos.\n"
            f"{EMOJI_MANTENIMIENTO} **mantenimiento** — Avisos o dudas sobre mantenimientos.\n"
            f"{EMOJI_VIPERFINDER} **viperfinder** — Soporte para ViperFinder / herramientas relacionadas.\n\n"
            "Pulsa el botón correspondiente para crear un ticket."
        ),
        color=discord.Color.from_rgb(114, 137, 218)
    )

    await ctx.send(embed=embed, view=TicketView())

@bot.command(name="ayuda")
async def ayuda(ctx):
    embed_ayuda = discord.Embed(
        title="📖 Guía de Comandos del Bot",
        description="Aquí tienes la lista de comandos disponibles para administrar y usar el bot:",
        color=discord.Color.green()
    )
    embed_ayuda.add_field(
        name="!panel",
        value="Envía el panel oficial de creación de tickets con todos los botones interactivos. *(Requiere permisos de Administrador)*",
        inline=False
    )
    embed_ayuda.add_field(
        name="!ayuda",
        value="Muestra este mensaje con la lista de comandos del bot.",
        inline=False
    )
    await ctx.send(embed=embed_ayuda)

# Reemplaza 'TU_TOKEN_DE_DISCORD' con el token real de tu bot
bot.run('TU_TOKEN_DE_DISCORD')
        
