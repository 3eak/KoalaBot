#!/usr/bin/env python

"""
Koala Bot Intro Message Cog Code

Commented using reStructuredText (reST)
"""
# Futures

# Built-in/Generic Imports

# Libs
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Own modules
import KoalaBot
from utils import KoalaDBManager

# Constants
load_dotenv()
BASE_LEGAL_MESSAGE = """This server utilizes KoalaBot. In joining this server, you agree to the Terms & Conditions of 
KoalaBot and confirm you have read and understand our Privacy Policy. For legal documents relating to this, please view 
the following link: http://legal.koalabot.uk/"""

# Variables
DBManager = KoalaDBManager.KoalaDBManager(KoalaBot.DATABASE_PATH)


async def dm_group_message(members, message):
    """
    DMs members in a list of members
    :param members: list of members to DM
    :param message: The message to send to the group
    :return: how many were dm'ed successfully.
    """
    count = 0
    for member in members:
        try:
            await member.send(message)
            count = count + 1
        except Exception:  # In case of user dms being closed
            pass
    return count


def get_guild_welcome_message(guild_id: int):
    """
    Retrieves a guild's customised welcome message from the database. Includes the basic legal message constant
    :param guild_id: ID of the guild
    :return: The particular guild's welcome message : str
    """
    welcome_messages = DBManager.db_execute_select(sql_str=
                                                   f"""SELECT * FROM GuildWelcomeMessages WHERE guild_id = '{guild_id}';""")
    if len(welcome_messages) < 1:
        # If there's no current row representing this (for whatever reason), add one to the table
        DBManager.db_execute_commit(sql_str=
                                    f"""INSERT INTO GuildWelcomeMessages (guild_id, welcome_message) VALUES ({guild_id}, 'default message');""")
        welcome_message_row = [0, 'default message']
    else:
        # Return the one that exists
        welcome_message_row = welcome_messages[0]

    guild_welcome_message = welcome_message_row[1]
    return f"{guild_welcome_message} \r\n {BASE_LEGAL_MESSAGE}"


class IntroCog(commands.Cog):
    """
    A discord.py cog with commands pertaining to the welcome messages that a member will receive
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        On bot joining guild, add this guild to the database of guild welcome messages.
        :param guild: Guild KoalaBot just joined
        """
        if (len(DBManager.db_execute_select(
                f"""SELECT * FROM GuildWelcomeMessages WHERE guild_id == {guild.id};""")) == 0):
            DBManager.db_execute_commit(
                sql_str=f"""INSERT INTO GuildWelcomeMessages (guild_id,welcome_message) VALUES({guild.id},'default message');""")
        else:
            # There already exists an entry in this table. Reset to default
            DBManager.db_execute_commit(
                f"""UPDATE GuildWelcomeMessages SET welcome_message = '{get_guild_welcome_message(guild.id)}'""")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.member):
        """
        On member joining guild, send DM to member with welcome message.
        :param member: Member which just joined guild
        """
        await dm_group_message([member], get_guild_welcome_message(member.guild.id))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """
        On bot leaving guild, remove the guild from the database of guild welcome messages
        :param guild: Guild KoalaBot just left
        """
        DBManager.db_execute_commit(f"""DELETE FROM GuildWelcomeMessages WHERE guild_id = {guild.id};""")
        import datetime
        print(f"{datetime.datetime.now()}: KoalaBot has left guild {guild.id}.")

    @commands.check(KoalaBot.is_admin)
    @commands.command(name="send_welcome_message")
    async def send_welcome_message(self, ctx):
        """
        Allows admins to send out their welcome message manually to all members of a guild.
        :param ctx: Context of the command
        """
        non_bot_members = [member for member in ctx.guild.members if not member.bot]

        await ctx.send(f"This will DM {len(non_bot_members)} people. Are you sure you wish to do this? Y/N")

        try:
            confirmation_message = await self.bot.wait_for('message', timeout=5.0,
                                                           check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.send('Timed out')
        else:
            conf_msg = confirmation_message.content.rstrip().strip().lower()
            if conf_msg not in ['y', 'n']:
                await ctx.send('Invalid input. Please restart with the command.')
            else:
                if conf_msg == 'n':
                    await ctx.send('Okay, I won\'t send the welcome message out.')
                else:
                    await dm_group_message(non_bot_members,
                                           get_guild_welcome_message(ctx.guild.id))

    @commands.check(KoalaBot.is_admin)
    @commands.command(name="update_welcome_message")
    async def update_welcome_message(self, ctx, *, new_message: str):
        """
        Allows admins to change their customisable part of the welcome message of a guild.
        :param ctx: Context of the command
        :param new_message: New customised part of the welcome message
        """
        await ctx.send("""Your current welcome message is: \r\n {0}
        \r\n\r\n Your new welcome message will be: \r\n {1}
        \r\n\r\n Do you accept this change? Y/N""".format(get_guild_welcome_message(ctx.message.guild.id),
                                                          f"{new_message}\r\n{BASE_LEGAL_MESSAGE}"))

        try:
            confirmation_message = await self.bot.wait_for('message', timeout=5.0,
                                                           check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.send('Timed out')
        else:
            conf_msg = confirmation_message.content.rstrip().strip().lower()
            if conf_msg not in ['y', 'n']:
                await ctx.send('Invalid input. Please restart with the command.')
            else:
                if conf_msg == 'n':
                    await ctx.send('Not changing welcome message then.')
                else:
                    DBManager.db_execute_commit(
                        sql_str=f"""UPDATE GuildWelcomeMessages SET welcome_message = '{new_message}' WHERE guild_id = {ctx.message.guild.id};""")
                    await ctx.send(f"Your new custom part of the welcome message is {new_message}")

    @update_welcome_message.error
    async def on_update_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await ctx.send('Please put in a welcome message to update to.')


def setup(bot: KoalaBot) -> None:
    """
    Loads this cog into the selected bot
    :param bot: The client of the KoalaBot
    """
    bot.add_cog(IntroCog(bot))
