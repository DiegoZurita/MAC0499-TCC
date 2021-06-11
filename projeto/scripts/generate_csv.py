'''
    Como usar: 
    python generate_csv.py caminho_para_logs_bons caminho_para_logs_contaminados destino

    caminho_para_logs_bons: caminho completo para o arquivo do logs no formato apache de requisições sem ataques.
    caminho_para_logs_contaminados: caminho completo para o arquivo do logs no formato apache de requisições com ataque ataques.
    destino: caminho com o nome do arquivo de destino
'''
import pandas as pd
import sys
from tcc_utils import transformLogFileToDataframe


def main():
    print("Gerando dataframe..")
    real_log_file_name = sys.argv[1]
    malicious_log_file_name = sys.argv[2]

    real_df = transformLogFileToDataframe(real_log_file_name, 0)
    malicious_df = transformLogFileToDataframe(malicious_log_file_name, 1)

    df = pd.concat([real_df, malicious_df], axis=1)
    print("Salvando dataframe..")
    df.to_csv(sys.argv[3], index=False)
    print("Dataframe salvo")
    print(df.head())


if __name__ == "__main__":
    main()