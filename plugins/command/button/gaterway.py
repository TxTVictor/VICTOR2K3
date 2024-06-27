from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>**GATERWAYS COMANDOS**
#################
- Stripe Gate ( /ah ) ✅
#################
- Shopify + Braintree ( /br ) ✅
#################
- Braintre Avs ( /sb ) ✅
#################
- Shopify Normal ( /sh ) ✅
#################
- Shopify Adyen ( /sa ) ✅
#################
- Shopify Normal ( /se ) ✅
#################
- Shopify Normal ( /st ) ✅
#################
- Shopify Cyber ( /sy ) ✅ 
- Créditos Necesarios
#################
- Paypal 0.01$ ( /pp ) ✅
#################
- Vbv Braintree ( /vbv ) ✅
#################</b>''',reply_markup=atras(message.from_user.id))
