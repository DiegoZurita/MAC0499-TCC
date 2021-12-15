from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("tcc").getOrCreate()

yColumns = ["statuscode", "navegadorCat", "qtd_query_params", "bytessent"]
xColumn = "malicious"

df = spark.read.csv(
    "/Users/diegozurita/Desktop/repos/facul/MAC0499-TCC/projeto/dados/processado/v4/dados_reais.csv", 
    header=True,
    inferSchema=True
)

df = df.withColumn("malicious", df[xColumn].cast("double"))

encoder = StringIndexer(inputCol="navegador", outputCol="navegadorCat")
endcodeDf = encoder.fit(df).transform(df)


va = VectorAssembler(inputCols = yColumns, outputCol='features')
vectorizedDf = va.transform(endcodeDf)


finalDf = vectorizedDf.select("features", xColumn)

# finalDf.show(50)

(trainingData, testData) = finalDf.randomSplit([0.7, 0.3])

dt = DecisionTreeClassifier(featuresCol="features", labelCol="malicious")
dtFitted = dt.fit(trainingData)

predictions = dtFitted.transform(testData)

# predictions.show()

evaluator = MulticlassClassificationEvaluator(
    labelCol="malicious", 
    predictionCol="prediction", 
    metricName="accuracy"
)

acc = evaluator.evaluate(predictions)

print("accuracy:", acc)