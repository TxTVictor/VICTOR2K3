from srca.configs import addCommand,Client
from paquetes.plantillas import  perfil_text
from db.mongo_client import MongoDB

@addCommand('claim')
def start(_,m):
    querY = MongoDB().query_user(int(m.from_user.id))

    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    bins = m.text.split('ingrese la key🔑')
    if  querY['role'] == 'baneado': return m.reply('User baneado')
    
    if len(bins) < 2: return m.reply('ingrese la key🔑.')
    
    querYl = MongoDB().query_key(bins[1])

    try:
        if querYl['key'] == bins[1]:
            MongoDB().update_group(int(m.from_user.id), querYl['dias'])
            MongoDB().update_user(m.from_user.id,querYl['dias'])
            m.reply('User updated successfully, ya eres premium.✅')
            MongoDB().key_delete(bins[1])

    texto= f'''<b>Key reclamada✅

    Name: {m.from_user.first_name}
    id: {m.from_user.id}
    Username: @{m.from_user.username}
    -------------
    Reclamo key

    key: {querYl['key']}
    dias: {querYl['dias']}
    -------------
    </b>'''
            
            Client.send_message(_,chat_id=-1002058267689,text=texto)
            return
        
    else: m.reply('Ya puedes usarme como lo hizo tu ex😜.✅')

            except: m.reply('invalid key.❌')
