# Example: filter rows where column 'status' = 'active'
df_filtered = df.filter(df.status == "active")

# Example: add a new column
from pyspark.sql.functions import col, upper
df_transformed = df_filtered.withColumn("NAME_UPPER", upper(col("name")))

df_transformed.show(5)


#WRITING THE TANFREMDD DDATA INTO

df_transformed.write.mode("overwrite").parquet("/mnt/bronze/transformed_data/")
