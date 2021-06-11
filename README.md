# Classificação de requisições HTTP maliciosas por meio de aprendizagem de máquina

Descrição do projeto: https://www.linux.ime.usp.br/~diegozurita/mac0499/

## Pastas

    .
    ├── site                      # Site da matéria. Feito em distill do R.
    ├── projeto         
    │  ├── dados       
    |  |   ├── raw/vi            # Aquivos de logs na forma bruta da versão i.
    │  |   └── processados/vi    # Arquivos csv dos logs na versão i.
    │  ├── notebooks             # Jupyter notebooks usados no trabalho.*
    │  └── scripts               # Scripts que vou criando para ajudar no trabalho. 
    ├── environment.yml          # Arquivo yml de um ambiente conda.
    └── README.md

    * Pasta descontinuada, vou criar os notebooks usando Google Colab e linkando eles aqui. Está ai apenas para efeitos de histórico.


## Notebooks 

Por hora, o acesso está restrio, mas ao final do projeto eu pretendo liberar.

### - Análise preliminar do logs v2

https://colab.research.google.com/drive/1vZuXMwDzy8OG-4BGAY61AWEPSVEFDXbu?usp=sharing

Uma análise breve dos logs que estão em v2 para ver se foram gerados de acordo com a expectativa, como também para ver se serão úteis para a criação dos modelos.

### - Modelos 

https://colab.research.google.com/drive/1LRwe-BydM45DsMw29IZBXmVbAboCRal6?usp=sharing

O primeiro modelo foi criado. É uma ávore de decisão que, apesar de simples, consegue classificar todas as requisições ao DVWA como maliciosas e não maliciosas corretamente.
