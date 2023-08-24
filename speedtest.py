#          █░█ █▀█ ▀█▀ █▀▄ █▀█ █ █▀▀ █▄█
#          █▀█ █▄█ ░█░ █▄▀ █▀▄ █ █▀░ ░█░
#          🔒 Licensed under the GNU AGPLv3.
#                    @HotDrify
# required: speedtest-cli
import speedtest
from pyrogram import Client, types
from .. import (
    loader, utils, validators)
from ..types import Config, ConfigValue


def speed_test():
    tester = speedtest.Speedtest()
    tester.get_best_server()
    tester.download()
    tester.upload()
    return tester.results.dict()


@loader.module(name="speed test", author="teagram")
class SpeedTestMod(loader.Module):
    """Тест интернета"""
    def __init__(self):
        self.config = Config(
            ConfigValue(
                'text',
                '📥скачивание: {download}MiB\n📤загрузка: {upload}MiB\n🏓задержка: {ping}MS',
                '📥скачивание: {download}MiB\n📤загрузка: {upload}MiB\n🏓задержка: {ping}MS',
                validators.String()
            )
        )

    async def speedtest_cmd(self, app: Client, message: types.Message):
        """Запускает тест скорости. Использование: speedtest"""
        await utils.answer(
            message, "<b>Запускаем тест...</b>")
 
        result = speed_test()
        await utils.answer(
            message, self.config["text"].format(download=round(result['download'] / 2 ** 20 / 8, 2), upload=round(result['upload'] / 2 ** 20 / 8, 2), ping=round(result['ping'], 2)))