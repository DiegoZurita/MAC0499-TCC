'''
    Como usar: 
    python generate_csv.py caminho_para_logs_bons caminho_para_logs_contaminados destino

    caminho_para_logs_bons: caminho completo para o arquivo do logs no formato apache de requisições sem ataques.
    caminho_para_logs_contaminados: caminho completo para o arquivo do logs no formato apache de requisições com ataque ataques.
    destino: caminho com o nome do arquivo de destino
'''
import os
import re
import pandas as pd
import sys


def main():
    lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/[1-2]\.[0-9]")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)
    logs_dir = os.getcwd()
    real_log_file_name = sys.argv[1]
    sql_injection_log_fille_name = sys.argv[2]

    print("Gerando dataframe..")

    real_log_file = open(real_log_file_name)
    sql_injection_log_file = open(sql_injection_log_fille_name)

    logs_data = []

    for l in real_log_file.readlines():
        data = re.search(lineformat, l)

        if data is None:
            print("Falha ao fazer o parse da linha {} do arquivo {}. Pulando..".format(l, real_log_file_name))
            continue

        datadict = data.groupdict()
        datadict["malicious"] = 0
        logs_data.append(datadict)


    for l in sql_injection_log_file.readlines():
        data = re.search(lineformat, l)

        if data is None:
            print("Falha ao fazer o parse da linha {} do arquivo {}. Pulando..".format(l, sql_injection_log_fille_name))
            continue

        datadict = data.groupdict()
        datadict["malicious"] = 1
        logs_data.append(datadict)


    real_log_file.close()
    sql_injection_log_file.close()
    df = pd.DataFrame(logs_data)
    print("Salvando dataframe..")
    df.to_csv(sys.argv[3], index=False)
    print("Dataframe salvo")
    print(df.head())


if __name__ == "__main__":
    main()