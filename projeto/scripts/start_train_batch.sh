source activate base

for i in `seq 1 20`; do
  echo "Runnig train $i..."

  time python train_spark.py 2> results/output-$i.log
done