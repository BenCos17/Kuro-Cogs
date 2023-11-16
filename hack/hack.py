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
    __version__ = "0.0.3"

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
            await message.edit(content=f"{loading(1)} Finding Discord Login...")
            await asyncio.sleep(2)
            await message.edit(content=f"{loading(2)} Bypassing 2FA...")
            await asyncio.sleep(3)
            email, password = await asyncio.to_thread(get_email_and_password, member)
            await message.edit(
                content=(
                    f"{loading(3)} Found login information:\n"
                    f"**Email**: `{email}`\n"
                    f"**Password**: `{password}`"
                )
            )
            await asyncio.sleep(4)
            await message.edit(content=f"{loading(0)} Fetching user DMs...")
            await asyncio.sleep(1)
            last_dm = await asyncio.to_thread(get_last_dm)
            await message.edit(content=f"{loading(1)} **Last DM**: `{last_dm}`")
            await asyncio.sleep(3)
            await message.edit(content=f"{loading(2)} Injecting trojan virus into {member}...")
            await asyncio.sleep(2)
            await message.edit(content=f"{loading(3)} Virus injected. Finding IP Address...")
            await asyncio.sleep(3)
            # A valid IP address must be in the form of x.x.x.x, where x is a number from 0-255.
            ip_address = f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
            await message.edit(content=f"{loading(0)} **IP Address**: `{ip_address}`")
            await asyncio.sleep(2)
            await message.edit(content=f"{loading(1)} Selling user data to the government...")
            await asyncio.sleep(2)
            await message.edit(
                content=f"{loading(2)} Reporting account to Discord for breaking ToS..."
            )
            await asyncio.sleep(1)
            await message.edit(content=f"{commands.context.TICK} Finished hacking {member.name}.")
            await ctx.send("The *totally* real and dangerous hack is complete.")
        except discord.NotFound:
            await ctx.send("Process terminated. The hack failed.")
            return
        
        
        
# Existing code...

    async def security_challenge(self, ctx: commands.Context):
        """Provides a cybersecurity challenge for users."""
        questions = [
            {
                "question": "What is the most secure type of password?",
                "options": ["123456", "Password123", "aS1!fd$H2f"],
                "answer": "aS1!fd$H2f",
            },
            {
                "question": "Which of these is a common phishing attack method?",
                "options": ["Sending emails from a known sender", "Using secure websites only", "Asking for sensitive information via email"],
                "answer": "Asking for sensitive information via email",
            },
            # Add more questions as needed
        ]

        correct_answers = 0
        for question in questions:
            await ctx.send(f"**Question:** {question['question']}")
            await ctx.send("\n".join(f"{idx + 1}. {option}" for idx, option in enumerate(question['options'])))

            def check_answer(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                user_answer = await self.bot.wait_for('message', check=check_answer, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Time's up!")
                return

            if user_answer.content.lower() == question['answer'].lower():
                correct_answers += 1

        await ctx.send(f"You got {correct_answers} out of {len(questions)} correct!")

    # Remaining code...
