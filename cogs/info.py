import discord
from discord.ext import commands


class info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command()
    async def info(ctx, user: discord.Member):
        'get info on somebody'
        await ctx.send('The users name is: {}'.format(user.name))
        await ctx.send('The users ID is: {}'.format(user.id))
        await ctx.send('The users status is: {}'.format(user.status))
        await ctx.send('The users highest role is: {}'.format(user.top_role))
        await ctx.send('The user joined at: {}'.format(user.joined_at))


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(info(bot))
