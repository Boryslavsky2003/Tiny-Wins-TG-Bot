from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import ChannelsState
from bot.utils.access import admin_only

router = Router()