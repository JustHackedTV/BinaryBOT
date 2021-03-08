import discord
import json
import time
import random
from discord.ext import commands
from discord.ext .commands import has_permissions
from discord.utils import get
from ping import ping

client = commands.Bot(command_prefix=('bin!'))
client.remove_command("help")

@client.event
async def on_ready():
  print("Online")

@client.command()
async def ajuda(ctx):
  emd=discord.Embed(title="Ajuda!", description="bin!decode para passar seu codigo binario para decimais!\n\nbin!encode para transformar uma letra em codigo binario!")
  user=ctx.author
  await ctx.send(f"{user.mention}", embed=emd)

@client.command()
async def encode(ctx, ltr):
  letra=ltr
  if letra=="0":
    await ctx.send("00000")
  elif letra==("A" or "a" or "1"):
    await ctx.send("00001")
  elif letra==("B" or "b" or "2"):
    await ctx.send("00010")
  elif letra==("C"or"c"or"3"):
    await ctx.send("00011")
  elif letra==("D"or"d"or"4"):
    await ctx.send("00100")
  elif letra==("E"or"e"or"5"):
    await ctx.send("00101")
  elif letra==("F"or"f"or"6"):
    await ctx.send("00110")
  elif letra==("G"or"g"or"7"):
    await ctx.send("00111")
  elif letra==("H"or"h"or"8"):
    await ctx.send("01000")
  elif letra==("I"or"i"or"9"):
    await ctx.send("01001")
  elif letra==("J"or"j"or"10"):
    await ctx.send("01010")
  elif letra==("K"or"k"or"11"):
    await ctx.send("01011")
  elif letra==("L"or"l"or"12"):
    await ctx.send("01100")
  elif letra==("M"or"m"or"13"):
    await ctx.send("01101")
  elif letra==("N"or"n"or"14"):
    await ctx.send("01110")
  elif letra==("O"or"o"or"15"):
    await ctx.send("01111")
  elif letra==("P"or"p"or"16"):
    await ctx.send("10000")
  elif letra==("Q"or"q"or"17"):
    await ctx.send("10001")
  elif letra==("R"or"r"or"18"):
    await ctx.send("10010")
  elif letra==("S"or"s"or"19"):
    await ctx.send("10011")
  elif letra==("T"or"t"or"20"):
    await ctx.send("10100")
  elif letra==("U"or"u"or"21"):
    await ctx.send("10101")
  elif letra==("V"or"v"or"22"):
    await ctx.send("10110")
  elif letra==("W"or"w"or"23"):
    await ctx.send("10111")
  elif letra==("X"or"x"or"24"):
    await ctx.send("11000")
  elif letra==("Y"or"y"or"25"):
    await ctx.send("11001")
  elif letra==("Z"or"z"or"26"):
    await ctx.send("11010")
  elif letra==("27"):
    await ctx.send("11011")
  elif letra==("28"):
    await ctx.send("11100")
  elif letra==("29"):
    await ctx.send("11101")
  elif letra==("30"):
    await ctx.send("11110")
  elif letra==("31"):
    await ctx.send("11111")
  else:
    await ctx.send("Numero ou letra invalida!")

@client.command()
async def decode(ctx, bin):
  Binario=bin
  if Binario=="00000":
    await ctx.send("0 (espaço)")
  elif Binario=="00001":
    await ctx.send("1 A")
  elif Binario=="00010":
    await ctx.send("2 B")
  elif Binario=="00011":
    await ctx.send("3 C")
  elif Binario=="00100":
    await ctx.send("4 D")
  elif Binario=="00101":
    await ctx.send("5 E")
  elif Binario=="00110":
    await ctx.send("6 F")
  elif Binario=="00111":
    await ctx.send("7 G")
  elif Binario=="01000":
    await ctx.send("8 H")
  elif Binario=="01001":
    await ctx.send("9 I")
  elif Binario=="01010":
    await ctx.send("10 J")
  elif Binario=="01011":
    await ctx.send("11 K")
  elif Binario=="01100":
    await ctx.send("12 L")
  elif Binario=="01101":
    await ctx.send("13 M")
  elif Binario=="01110":
    await ctx.send("14 N")
  elif Binario=="01111":
    await ctx.send("15 O")
  elif Binario=="10000":
    await ctx.send("16 P")
  elif Binario=="10001":
    await ctx.send("17 Q")
  elif Binario=="10010":
    await ctx.send("18 R")
  elif Binario=="10011":
    await ctx.send("19 S")
  elif Binario=="10100":
    await ctx.send("20 T")
  elif Binario=="10101":
    await ctx.send("21 U")
  elif Binario=="10110":
    await ctx.send("22 V")
  elif Binario=="10111":
    await ctx.send("23 W")
  elif Binario=="11000":
    await ctx.send("24 X")
  elif Binario=="11001":
    await ctx.send("25 Y")
  elif Binario=="11010":
    await ctx.send("26 Z")
  else:
    await ctx.send("Binario invalido!")

ping()
f = open('token.json')
token = json.load(f)['token']
client.run(token)