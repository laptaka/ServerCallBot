import discord


class Embed:
    def incoming_call(ctx, invite, icon):
        incoming_call_embed = discord.Embed(
            title="Incoming call", description="{} is calling you!".format(ctx.author.mention),
            color=discord.Colour.green(), url=invite)
        incoming_call_embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        incoming_call_embed.set_thumbnail(url=icon)
        incoming_call_embed.add_field(name="Server", value=ctx.guild.name, inline=True)
        incoming_call_embed.add_field(name="Channel", value=ctx.author.voice.channel.name, inline=True)
        return incoming_call_embed

    def called(ctx, user):
        called_embed = discord.Embed(
            title="Outgoing call", description="Calling {}...".format(user.mention), color=discord.Colour.blurple())
        called_embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        return called_embed

    def noVC(ctx):
        no_vc_embed = discord.Embed(
            title="Error", description="Join a VC first!", color=discord.Colour.red())
        no_vc_embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        return no_vc_embed
