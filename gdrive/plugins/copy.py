"""copy plugins."""

from pyrogram import Client, filters
from pyrogram.types import Message 

from gdrive import LOGGER
from gdrive.config import BotCommands, Messages
from gdrive.helpers.utils import CustomFilters
from gdrive.helpers.gdrive_utils import GoogleDrive

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Clone) & CustomFilters.auth_users)
def _clone(client: Client, message: Message):
  user_id = message.from_user.id
  if len(message.command) > 1:
    link = message.command[1]
    LOGGER.info(f'Copy:{user_id}: {link}')
    sent_message = await message.reply_text(Messages.CLONING.format(link), quote=True)
    msg = GoogleDrive(user_id).clone(link)
    await sent_message.edit(msg)
  else:
    await message.reply_text(Messages.PROVIDE_GDRIVE_URL.format(BotCommands.Clone[0]))
