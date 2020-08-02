#!/usr/bin/env python

"""
Koala Bot Cog prividing Social Feed updates
Commented using reStructuredText (reST)
TODO: - FB GraphAPI Wrapper
      - Page Access Tokens
      - Display top item in feed
      - similar structure for Instagram + Twitter

"""
# Futures

# Built-in/Generic Imports
import os
import time
import asyncio
import concurrent.futures

# Libs
import discord
import facebook
from discord.ext import commands
from dotenv import load_dotenv
import requests

# Own modules
import KoalaBot

# Constants
load_dotenv()


# Variables


class SocialAlert(commands.Cog):
    """
        A discord.py cog for providing social feed updates from Facebook, Instagram and Twitter
    """


pass


class FacebookGraphAPIHandler:
    """
    A wrapper to interact with the Facebook GraphAPI
    """

    def __init__(self, client_id: str, client_secret: str, short_token: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.short_token = short_token
        self.oauth_token = self.get_new_facebook_oauth()
        self.graph = facebook.GraphAPI(self.oauth_token)

    def get_new_facebook_oauth(self):
        """
        Get a new long-lived access token from Facebook
        :return: New long-lived access token
        """
        access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(
            self.client_id, self.client_secret, self.short_token)
        return requests.get(access_token_url).json()['access_token']

    def get_post_info(self, page_id):
        """
        Gets default fields for the most recent post on a page feed
        :param page_id: ID of the page
        :return: Dictionary with the post's data
        """
        return self.graph.get_connections(page_id, connection_name="feed", limit=1)

    def get_page_info(self, page_id):
        """
        Gets default fields (name and id) for a specified page
        :param page_id: ID of the page
        :return: Dictionary with the page's data
        """
        return self.graph.get_object(page_id)


def setup(bot: KoalaBot) -> None:
    """
    Load this cog to the KoalaBot.
    :param bot: the bot client for KoalaBot
    """
    bot.add_cog(SocialAlert(bot))