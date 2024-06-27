from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("tools"))
def tool_com(client, m):
    m.edit_message_text('''<b>T O O L S 
                              
bin ( /bin 123456 )
Gen ( /gen 123456 )                              
Random ( /rnd us)                    
VBV chk ( /vbv ccs)</b>''',reply_markup=atras(m.from_user.id))
