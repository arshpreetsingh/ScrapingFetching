import json
import hmac
import hashlib
import time
import requests
import base64


class BitfinexError(Exception):
    pass


class BaseClient(object):
    
    #api_url = 'https://bf1.apiary-mock.com/'
    api_url = 'https://api.bitfinex.com/'
    exception_on_error = True

    def __init__(self, proxydict=None, *args, **kwargs):
        self.proxydict = proxydict

    def _get(self, *args, **kwargs):
        """
        Make a GET request.
        """
        return self._request(requests.get, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """
        Make a POST request.
        """
        data = self._default_data()
        data.update(kwargs.get('data') or {})
        kwargs['data'] = data
        return self._request(requests.post, *args, **kwargs)

    def _default_data(self):
        """
        Default data for a POST request.
        """
        return {}

    def _request(self, func, url, *args, **kwargs):
        return_json = kwargs.pop('return_json', False)
        url = self.api_url + url
        response = func(url, *args, **kwargs)

        if 'proxies' not in kwargs:
            kwargs['proxies'] = self.proxydict
        response.raise_for_status()

        try:
            json_response = response.json()
        except ValueError:
            json_response = None
        if isinstance(json_response, dict):
            error = json_response.get('error')
            if error:
                raise BitfinexError(error)

        if return_json:
            if json_response is None:
                raise BitfinexError(
                    "Could not decode json for: " + response.text)
            return json_response

        return response


class Public(BaseClient):

    def ticker(self):
        return self._get("v1/pubticker/btcusd", return_json=True)
    
    def get_last(self):
        """shortcut for last trade"""
        return float(self.ticker()['last_price'])
        


class Trading(Public):

    def __init__(self, key, secret, *args, **kwargs):
        super(Trading, self).__init__(
                 key=key, secret=secret, *args, **kwargs)
        self.key = key
        self.secret = secret

    def _get_nonce(self):
        
        nonce = getattr(self, '_nonce', 0)
        if nonce:
            nonce += 1
        # If the unix time is greater though, use that instead (helps low
        # concurrency multi-threaded apps always call with the largest nonce).
        self._nonce = max(int(time.time()), nonce)
        return self._nonce

    def _default_data(self, *args, **kwargs):
        """
        Generate a one-time signature and other data required to send a secure
        POST request to the Bitfinex API.
        """
        data = {}
        nonce = self._get_nonce()
        data['nonce'] = str(nonce)
        data['request'] = args[0]
        return data

    def _post(self, *args, **kwargs):
        """
        Make a POST request.
        """
        data = kwargs.pop('data', {})
        data.update(self._default_data(*args, **kwargs))
        
        key = self.key
        secret = self.secret
        payload_json = json.dumps(data)
        payload = base64.b64encode(payload_json)
        sig = hmac.new(secret, payload, hashlib.sha384)
        sig = sig.hexdigest()

        headers = {
           'X-BFX-APIKEY' : key,
           'X-BFX-PAYLOAD' : payload,
           'X-BFX-SIGNATURE' : sig
           }
        kwargs['headers'] = headers
        return self._request(requests.post, *args, **kwargs)

    def account_infos(self):
        """
        Returns dictionary::
        [{"fees":[{"pairs":"BTC","maker_fees":"0.1","taker_fees":"0.2"},
        {"pairs":"LTC","maker_fees":"0.0","taker_fees":"0.1"},
        {"pairs":"DRK","maker_fees":"0.0","taker_fees":"0.1"}]}]
        """
        return self._post("/v1/account_infos", return_json=True)
    
    def balances(self):
        """
        returns a list of balances
        A list of wallet balances:
        type (string): "trading", "deposit" or "exchange".
        currency (string): Currency 
        amount (decimal): How much balance of this currency in this wallet
        available (decimal): How much X there is in this wallet that 
        is available to trade.
        """
        return self.post("/v1/balances",return_json=False)
