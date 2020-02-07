import discord
import asyncio
import os
token=os.environ["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
    await client.get_channel(int(673867494783713300)).send("해피의 탑을 시작하지..")

@client.event
async def on_message(message):
    try:
        if message.content.startswith('/정답'):
            if message.author.bot:
                return None
            if message.content == '/정답 해피디스코드':
                print(f'{message.author.name}(' + f'{message.author.id}) : ' + message.content)
                author = message.author
                role = discord.utils.get(message.guild.roles, name="1층")
                await author.add_roles(role)
                await message.delete()
                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                embed.add_field(name="해피의 탑 로비", value="정답", inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content == '/정답 맞추기':
                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                embed.add_field(name="해피의 탑 로비", value="고고!!", inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                print(f'{message.author.name}(' + f'{message.author.id}) : ' + message.content)
                author = message.author
                role = discord.utils.get(message.guild.roles, name="로비")
                await author.add_roles(role)
                await message.delete()
            else:
                await message.delete()
                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                embed.add_field(name="해피의 탑 로비", value="오답", inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

    except Exception as ex:
        embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
        embed.add_field(name=":no_entry_sign: 오류!! ERROR!! :no_entry_sign:", value=f'에러랍니다! 봇에서 많이 발생해요!\n<@652509076055523338>한테 캡처해서 보내주세여.\n에러 내용 : {str(ex)}', inline=True)
        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        print(f'오류 발생, 에러 내용 : {str(ex)}')
        await message.channel.send(embed=embed)

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game(client.user.name + '입니다.')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'{len(client.users)}명을 위한 해피의 탑 진행중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game('해피의 탑 OPEN!!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
client.loop.create_task(my_background_task())

client.run(token)
os.execv(sys.executable, ['python']+sys.argv)
