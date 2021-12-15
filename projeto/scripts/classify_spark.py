from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import sys

spark = SparkSession.builder.appName("tcc").getOrCreate()

yColumns = ["statuscode", "navegadorCat", "qtd_query_params", "bytessent"]
xColumn = "malicious"

df = spark.read.csv(
    sys.argv[1],
    header=True,
    inferSchema=True
)

df = df.withColumn("malicious", df[xColumn].cast("double"))

encoder = StringIndexer(inputCol="navegador", outputCol="navegadorCat")
endcodeDf = encoder.fit(df).transform(df)


va = VectorAssembler(inputCols = yColumns, outputCol='features')
vectorizedDf = va.transform(endcodeDf)


finalDf = vectorizedDf.select("features", xColumn)

dtFitted = DecisionTreeClassificationModel.load("decision_tree.model")

predictions = dtFitted.transform(finalDf)


evaluator = MulticlassClassificationEvaluator(
    labelCol="malicious", 
    predictionCol="prediction", 
    metricName="accuracy"
)

acc = evaluator.evaluate(predictions)

print("accuracy:", acc)