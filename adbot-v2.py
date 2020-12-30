import asyncio
import discord
import os

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "NzkzNzc4MjE4MTQ2MDcwNTg4.X-xNkg.95WELDXND9tnmUpyO_WCE3gHj38"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.dnd, activity=game)
    while True:
        game = discord.Game("Made by 우정#9444")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("discord.gg/nEzPCjd")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("24시간 풀 가동")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("유저 관리")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("Powerd by PYTHON")
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('/조회'):
        channel = message.channel
        await channel.send('유저ID 조회를 시작합니다...🔍')
        await channel.send('잠시만 기다려주세요...🕓')
        await channel.send('유저의 ID를 조회하는중입니다...🔍')
        await channel.send('유저ID 조회가 거의 완료되었습니다...📊')
        await channel.send('유저ID 조회완료!✅')

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
