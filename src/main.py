import os
from discord.ext import commands
from discord import Intents, Permissions, utils, Member

intents = Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)

bot.author_id = 'kuramAZ#1620'  # Change to your discord id!!!


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def name(ctx):
    await ctx.send(f"{ctx.author.name}")


@bot.command()
async def count(ctx):
    res = {}
    for member in ctx.guild.members:
        status = str(member.status)
        if not status in res:
            res[status] = []
        res[status].append(member.name)
    toSend = ""
    statusTab = [("online", "Online"), ("idle", "Idle"),
                 ("dnd", "Do not disturb"), ("offline", "Offline")]
    for status, statusString in statusTab:
        if status in res:
            toSend += "**" + statusString + "**\n"
            for name in res[status]:
                toSend += name + "\n"
            toSend += "\n"
    await ctx.send(toSend)


@bot.command()
async def admin(ctx, param):
    identity = param.split("!")[1].split(">")[0]
    roleName = 'admin_from_bot'
    perms = Permissions(8)
    roleExists = False
    user = None
    role_ = None
    for role in ctx.guild.roles:
        if (role.name == roleName):
            role_ = role
            roleExists = True
    if (not roleExists):
        role_ = await ctx.guild.create_role(name=roleName, permissions=perms)
    for member in ctx.guild.members:
        print(identity)
        if (f'{member.id}' == str(identity)):
            user = member
    role = utils.get(ctx.guild.roles, name=roleName)
    await user.add_roles(role_)


@bot.command()
async def ban(ctx, member: Member):
    await member.ban()


token = "ODkyODIyODA2Mzg2MDU3Mjg3.YVSgCA.SXftHglgMRVUX194ruT6EJ2KdAE"
bot.run(token)  # Starts the bot
