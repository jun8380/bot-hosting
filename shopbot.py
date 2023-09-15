import discord
from discord.ui import Button, View
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# 주문로그 채널의 ID를 지정합니다.
order_log_channel_id = 1152249485909565530

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was successful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("TUNGSHOP에서 일"))

@bot.command()
async def 주문(ctx):
    async def button_callback1(interaction):
        # 임베드 생성
        embed = discord.Embed(
            title="로고 주문",
            description="로고를 주문하려면 아래 양식을 확인하세요:",
            color=discord.Color.green()
        )
        embed.add_field(name="로고 주문 양식", value="[디스코드 아이디/닉네임]을 보내주세요")

        # 메시지로 임베드를 보냅니다.
        await interaction.response.send_message(embed=embed, ephemeral=False)

        # 유저의 응답을 기다립니다.
        response = await bot.wait_for("message", check=lambda message: message.author == interaction.user)
        
        # 주문 내용에 버튼 정보와 유저의 응답을 추가합니다.
        order_content = f"주문 내용: 로고/{response.content}"
        
        # 주문이 접수되었습니다! 임베드를 보냅니다.
        response_embed = discord.Embed(
            title="주문이 접수되었습니다!",
            description=order_content,
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=response_embed)

        # 주문로그 채널을 찾아서 임베드를 보냅니다.
        order_log_channel = ctx.guild.get_channel(order_log_channel_id)
        if order_log_channel:
            await order_log_channel.send(embed=response_embed)

    async def button_callback2(interaction):
        # 임베드 생성
        embed = discord.Embed(
            title="모션그래픽 주문",
            description="모션그래픽을 주문하려면 아래 양식을 확인하세요:",
            color=discord.Color.green()
        )
        embed.add_field(name="모션그래픽 주문 양식", value="[디스코드 아이디/닉네임]을 보내주세요")

        # 메시지로 임베드를 보냅니다.
        await interaction.response.send_message(embed=embed, ephemeral=False)

        # 유저의 응답을 기다립니다.
        response = await bot.wait_for("message", check=lambda message: message.author == interaction.user)
        
        # 주문 내용에 버튼 정보와 유저의 응답을 추가합니다.
        order_content = f"주문 내용: 모션그래픽/{response.content}"
        
        # 주문이 접수되었습니다! 임베드를 보냅니다.
        response_embed = discord.Embed(
            title="주문이 접수되었습니다!",
            description=order_content,
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=response_embed)

        # 주문로그 채널을 찾아서 임베드를 보냅니다.
        order_log_channel = ctx.guild.get_channel(order_log_channel_id)
        if order_log_channel:
            await order_log_channel.send(embed=response_embed)

    button1 = Button(label="로고", style=discord.ButtonStyle.green)
    button2 = Button(label="모션그래픽", style=discord.ButtonStyle.green)

    button1.callback = button_callback1
    button2.callback = button_callback2

    view = View()
    view.add_item(button1)
    view.add_item(button2)

    await ctx.send(embed=discord.Embed(title='TUNGTUNG2SHOP', description="원하시는 상품을 선택해주세요", color=discord.Colour.blue()), view=view)

bot.run('MTE1MTg0NzE2NDY5MjEzNTk2Ng.G-1o1H.4-hJGisReqQfqWaEfo3EbIsxU_N7D2WS_Lx68I')