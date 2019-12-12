import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

prefix = "!"

Bot = commands.Bot(command_prefix= [prefix])

Bot.remove_command("help")

@Bot.event
async def on_ready():
    print("Online")

@Bot.command(pass_context= True)
async def привет(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention} здравствуй")

@Bot.command(pass_context= True)
async def информация(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention}, меня создал @Евгений Валентинович#7861, если хочешь себе собственного бота - пиши ему!")

@Bot.command(pass_context= True)
async def команды(ctx):
    emb = discord.Embed(title = "Команды")

    emb.add_field(name = "{}ip".format(prefix),value = "Узнать ip сервера")
    emb.add_field(name = "{}информация".format(prefix),value = "Информация о боте")
    emb.add_field(name = "{}обновление".format(prefix),value = "Узнать последнее обновление на сервере")
    emb.add_field(name = "{}привет".format(prefix),value = "Поздороваться со мной")

    await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def обновление(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention}, в данный момент сервер еще не запущен")

@Bot.command(pass_context= True)
async def информативно(ctx):
    await ctx.send("Согласен")

@Bot.command(pass_context= True)
async def ip(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention}, ip сервера: 80.93.187.158:27415")   

token = os.environ.get("BOT_TOKEN")
