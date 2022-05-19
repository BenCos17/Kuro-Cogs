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

import json
from pathlib import Path
from random import choice

import discord


async def fumo_calling_ritual(self):
    """Fumo API Call."""
    async with self.session.get("https://fumoapi.nosesisaid.me/random") as response:
        if response.status == 200:
            get_fumo = await response.json()
            return get_fumo["URL"]
        else:
            return


async def summon_fumo(self, ctx, type: str):
    """Summon a Fumo."""
    e = discord.Embed(color=await ctx.embed_color())
    if type == "Random":
        fumo = await fumo_calling_ritual(self)
        if fumo:
            e.title = f"Here's a Random Fumo! ᗜˬᗜ"
            e.set_image(url=fumo)
            e.set_footer(
                text="Source: https://fumoapi.nosesisaid.me/",
                icon_url="https://cdn.discordapp.com/emojis/935839733173612594.gif?quality=lossless",
            )
        else:
            return await ctx.send("There's something wrong with the Fumo API, try again later!")
    else:
        with open(Path(__file__).parent / "fumos.json") as fumos:
            fumo = json.load(fumos)
        e.title = f"Here's a Random Fumo {type}! ᗜˬᗜ"
        e.set_image(url=choice(fumo[type]))
    await ctx.send(embed=e)
