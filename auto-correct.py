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
        