
from srca.configs import addCommand,Client
from db.mongo_client import MongoDB



@addCommand('panel')
def bin(_,m):

    if MongoDB().admin(int(m.from_user.id)) == False: return ...

    m.reply('acceso totalmente al bot... pedir permiso antes de ejecutar cualquier comano administrador..... de no hacerlo motivo de ban')
    