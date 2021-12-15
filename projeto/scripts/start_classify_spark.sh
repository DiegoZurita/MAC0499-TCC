source activate base

for i in `seq 1 20`; do
  echo "Runnig classify-10000 $i..."

  (time python classify_spark.py /Users/diegozurita/Desktop/repos/facul/MAC0499-TCC/projeto/dados/processado/v4/dados_reais_10000.csv) 2> results/classify/output-10000-$i.log
done