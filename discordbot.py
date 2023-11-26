import discord, random
from discord.ui import Button, View, Modal, TextInput
from discord import app_commands, Interaction, Object, ButtonStyle

bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)
 
owner = 786571191435395072

# 홍보 감지 키워드
DISCORD_KEYWORDS = ["https", "discord.gg", "discord.com/invite"] 

BASE = "https://discord.com/api/v9/"

class button1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="자리비움해제", custom_id="b1")
    async def press_me1(self, interaction: discord.Interaction, button: discord.ui.Button):
      close1= discord.Embed(title=' ', description=f'<@{interaction.user.id}> 님이 자리비움 해제 상태입니다.', color = 5564250, timestamp=interaction.created_at)
      close1.set_footer()
      await bot.get_channel(1157616419144486983).send(embed=close1)
      await interaction.followup.send("> 출퇴근 메시지를 전송하였습니다!", ephemeral=True)

      
    @discord.ui.button(label="자리비움", custom_id="b2")
    async def press_me2(self, interaction: discord.Interaction, button: discord.ui.Button):
      close1 = discord.Embed(title=f' ', description=f'<@{interaction.user.id}> 님이 자리비움 상태입니다.', color = 15160404, timestamp=interaction.created_at)
      close1.set_footer()
      await bot.get_channel(1157616419144486983).send(embed=close1)
      await interaction.followup.send("> 출퇴근 메시지를 전송하였습니다!", ephemeral=True)

@tree.command(name = "자리비움", description = "자리비움 상태 설정")
async def cal(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.defer()
        embed = discord.Embed(title=' ', description = "원하시는 버튼을 클릭해주세요.", color=11661534)
        await interaction.user.send(embed=embed, view=button1())     

@tree.command(name = "계좌", description = "계좌번호를 보여줍니다.")
async def cal(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.defer()
        embed = discord.Embed(title=' ', description = "<a:pinkstar:1162799982529740810> 7777 - 03 - 0547694 ( 카카오뱅크 ㅊㅈㅇ )", color=11661534)
        await interaction.followup.send(embed=embed)     

@tree.command(name = "공지", description = "공지사항을 작성합니다.")
async def cal(interaction: discord.Interaction, notice: str):
    if interaction.user.id == owner:
        await interaction.response.defer()
        random_color = random.choice([15204258, 12124066, 16754338, 10682322, 10682356, 10673919, 11641599, 16753403])
        chembed = discord.Embed(title="**[ Lunar Shop 공지사항 💕 ]**", description=f"{notice}", color=random_color)
        await bot.get_channel(1155106266289553428).send("( @everyone ) **HAEZONE**", embed=chembed)
        complete = discord.Embed(title=" ", description="공지 메시지를 전송 완료하였습니다 ✔", color=2838232)
        await interaction.followup.send(embed=complete)


@bot.event
async def on_ready():
    print("[ Bot Starting.. ]")
    await tree.sync()
    print("[  Bot Started!  ]")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="루나샵 관리"))

@bot.event
async def on_message(message):
    if message.channel.id == 1155142059703939122:
        await message.add_reaction("<a:blueheart:1155448965886644305>")

    if message.content.startswith("!청소 "):
        if message.author.id == 786571191435395072:
            amount = message.content[4:]
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림 📢", description=f"최근 디스코드 채팅 {amount}개가\n{message.author.mantion}님의 요청으로 정상 삭제 되었습니다!", color=11661534)
            await message.channel.send(embed=embed)

    if not message.author.bot:
        if message.channel.id != 1155159597108187206:
            if any(keyword in message.content.lower() for keyword in DISCORD_KEYWORDS):
                if message.author.id != owner:
                    await message.delete() # 무단 홍보 삭제
                    
@bot.event #Join Dm
async def on_member_join(member):
    embed = discord.Embed(title=f'HAEZONE에 오신걸 환영합니다!', description=f'인증을 하셔야 채널이 보입니다!', color = 10658559)
    await member.send(f"[  {member}  ] 입장안내 🎈", embed=embed)

    random_color = random.choice([15204258, 12124066, 16754338, 10682322, 10682356, 10673919, 11641599, 16753403])
    join = discord.Embed(title=f"<@{member.id}> 님이 입장하셨어요!", description=f"**Server Name** : HAEZONE\n**Member ID**: {member.id}\n**Member Tag** : {member}", color=random_color)
    await bot.get_channel(1168044693616066670).send(embed=join)

@bot.event #Join Dm
async def on_member_remove(member):


    random_color = random.choice([15204258, 12124066, 16754338, 10682322, 10682356, 10673919, 11641599, 16753403])
    join = discord.Embed(title=f"<@{member.id}> 님이 퇴장하셨어요!", description=f"**Server Name** : HAEZONE\n**Member ID**: {member.id}\n**Member Tag** : {member}", color=random_color)
    await bot.get_channel(1168044711169228830).send(embed=join)

bot.run("MTE3ODIzOTQ0MTE1Njk3MjU5NQ.G2Fc9h.EYfnYae1R72Exl3sNSsUyUVtQueO8NtlgjLTq4")

