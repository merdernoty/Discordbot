import disnake 
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

CENSORED_WORDS = ["лох"]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
    role_id = 1157627847817560224
    role = member.guild.get_role(role_id)
    channel = member.guild.system_channel

    embed = disnake.Embed(
        title="New Member!",
        description=f"{member.name}#{member.discriminator}",
        color=0xffffff
    )
    await member.add_roles(role)
    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower().replace(" ", "") == censored_word.lower().replace(" ", ""):
                await message.delete()
                await message.channel.send(f"{message.author.mention} Не используйте ненормативную лексику!")

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}", delete_after=10)
    await member.kick(reason=reason)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}", delete_after=10)
    await member.ban(reason=reason)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(mute_members=True, administrator=True)
async def mute(ctx, member: disnake.Member, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} замутил пользователя {member.mention}", delete_after=10)
    await member.mute(reason=reason)
    await ctx.message.delete()

bot.run("MTE1NzI3MTI5ODk4OTM1OTE4NQ.GAp0J2.24i8fuw0UTUrPog1SCx6snRPoA-JuDVfBysxfc")