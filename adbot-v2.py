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
        game = discord.Game("유저 조회")
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

    if message.content.startswith('/서버정보'):
        channel = message.channel
        await channel.send('**Friendship hub** (은)는 **2020년 4월 27일**에 개설된 서버이며,')
        await channel.send('서버의 소유권을 가지고 있는 유저는 **우정#9444** 님 입니다.')
    if message.content.startswith('/디코주소'):
        channel = message.channel
        await channel.send('https://discord.gg/nEzPCjd')
        await channel.send('**Friendship hub** 의 공식 디스코드 주소입니다.')
    if message.content.startswith('/도움'):
        channel = message.channel
        await channel.send('도움을 요청하셨네요.')
        await channel.send('저를 이용할 수 있는 명령어를 알려드릴게요.')
        await channel.send('> 접두사는 **/** 입니다.')
        await channel.send('> 명령어는 [서버정보 / 디코주소] - 총 2가지입니다.')
    if message.content.startswith("/청소"): # `/청소` 라는 메시지로 시작되었을 때
        if message.content == '/청소': # 메시지가 숫자 없이 `/청소` 만 있다면
            await message.channel.send(f"{message.author.mention}님,  \n청소할 메시지의 수를 적어주세요.") # 숫자를 넣어 달라고 말한다.
        else: # 아니라면 (숫자가 정상적으로 있다면)
            if message.author.guild_permissions.administrator: # 만약 명령어를 실행한 유저가 관리자 권한을 가지고 있다면
                number = int(message.content.split(" ")[1]) # 입력한 숫자만큼 number 변수에 집어넣는다
                await message.delete() # 그만큼 메시지를 지운다
                await message.channel.purge(limit=number) # 대기한다
                a = await message.channel.send(f"{message.author.mention}님,  \n{number}개의 메시지를 삭제했습니다.\n( 이 메시지는 잠시 후에 삭제됩니다. )") # 메시지 삭제 성공을 알린다.
                await asyncio.sleep(2) # 2초 동안 대기한다.
                await a.delete() # 삭제했다는 메시지를 삭제한다.
            else: # 아니라면 (관리자 권한이 없다면)
                await message.channel.send(f"{message.author.mention}님,  \n관리자 권한이 없어 명령어를 실행할 수 없습니다.") # 관리자 권한이 없다는 것을 알린다.
    if message.content == "/핑":
        la = client.latency
        await message.channel.send(f'{message.author.mention}님의 핑은 {str(round(la * 1000))}ms 입니다.')
    if message.content.startswith('/타이머'): # `/타이머` 라는 메시지를 받았을 때
        if message.content == '/타이머': # 만약 메시지가 숫자 없이 `/타이머` 만 있다면
            await message.channel.send(f"{message.author.mention} \n그래서 몇 초를 맞추라고요?\n올바른 명령어는 `/타이머 (숫자)` 에요!") # 몇 초를 맞추라는지 출력한다.
        else: #그렇지 않다면
            timer = int (message.content.split(" ")[1]) # 타이머를 숫자만큼 지정한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 설정되었습니다.\n시간이 끝나면 맨션해드릴게요!") # 설정 완료 메시지를 보낸다.
            await asyncio.sleep(timer) # 그 숫자만큼 대기한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 끝났어요!") # 타이머가 끝났음을 알린다.


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
