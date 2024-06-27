import uuid
import names
import random
import string
from dataclasses import dataclass


@dataclass
class BehaviorsShopify:

    @classmethod
    def __init__(self):... 
    
    @classmethod
    def Ccs(self, cards:str=None):
        if '|' in cards: return cards.split('|')
        elif ':' in cards: return cards.split(':')
        elif ',' in cards: return cards.split(',')
        elif '-' in cards: return cards.split('-')

        return cards
    
    @classmethod
    def RandomName(self,dato:str=None):
        if dato == 'username': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        elif dato == 'correo': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        elif dato == 'password': return f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        else: return 'Valores InCorrectos: username, password, correo'
    
    @classmethod
    def QueryNotice(self,data):
        try: 
            start = data.index('notice__text">') + len('notice__text">')
            end   = data.index( '<' ,start)
            return       data [start:end]
        
        except: return 'Card was declined.'
        

    @classmethod
    def Token_(self):
        self.acii = string.ascii_letters + string.digits
        self.token = ''.join(random.choice(self.acii) for i in range(86))

        return self.token

    @classmethod
    def Response(self,resultados ,reques_url:str,charged:str):
        
        if 'No Match' == resultados:                                                                                    return 'Approved ✅',resultados
        elif 'Charged' == resultados:                                                                                   return 'Approved ✅',  'Charged {}$'.format(charged)
        elif 'INVALID_CVV' == resultados:                                                                               return 'Approved ✅',resultados
        elif 'Code: "INVALID_CVV"' == resultados:                                                                       return 'Approved ✅',resultados
        elif '/3d_secure_2/' in str(reques_url):                                                                        return 'Declined! ❌','3d_secure_2',
        elif 'CVV does not match' == resultados:                                                                        return 'Approved ✅' ,resultados
        if '2010 Card Issuer Declined CVV' == resultados:                                                               return 'Approved ✅',resultados
        elif 'Transaction Normal - Insufficient Funds'== resultados:                                                    return 'Approved ✅',resultados
        elif 'Street address and postal code do not match' == resultados:                                               return 'Approved ✅',resultados
        elif 'Security code was not matched by the processor' == resultados:                                            return 'Approved ✅',resultados
        elif 'Security codes does not match correct format (3-4 digits)' == resultados:                                 return 'Approved ✅',resultados
        elif '/thank_you' in str(reques_url) or '/orders/' in str(reques_url) or '/post_purchase' in str(reques_url):   return  'Approved ✅',  'Charged {}$'.format(charged)
        
        else: return 'Declined! ❌',resultados



@dataclass
class RandomProxies:
    
    @classmethod
    def __init__(self):...

    @classmethod
    def randomP(self):

        with open("srca/proxy.txt") as a: 
            self._host = f"{random.choice(a.read().splitlines()).strip()}:http"

        self.pasrt = self._host.split(":")
        self.proxy = '{}://{}:{}@{}:'.format(   self.pasrt[-1], 
                                                self.pasrt[2], 
                                                self.pasrt[3],
                                                self.pasrt[0],
                                                self.pasrt[1])
        
        self.dicPo = {"http://": self.proxy, "https://": self.proxy}
        return self.dicPo



def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  


def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session

