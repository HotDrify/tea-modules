import logging
import asyncio
from pyrogram import types, Client
from .. import (
    loader, utils, validators)
from ..types import Config, ConfigValue
import json

@loader.module(name="Filters", author="HotDrify")
class FiltersMod(loader.Module):
  """импортированы фильтры из известного юзербота FTG"""
  def __init__(self):
    self.config = Config(
        ConfigValue(
            'waitTime',
            0.0,
            0.0,
            validators.Integer(minimum=0.0, maximum=10.0)
        )
    )
    async def filter_cmd(self, message: types.Message, args: str):
        """добавить фильтр"""
        filters = self.db.get("Filters", "filters", {})
        data = json.loads(str(filters))
        if not message.reply_to_message:
            return await utils.answer(message, "🚫 нету перлея на сообщение.")
        if message.reply_to_message.text in filters:
            return await utils.answer(message, "🚫 уже есть.")
        if not args:
            return await utils.answer(message, "🚫 нету агрументов!")
        data[str(message.chat.id)] = {args: message.reply_to_message.text}
        upd = json.dumps(data)
        self.db.set("Filters", "filters", upd)
        await utils.answer(message, f"✅ фильтр <b>{args}</b> сохранен.")
    async def stopall_cmd(self, message: types.Message, args: str):
        """остановить фильтры"""
        filters = self.db.get("Filters", "filters", {})
        if message.chat.id not in filters:
            return await utils.answer(message, "🚫 нету в фильтрах!")
        #if not args:
        #    return await utils.answer(message, "🚫 нужны аргументы!")
        del data[message.chat.id]
        upd = json.dumps(data)
        self.db.set("Filters", "filters", upd)
        await utils.answer(message, f"✅ фильтры чата удалены")
    @loader.on(lambda _, m: m)
    async def watcher(self, app: Client, message: types.Message):
        filters = self.db.get("Filters", "filters", {})
        if str(message.chat.id) in filters:
            if message in filters:
                await message.reply(filters[message])
    
