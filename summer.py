from pyrogram import Client, types
from .. import loader, utils
from datetime import datetime

@loader.module(name="summer", author="HotDrify")
class SummerMod(loader.Module):
    """через сколько лето?"""
    async def sum_cmd(self, app: Client, message: types.Message):
        """таймер лета"""
        await utils.answer(
            message, "<b>⌛ считаем...</b>")
        now = datetime.now()
        summer = datetime(now.year, 6, 1)
        if now.month > 6 or (now.month == 6 and now.day > 1):
            summer = datetime(now.year + 1, 6, 1)
        stime = abs(summer - now)
        text = (
            "🤔 до лета <b>осталось</b>\n",
            f"Дней: <code>{stime.days}</code>\n",
            f"Часов: <code>{stime.seconds // 3600}</code>\n",
            f"Минут: <code>{stime.seconds // 60 % 60}</code>\n",
            f"Секунд: <code>{stime.seconds % 60}</code>\n"
        )
        await utils.answer(
            message, text)