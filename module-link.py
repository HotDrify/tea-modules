#          █░█ █▀█ ▀█▀ █▀▄ █▀█ █ █▀▀ █▄█
#          █▀█ █▄█ ░█░ █▄▀ █▀▄ █ █▀░ ░█░
#          🔒 Licensed under the GNU AGPLv3.
#                    @HotDrify

from pyrogram import Client, types
from .. import (
    loader, utils)

import io
import os
import inspect

@loader.module(name="module-link", author="HotDrify")
class ModuleLinkMod(loader.Module):
    """отправляет ссылку на модуль, либо файл модуля."""
    async def ml_cmd(self, app: Client, message: types.Message, args: str):
        if not args:
          return await utils.answer(
            message, "🚫 не указан модуль.")
        msg = await utils.answer(
          message, "⏳ ищем...")

        if not (module := self.all_modules.get_module(args, True)):
            return await utils.answer(
              message, f"🚫 не найден модуль под именем {args}.")
        get_module = inspect.getmodule(module)
        origin = get_module.__spec__.origin
        try:
            source = get_module.__loader__.data
        except AttributeError:
            source = inspect.getsource(get_module).encode("utf-8")
        source_code = io.BytesIO(source)
        source_code.name = module.name + ".py"
        source_code.seek(0)
        text = (
          f"🔗 {origin}\n"
          if origin != "<string>" and not os.path.exists(origin)
          else f"📄 файл модуля {module_name}"
        )
        await msg[-1].delete()
        await utils.answer(
          message, source_code, doc=True, caption=text)
