
from srca.configs import find_cards,antispam
from gates.wyze import wyze
import time 
from db.mongo_client import MongoDB
from srca.configs import addCommand


@addCommand('se')
def mc(client, m):
    if MongoDB().query_group(m.chat.id) == None: return m.reply('Chat not Authorized.')
    querY = MongoDB().query_user(int(m.from_user.id))
    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    if  querY['role'] == 'baneado': return m.reply('User baneado')
    if  querY['plan'] == 'free': return m.reply('User Fre , adquiera un plan https://t.me/VICTOR2K3')
    inicio = time.time()
    if antispam(querY['antispam'],m):return
    
    
    if m.reply_to_message:ccs = find_cards(m.reply_to_message.text)
    else: ccs = find_cards(m.text)
    cc_com = '{}|{}|{}|{}'.format(ccs[0], ccs[1], ccs[2], ccs[3])
    
    if ccs == '<b>ingrese la ccs.</b>': return m.reply(ccs)

    new = m.reply(f'''<b>あ Shopify

• Cc: <code>{cc_com}</code>      
• Status: Processing... [ ☃️ ]
• From: {m.from_user.first_name}</b>''')
    
    chk = wyze(ccs[0], ccs[1], ccs[2],ccs[3])


    fin = time.time()
    texto = f'''<b>あ Shopify

• Cc: <code>{cc_com}</code>
• Status: {chk[1]}
• Response: <code>{chk[0]}</code>

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: {m.from_user.first_name}</b>'''
    new.edit_text(texto) 