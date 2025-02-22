import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import yt_dlp

# تحميل المتغيرات البيئية
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# إعداد البوت
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
    async def setup_hook(self):
        await self.tree.sync()
        print("تم مزامنة Slash Commands!")

bot = Bot()

# إعدادات yt-dlp
ydl_opts = {
    'format': 'best',
    'noplaylist': True,
}

@bot.event
async def on_ready():
    print(f'{bot.user} تم تشغيل البوت بنجاح!')

@bot.tree.command(name="join", description="الانضمام إلى القناة الصوتية")
async def join(interaction: discord.Interaction):
    if not interaction.user.voice:
        await interaction.response.send_message('يجب أن تكون في قناة صوتية أولاً!')
        return
    
    channel = interaction.user.voice.channel
    if interaction.guild.voice_client is not None:
        await interaction.guild.voice_client.move_to(channel)
    else:
        await channel.connect()
    
    await interaction.response.send_message(f'تم الانضمام إلى {channel}')

@bot.tree.command(name="leave", description="مغادرة القناة الصوتية")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message('تم المغادرة من القناة الصوتية')
    else:
        await interaction.response.send_message('البوت غير متصل بأي قناة صوتية')

@bot.tree.command(name="stream", description="بث المباراة من الرابط المحدد")
async def stream(interaction: discord.Interaction, url: str):
    if not interaction.guild.voice_client:
        await interaction.response.send_message('البوت غير متصل بأي قناة صوتية. استخدم أمر /join أولاً')
        return

    await interaction.response.send_message('جاري تحضير البث...')
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2)
            interaction.guild.voice_client.play(source)
        await interaction.channel.send('بدأ البث!')
    except Exception as e:
        await interaction.channel.send(f'حدث خطأ: {str(e)}')

@bot.tree.command(name="stop", description="إيقاف البث")
async def stop(interaction: discord.Interaction):
    if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
        interaction.guild.voice_client.stop()
        await interaction.response.send_message('تم إيقاف البث')
    else:
        await interaction.response.send_message('لا يوجد بث حالياً')

# تشغيل البوت
bot.run(TOKEN) 