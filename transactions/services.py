import requests


# i am thinking that before any requests are made a token needs to be generated
# for the payment process to proceed
class PeoplesPayService:
    BASE_URL = "https://peoplespay.com.gh/peoplepay/hub"

    @staticmethod
    def get_token(merchant_id, api_key):
        url = f"{PeoplesPayService.BASE_URL}/token/get"
        payload = {
            "merchant_id": merchant_id,
            "api_key": api_key,
            "operation": "CREDIT",
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def disburse_money(token, amount, account_name, account_number, account_issuer, external_transaction_id, description):
        URL = f"{PeoplesPayService.BASE_URL}/disburse"
        payload = {
            "amount": str(amount),
            "account_number": account_number,
            "account_name": account_name,
            "account_issuer": account_issuer,
            "external_transaction_id": external_transaction_id,
            "description": description
        }
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        reponse = requests.post(URL, json=payload, headers=headers)
        return reponse.json()

    @staticmethod
    def disburse_money(
        token,
        amount,
        account_name,
        account_number,
        account_issuer,
        callback_url,
    ):
        URL = f"{PeoplesPayService.BASE_URL}/collectmoney"
        payload = {
            "amount": str(amount),
            "account_number": account_number,
            "account_name": account_name,
            "account_issuer": account_issuer,
            "callback_url": callback_url,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        reponse = requests.post(URL, json=payload, headers=headers)
        return reponse.json()
