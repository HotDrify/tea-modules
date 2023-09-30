import logging
import asyncio
import itertools
import os
import re

from pyrogram import Client, types
from .. import (
    utils, loader, fsm, validators)
from ..types import Config, ConfigValue

@loader.module(name="bot-bandit", author="hotdrify", version="1.2(teagram)")
class BotBanditMod(loader.Module):
    """автофарм для бота бандита."""
    def __init__(self):
        self.config = Config(
            ConfigValue(
                'run',
                True,
                True,
                validators.Boolean()
            )
        )
    async def load_cmd(self, app: Client, message: types.Message):
        if self.config.get("run"):
            self.tasks = [asyncio.create_task(self.federalrun(app))]
        else:
            self.tasks = []
        await utils.answer(
            message,
            "🌙 обновленно!")
    async def bisrun(self, app): # фарм денег благодаря бизнесу.
        async with fsm.Conversation(app, "@banditchatbot", purge = True) as conv:
            while True:
                commands = ['я', 'бизнес', 'снять деньги', 'склад', 'закупить сырьё', 'закупить на все деньги', 'оплатить']
                for command in commands:
                    await conv.ask(command)
                    await asyncio.sleep(1)
                await asyncio.sleep(86400)
    async def federalrun(self, app): # фарм денег благодаря федералу. (TEST FUNCTION!)
        async with fsm.Conversation(app, "@banditchatbot", purge = True) as conv:
            while True:
                commands = ['я', 'работа', '👮🏻‍♂️ федерал']
                for command in commands:
                    await conv.ask(command)
                    await asyncio.sleep(2)
                msg = await conv.get_response()
                path = await app.download_media(msg, f"cache-{msg.id}.png")
                async with fsm.Conversation(app, "@TranslateIDrobot", purge = True) as conv: # OCR
                    conv.ask_media(path, "photo")
                    await asyncio.sleep(10)
                    msg = await conv.get_response()
                    async with fsm.Conversation(app, "@banditchatbot", purge = True) as conv:
                        os.remove(path)
                        match = re.search(r'ЗАШИФРОВАННОЕ СЛОВО - (\S+)', msg.text)
                        if match:
                            encrypted = match.group(1)
                            words = [''.join(p) for p in itertools.permutations(encrypted)]
                            for word in words:
                                conv.ask(word)
                                await asyncio.sleep(1)
                                msg = await conv.get_response()
                                if msg.text == "окей! ты заработал $6.000. идём дальше.":
                                    pass
                    
