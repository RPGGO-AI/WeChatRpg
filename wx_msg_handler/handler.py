from wxhook import Bot
from wxhook.model import Event

from config import constans
from wx_event.event_enum import EventType


def handle_text_message(wx_bot: Bot, event: Event):
    wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, f"Text: {event.content}")
    print("Text message processed.")


def handle_image_message(wx_bot: Bot, event: Event):
    wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, "Image received!")
    print("Image message processed.")


def handle_voice_message(wx_bot: Bot, event: Event):
    wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, "Voice message received!")
    print("Voice message processed.")


event_handlers = {
    EventType.TEXT_MESSAGE: handle_text_message,
    EventType.IMAGE_MESSAGE: handle_image_message,
    EventType.VOICE_MESSAGE: handle_voice_message,
}
