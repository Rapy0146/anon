from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types


def main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="💼Профиль"),
        types.KeyboardButton(text="❓О боте")
    )
    return builder.as_markup(resize_keyboard=True)


def main_cancel_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="❌Отмена")
    )
    return builder.as_markup(resize_keyboard=True)


def profile_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔮Подписка", callback_data="subscription")
    builder.button(text="🧿Просмотры", callback_data="views")
    builder.button(text="❌Отмена", callback_data="cancel")
    builder.adjust(2, 1)
    return builder.as_markup()


def cancel_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="❌Отмена", callback_data="cancel")
    return builder.as_markup()


def guess_keyboard(username, name):
    builder = InlineKeyboardBuilder()
    builder.button(text="Узнать отправителя 🫣", callback_data=f"guess:{username}:{name}")
    return builder.as_markup()


def quest_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Да", callback_data="quest:yes")
    builder.button(text="Нет", callback_data="quest:no")
    builder.adjust(2)
    return builder.as_markup()


def ask_buy_views_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🤫Купить просмотры", callback_data="buy_views:1")
    builder.button(text="❌Отмена", callback_data="cancel")
    builder.adjust(1)
    return builder.as_markup()


def subscription_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔮1 месяц", callback_data="buy_subscription:1:месяц")
    builder.button(text="🔮3 месяца", callback_data="buy_subscription:3:месяца")
    builder.button(text="🔮12 месяцев", callback_data="buy_subscription:12:месяцев")
    builder.button(text="◀️Назад", callback_data="back_profile")
    builder.adjust(3, 1)
    return builder.as_markup()


def subscription_info_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️Назад", callback_data="back_profile")
    return builder.as_markup()


def buy_subscription_keyboard(link, p_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="📎Оплатить", url=link)
    builder.button(text="🔄Проверить оплату", callback_data=f"check_subscription_pay:{p_id}")
    builder.button(text="❌Отмена", callback_data="back_profile")
    builder.adjust(1)
    return builder.as_markup()


def buy_views_keyboard(link, p_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="📎Оплатить", url=link)
    builder.button(text="🔄Проверить оплату", callback_data=f"check_views_pay:{p_id}")
    builder.button(text="❌Отмена", callback_data="back_profile")
    builder.adjust(1)
    return builder.as_markup()


def views_keyboard():
    keyboard = InlineKeyboardBuilder()
    for i in range(1, 11):
        keyboard.button(text=str(i), callback_data=f"buy_views:{i}")
    keyboard.button(text="◀️Назад", callback_data="back_profile")
    return keyboard.adjust(5).as_markup()