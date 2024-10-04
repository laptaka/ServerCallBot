import os

import discord
from discord.ui import Button, View
from dotenv import load_dotenv

from embeds import Embed

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="/call"))
    print(f"{bot.user} is ready and online!")


@bot.user_command(name="Call", description="Call someone!")
@bot.slash_command(name="call", description="Call someone!")
async def call(ctx, user: discord.User):
    icon = ctx.guild.icon.url if ctx.guild.icon else ""
    if ctx.author.voice:
        invite = await ctx.author.voice.channel.create_invite(
            max_age=600, max_uses=1, unique=True)

        incoming_call = Embed.incoming_call(ctx, invite, icon)
        join = Button(emoji="🟢", label="Connect", url=f"{invite}")
        view = View()
        view.add_item(join)
        await user.send(view=view, embed=incoming_call, delete_after=600)

        called = Embed.called(ctx, user)
        await ctx.respond(embed=called, ephemeral=True)
    else:
        noVC = Embed.noVC(ctx)
        await ctx.respond(embed=noVC, ephemeral=True)


bot.run(os.environ["TOKEN"])
