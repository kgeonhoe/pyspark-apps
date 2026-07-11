import time

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName('homework_pyspark') \
    .getOrCreate()

schema = 'country STRING, hit LONG'
df = spark.createDataFrame(data=[('Korea', 120), ('USA', 80), ('Japan', 40)], schema=schema)
df.show()

# sleep 5 minute
time.sleep(600)
