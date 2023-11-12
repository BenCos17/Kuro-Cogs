"""
MIT License

Copyright (c) 2021-present Kuro-Rui

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
from random import randint

import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import humanize_list

from .utils import get_email_and_password, get_last_dm, loading

class Hack(commands.Cog):
    """Le professional hecker."""

    def __init__(self, bot):
        self.bot = bot

    __author__ = humanize_list(["Kuro"])
    __version__ = "0.0.4"

    def cog_unload(self):
        # Optional: Clean up resources when the cog is unloaded
        pass

    def format_help_for_context(self, ctx: commands.Context):
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return (
            f"{pre_processed}\n\n"
            f"`Cog Author  :` {self.__author__}\n"
            f"`Cog Version :` {self.__version__}"
        )

    @commands.guild_only()
    @commands.cooldown(1, 25, commands.BucketType.channel)
    @commands.command(aliases=["heck"])
    async def hack(self, ctx: commands.Context, member: discord.Member):
        """Hack someone!"""

        if member == ctx.author:
            await ctx.send("Umm, please don't DOXX yourself \N{SKULL}")
            return

        # Mass editing lol
        message = await ctx.send(f"{loading(0)} Hacking {member.name} now...")
        await asyncio.sleep(2)

        try:
            # Custom Embed for a more visually appealing output
            embed = discord.Embed(title="Hacking in Progress", color=0x00ff00)
            embed.set_author(name="Le Professional Hacker", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)

            # Initial Embed with the progress bar
            embed.add_field(name="Progress", value=":green_square: :green_square: :green_square: :green_square: :green_square:")

            await message.edit(embed=embed)
            await asyncio.sleep(2)

            # Update Embed for different stages of hacking
            embed.set_field_at(0, name="Progress", value=":white_check_mark: :green_square: :green_square: :green_square: :green_square:")
            await message.edit(embed=embed)
            await asyncio.sleep(2)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :green_square: :green_square: :green_square:")
            await message.edit(embed=embed)
            await asyncio.sleep(3)

            email, password = await asyncio.to_thread(get_email_and_password, member)
            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :green_square: :green_square:")
            embed.add_field(name="Found login information", value=f"**Email**: `{email}`\n**Password**: `{password}`", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(4)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :green_square:")
            embed.add_field(name="Fetching user DMs", value=f"**Last DM**: `{await asyncio.to_thread(get_last_dm)()}`", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(3)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="Injecting trojan virus", value=f"Into {member}...", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(2)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="Virus injected", value="Finding IP Address...", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(3)

            # A valid IP address must be in the form of x.x.x.x, where x is a number from 0-255.
            ip_address = f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="IP Address", value=f"`{ip_address}`", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(2)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="Selling user data", value="To the government...", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(2)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="Reporting account", value="To Discord for breaking ToS...", inline=False)
            await message.edit(embed=embed)
            await asyncio.sleep(1)

            embed.set_field_at(0, name="Progress", value=":white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:")
            embed.add_field(name="Finished hacking", value=f"{member.mention} :white_check_mark:", inline=False)
            await message.edit(embed=embed)

            await ctx.send("The *totally* real and dangerous hack is complete.")
        except discord.NotFound:
            await ctx.send("Process terminated. The hack failed.")
            return
