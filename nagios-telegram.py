#!/usr/bin/env python3

import asyncio
import asyncclick as click

import telegram

from emoji import emojize

@click.command()
@click.option('--notification_type', help='Notification Type', required=True)
@click.option('--service_desc', help='Service Description', required=True)
@click.option('--hostname', help='Host Name', required=True)
@click.option('--state', help='Host State', required=True)
@click.option('--address', help='Host Address', required=True)
@click.option('--moreinfo', help='Host Output', required=True)
@click.option('--datetime', help='Date and Time', required=True)
@click.option('--chat_id', help='Telegram Chat ID', required=True)
@click.option('--token', help='Telegram Bot Token', required=True)

async def main(notification_type=None, service_desc=None, hostname=None, state=None, address=None, moreinfo=None, datetime=None, chat_id=None, token=None):
    bot = telegram.Bot(token=token)

    if notification_type == 'ACKNOWLEDGEMENT':
        emoji_emojize = ':check_mark:'
    elif notification_type == 'CUSTOM':
        emoji_emojize = ':information_source:'
    elif notification_type == 'DOWNTIMEEND':
        emoji_emojize = ':play_button:'
    elif notification_type == 'DOWNTIMEREMOVED':
        emoji_emojize = ':eject_button:'
    elif notification_type == 'DOWNTIMESTART':
        emoji_emojize = ':stop_button:'
    elif notification_type == 'FLAPPINGEND':
        emoji_emojize = ':shuffle_tracks_button:'
    elif notification_type == 'FLAPPINGSTART':
        emoji_emojize = ':shuffle_tracks_button:'
    elif notification_type == 'PROBLEM':
        if state is not None:
            if state == 'CRITICAL':
                emoji_emojize = ':broken_heart:'
            elif state == 'WARNING':
                emoji_emojize = ':yellow_heart:'
            else:
                emoji_emojize = ':purple_heart:'
        else:
            emoji_emojize = ':broken_heart:'
    elif notification_type == 'RECOVERY':
        emoji_emojize = ':green_heart:'
    else:
        emoji_emojize = ':information:'
    
    emoji_emojized = emojize(emoji_emojize + ' ')

    message = '''{} -- {}

Host: **{}**
Service: {}
State: {}
Address: {}
Time: {}
Info:
{}

    '''.format(emoji_emojize, notification_type, hostname, service_desc, state, address, datetime, moreinfo)
    message = emojize(message)
    await bot.send_message(chat_id, message, parse_mode=telegram.constants.ParseMode.MARKDOWN)
    
if __name__ == '__main__':
    asyncio.run(main())


