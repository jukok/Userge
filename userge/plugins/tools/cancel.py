# Copyright (C) 2020 by UsergeTeam@Telegram, < https://t.me/theUserge >.
#
# This file is part of < https://github.com/uaudith/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.


from userge import userge, Message


@userge.on_cmd("cancel", about="\
__Reply this to message you want to cancel__")
async def cancel_(message: Message):
    replied = message.reply_to_message

    if replied:
        replied.cancel_the_process()
        await message.edit("`added your request to the cancel list`", del_in=5)

    else:
        await message.edit("`reply to the message you want to cancel`", del_in=5)