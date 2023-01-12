from abc import ABC, abstractmethod
from typing import Any

from telebot import TeleBot


class ChannelPostHandler(ABC):
    channel_id: str
    update: Any

    @abstractmethod
    def handle_update(self):
        """This Method handles the provided update before sending"""

    @abstractmethod
    def send_update(self, bot: TeleBot, parse_mode: str = None) -> None:
        """This Method sends the update to the channel"""
