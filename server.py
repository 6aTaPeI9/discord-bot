import discord
from discord.ext import commands

# CHANNELS = {
#     'welcome': 696289457514741820,
#     'GuildMember': {'Name': 'основа', 'Id': 696289663479971840},
#     'AcademiMember': {'Name': 'академия', 'Id': 696289801938272266}
# }

CHANNELS = {
    'welcome': 694230411966021633,
    'Академик': {'Name': 'основа', 'Id': 696814150621331567},
    'Участник': {'Name': 'академия', 'Id': 696814206921736322}
}

COMMAND_PREFIX = '!'

BOT = commands.Bot(command_prefix=COMMAND_PREFIX)

@BOT.event
async def on_member_join(member):
    """
        Обработка события подключения нового пользователя к серверу
    """
    channel = BOT.get_channel(CHANNELS['welcome'])

    if not channel:
        return

    await channel.send(embed=get_welcome_embed(member))

@BOT.event
async def on_member_update(before, after):
    """

    """
    if len(before.roles) >= len(after.roles):
        return
    
    new_role = next(role for role in after.roles if role not in before.roles)
    
    if not new_role:
        return

    channel = CHANNELS.get(new_role.name)

    if channel:
        remote_channel = BOT.get_channel(channel.get('Id'))
        await remote_channel.send(embed=get_guild_rules_embed(after))

@BOT.event
async def on_ready():
    """
        Обрабатываем запуск бота. Создаем каналы если требуется, настраиваем роутинг
    """
    # res = list(BOT.get_all_channels())
    # print(len(res))
    # print(res)
    # channels = {}
    # for row in res:
    #     print(row.id)
    # print(channels)
    print('started')

@BOT.event
async def on_message(message):
    """
        Обработка входящих сообщений, с переопределением комманд
    """

    if message.author == BOT.user:
        return

    if message.content[0] == COMMAND_PREFIX:
        await BOT.process_commands(message)
    # else:
    #     if len(message.mentions) > 0:
    #         images = ''
    #         for user in message.mentions:
    #             images += str(user.avatar_url) + str('\n')
    #         await message.channel.send(images)
    #     else:
    #         await message.channel.send(f'<@{message.author.id}>')

@BOT.command()
async def ping(ctx: discord.ext.commands.Context):
    """

    """
    await ctx.message('still alive!')

@BOT.command()
async def grant_me_permissions(ctx, member: discord.Member = None):
    print('test')

    # embed.add_field(name="Имя:", value=member.display_name)
    # embed.add_field(name="Создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    # embed.add_field(name="Присоединился:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    # embed.add_field(name=f"Роли ({len(roles)})", value=" ".join([role.mention for role in roles]))
    # embed.add_field(name="Лучшая роль:", value=member.top_role.mention)


def get_welcome_embed(member: discord.Member):
    """

    """
    embed = discord.Embed(
        colour=0x00ff00,
        description=f'Привет <@{member.id}>!\n Если ты являешься участником гильдии: \n\n'\
                'Отправь сообщение со своим игровым ником в канал <#696264696483020800>, '\
                'чтобы офицеры гильдии смогли выдать тебе права на основные '\
                'каналы сервера.\n\n\n',
        title=':beers:Добро пожаловать в группу гильдии Mad Hatters!:beers:'
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/BVjOU0swUsVSENZ61pwp6s62ARSCl_mkN5wTQtfYSjM/%3Fwidth%3D845%26height%3D476/https/media.discordapp.net/attachments/574888402261114890/685499531554455585/KH_Backdrop_Tavern_01_1920x1080.png')

    return embed


def get_guild_rules_embed(member: discord.Member):
    """

    """
    embed = discord.Embed(
        colour=0x00ff00,
        description=':fire: Ты получишь::fire:\n'\
            '-<#684342361513394186>\n'\
            '-Поддержку\n'\
            '-Фан\n'\
            '-Актуальные новости\n'\
            '-Боссы\n'\
            '-Статистику о себе\n\n'\
            ':man_with_probing_cane: При условии, что будешь соблюдать::man_with_probing_cane:\n'\
            '-Чтение канала <#684350097823236106> и <#684340800875790383>\n'\
            '-Выполнение указаний из этих каналов\n'\
            '-Соблюдение правил клана\n'\
            '-Будешь активным\n'\
            '-Никакого буллинга :man_gesturing_no:\n\n'\
            ':knife: Правила::knife:\n'\
            '- 2 дня не на связи в игре/дискорде = кик\n'\
            '- Не вести себя агрессивно\n'\
            '- Набирать норму по славе. Норма - 500 очков, как заработать - канал "гайды"\n'\
            '- Не бегать по кланам без разрешения\n'\
            '- Не вводить в заблуждение других\n\n',
        title=f'<@{member.display_name}> добро пожаловать в Mad Hatters :black_joker:!'
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/BVjOU0swUsVSENZ61pwp6s62ARSCl_mkN5wTQtfYSjM/%3Fwidth%3D845%26height%3D476/https/media.discordapp.net/attachments/574888402261114890/685499531554455585/KH_Backdrop_Tavern_01_1920x1080.png')

    return embed


if __name__ == '__main__':
    BOT.run('NjkxOTM4MDE0NjgyOTM5NDEz.Xnt8Lg.0dDK-RXqMWp2Ob2zPhhzUFudaqY')
