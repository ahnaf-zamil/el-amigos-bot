import discord
from discord.ext import commands
import random
from datetime import datetime

token = 'NzE3Mzc5MTc2NDY1OTU2OTY0.XtZd9A.UvkR2ETmFsLk4Ay_2_QdmNA3PUU'

client = commands.Bot(command_prefix = '$')
client.remove_command('help')



@client.event
async def on_ready():
    
    print('Logged in as {0.user}'.format(client))

@client.command()
async def get_server_icon_url(ctx):
    icon_url = ctx.guild.icon_url
    await ctx.send(icon_url)


@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}ms")

@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    responses = ['As I see it, yes',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don’t count on it',
                'It is certain',
                'It is decidedly so',
                'Most likely',
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Outlook good',
                'Reply hazy, try again',
                'Signs point to yes',
                'Very doubtful',
                'Without a doubt',
                'Yes',
                'Yes – definitel',
                'You may rely on it']

    reply = f"Question: {question}\n{random.choice(responses)} {ctx.message.author.mention}."



    await ctx.send(reply)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member, *, reason):
    
        await user.kick(reason=reason)
        await ctx.send(f"{user} has been banned by {ctx.message.author.mention} due to {reason}.")
    
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason):
    
        await user.ban(reason=reason)
        await ctx.send(f"{user} has been kicked by {ctx.message.author.mention} due to {reason} for ∞.")

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.name}#{user.discriminator} has been unbanned by {ctx.message.author.mention}.")
            return


@client.command()
async def help(ctx):
    desc = """
    
    **Bot prefix is '$'**

    help - Shows this message

    ping - Shows you latency between the bot and Discord

    8ball [question] - Ask the bot about an 8ball question

    kick [mention-user] [reason] - Kicks a specific user (Requires admin permissions)

    ban [mention-user] [reason] - Bans a user until he/she is unbanned (Requires admin permissions)

    unban [discord-username] - Unbans user (Requires admin permissions)
    
    members - Get number of members in a server


    """
    embed = discord.Embed(
        description = desc,
        color = discord.Color.blue()
    )

    embed.set_footer(text=f'© K.M Ahnaf Zamil {int(datetime.now().year)}')
    embed.set_author(name='List of Commands', icon_url='https://discord.com/assets/dd4dbc0016779df1378e7812eabaa04d.png')
    await ctx.send(embed = embed)

@client.command()
async def members(ctx):
    server = ctx.message.author.guild
    await ctx.send(f"{server.name} has {server.member_count} members.")

@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)

client.run(token)