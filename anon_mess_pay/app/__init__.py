from aiogram import Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message

import app.user_handlers as user_handlers
import app.admin_handlers as admin_handlers
from data.config import admin_id


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in admin_id:
            return True
        else:
            return False


def register_all_routers(dp: Dispatcher):
    user_handlers.router.message.filter(F.chat.type == "private")
    admin_handlers.router.message.filter(F.chat.type == "private", IsAdmin())
    dp.include_router(user_handlers.router)  # Юзер роутер
    dp.include_router(admin_handlers.router)  # Админ роутер
