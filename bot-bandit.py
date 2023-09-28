import logging
import asyncio

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
                validators.Boolean()
            ),
            ConfigValue(
                'wait',
                1,
                validators.Integer(minimum=1, maximum=5)
        )
    async def load_cmd(self, app: Client, message: types.Message):
        if self.config.get("run"):
            self.tasks = [asyncio.create_task(self.botrun(app))]
        else:
            self.tasks = []
        await utils.answer(
            message,
            "🌙 обновленно!")
    async def botrun(self, app):
        while True:
            async with fsm.Conversation(app, "@banditchatbot", purge = True) as conv:
                commands = ['я', 'бизнес', 'снять деньги', 'склад', 'закупить сырьё', 'закупить на все деньги', 'оплатить']
                for command in commands:
                    await conv.ask(command)
                    await asyncio.sleep(self.config.get("wait"))
