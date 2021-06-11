'''
    Funções uteis que serão usadas pelo TCC.
'''

import pandas as pd
import re
from urllib.parse import urlparse, parse_qs

def quantidade_de_params_na_query(url):
  parse = urlparse(url)
  query_obj = parse_qs(parse.query)
  return len(query_obj)

def transformLogFileToDataframe(logFilePath, isMalicious):
    lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/[1-2]\.[0-9]")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)

    logFile = open(logFilePath)

    logs_data = []

    for l in logFile.readlines():
        data = re.search(lineformat, l)

        if data is None:
            print("Falha ao fazer o parse da linha {} do arquivo {}. Pulando..".format(l, logFile))
            continue

        datadict = data.groupdict()
        datadict["malicious"] = isMalicious
        logs_data.append(datadict)

    logFile.close()

    df = pd.DataFrame(logs_data)

    df["statuscode"] = df["statuscode"].apply(int)
    df["qtd_query_params"] = df["url"].apply(quantidade_de_params_na_query)

    return df