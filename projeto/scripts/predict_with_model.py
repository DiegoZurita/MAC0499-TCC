'''
    Como usar: 
    python predict_with_model.py model_dump_file log_file is_malicious
'''

import sys
from joblib import load
import sklearn
from sklearn.metrics import accuracy_score, confusion_matrix
from tcc_utils import transformLogFileToDataframe



def main():
    model_dump = sys.argv[1]
    log_path = sys.argv[2]
    is_malicious = int(sys.argv[3])

    print("- Transformando logs em DataFrame..")

    df = transformLogFileToDataframe(log_path, is_malicious)
    X_columns = ["statuscode", "qtd_query_params", "bytessent"]
    y_columns = ["malicious"]

    X = df.loc[:, X_columns]
    y = df.loc[:, y_columns]

    print()
    print("- Head do X:")
    print(X.head())

    print()
    print("- Sklearn version:", sklearn.__version__)

    print()
    print("- Carregando modelo..")
    model = load(model_dump)

    print()
    print("- Realizando previsão..")

    yhat = model.predict(X)

    print()
    print("- Acurácia encontrada pelo modelo:", accuracy_score(y, yhat))
    print("- Matriz de confusão:")
    print(confusion_matrix(y, yhat))



if __name__ == "__main__":
    main()