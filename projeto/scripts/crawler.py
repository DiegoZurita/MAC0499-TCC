'''
    Como usar: 
    python crawler.py host n sessId 

    host: endereço onde esta o dvwa
    n: quantidade de requisições
    sessId: coockei PHPSESSID do dvwa (útil para não gerar somente requisições não autorizadas)
'''


import sys
from multiprocessing import Pool
from dataclasses import dataclass
import numpy as np
from typing import List
import string
import requests
from fake_useragent import UserAgent
from time import sleep


@dataclass
class RequestData:
    host: str
    url: str
    sessid: str
    userAgent: str


def execRequest(requestData: RequestData) -> bool:
    print("Requeisitando url {}{} ".format(requestData.host, requestData.url))
    headers = {
        'User-Agent': requestData.userAgent
    }
    cookies = {
        "PHPSESSID": requestData.sessid,
        "security": "low"
    }
    req = requests.get(
        "{}{}".format(requestData.host, requestData.url), 
        headers = headers,
        cookies = cookies
    )
    
    return req.status_code == 200


def genRandomString():
    qtd_extra = np.random.randint(20, 60)
    random_string_list = np.random.choice(list(string.ascii_letters), qtd_extra)
    return  "".join(random_string_list)

def createRequests(host: str, urls: List[str], n: int, sessid: str) -> List[RequestData]:
    url_index = np.random.binomial(len(urls), 0.5, n)
    shouldAddExtraPrams = np.random.choice([True, False], n)
    ua = UserAgent()

    requests = []

    for i in range(n):
        url = urls[url_index[i]]

        if shouldAddExtraPrams[i]:
            random_string = genRandomString()

            url = "{}?extraParam={}".format(url, random_string)

        
        requests.append(RequestData(host, url, sessid, ua.random))

    return requests

def main():
    urls = [
        "/instructions.php",
        "/setup.php",
        "/vulnerabilities/brute/",
        "/vulnerabilities/exec/",
        "/vulnerabilities/csrf/",
        "/vulnerabilities/upload/",
        "/vulnerabilities/captcha/",
        "/vulnerabilities/sqli/",
        "/index.php",
        "/about.php",
        "/vulnerabilities/sqli_blind/",
        "/vulnerabilities/weak_id/",
        "/vulnerabilities/xss_d/",
        "/vulnerabilities/xss_r/",
        "/vulnerabilities/xss_s/",
        "/unknown", ## papel de fazer 404
        "/vulnerabilities/csp/",
        "/vulnerabilities/javascript/",
        "/security.php"
    ]

    host = sys.argv[1]
    n_requests = int(sys.argv[2])
    sessId = sys.argv[3]
    reqs = createRequests(host, urls, n_requests, sessId)

    with Pool(8) as p:
        results = p.map(execRequest, reqs)

        print("Porcentagem de requisições 200: {}".format(np.sum(results)/n_requests))

if __name__ == "__main__":
    main()