from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def commd(user_id):
    commd = InlineKeyboardMarkup([[
                                InlineKeyboardButton(text='𝙋𝙚𝙧𝙛𝙞𝙡',callback_data=f'perfil:{user_id}'),
                                InlineKeyboardButton(text='𝙂𝙖𝙩𝙚𝙒𝙖𝙮𝙨',callback_data=f'gates:{user_id}'),],[
                                InlineKeyboardButton(text='𝙃𝙚𝙧𝙧𝙖𝙢𝙞𝙚𝙣𝙩𝙖𝙨',callback_data=f'tools:{user_id}')]])
    return commd


def atras(user_id):
    atras = InlineKeyboardMarkup([[InlineKeyboardButton(text='𝘼𝙩𝙧𝙖𝙨',callback_data=f'atras:{user_id}')]])
    return atras

perfil_text = '''Perfil user

𝐈𝐝: {}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{}
𝐍𝐚𝐦𝐞: {}
𝐂𝐫𝐞𝐝𝐢𝐭𝐨𝐬: {}
𝐑𝐚𝐧𝐠𝐨: {}
𝐏𝐥𝐚𝐧: {}
𝐀𝐧𝐭𝐢𝐬𝐩𝐚𝐦: {}
𝐅𝐞𝐜𝐡𝐚: {}

'''