#          █░█ █▀█ ▀█▀ █▀▄ █▀█ █ █▀▀ █▄█
#          █▀█ █▄█ ░█░ █▄▀ █▀▄ █ █▀░ ░█░
#          🔒 Licensed under the GNU AGPLv3.
#                    @HotDrify
from pyrogram import Client, types
from .. import (
    loader, utils, validators)
from ..types import Config, ConfigValue

import requests
import json

@loader.module(name="auto-correct", author="HotDrify", version="1.5")
class AutoCorrectMod(loader.Module):
    """❤️ автоматическое исправление текста."""
    def __init__(self):
        self.config = Config(
            ConfigValue(
                'api_base',
                'https://speller.yandex.net/services/spellservice.json/checkText',
                'https://speller.yandex.net/services/spellservice.json/checkText',
                validators.String(),
            ),
            ConfigValue(
                'is_slash',
                True,
                True,
                validators.Boolean(),
            ),
            ConfigValue(
                'is_link',
                True,
                True,
                validators.Boolean(),
            ),
            ConfigValue(
                'is_slash',
                True,
                True,
                validators.Boolean(),
            ),
            ConfigValue(
                'status',
                True,
                True,
                validators.Boolean(),
            ),
            ConfigValue(
                'lang',
                'ru',
                'ru',
                validators.String()
            )
        )
    
    async def watcher(self, app: Client, message: types.Message):
        if not self.config["status"]:
            return
        if self.config["is_ping"]:
            if "@" in message.text:
                return
        if self.config["is_slash"]:
            if "/" in message.text:
                return
        if self.config["is_link"]:
            if "https" in message.text or "http" in message.text:
                return
                
        response = requests.get(
            self.config["api_base"],
            params = {
                'text': message.text,
                'lang': self.config["lang"],
                'options': 512
            }
        )
        
        data = response.json()
        ctext = message.text
        
        for mistake in data:
            ctext = ctext[:mistake['pos']] + mistake['s'][0] + ctext[mistake['pos']+mistake['len']:]
        
        if message.text != ctext:
            await utils.answer(message, ctext)