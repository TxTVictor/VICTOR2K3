from pyrogram import Client, filters
from paquetes.plantillas import commd

@Client.on_callback_query(filters.regex("atras"))
def atras(client, message):
    message.edit_message_text('<i><b>Lista de comandos</b>.</i>',reply_markup=commd(message.from_user.id))