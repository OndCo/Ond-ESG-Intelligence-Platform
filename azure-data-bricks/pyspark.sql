# Define storage account, container, and SAS token
storage_account = "esgdatae334"
container_name = "bronze"
sas_token = "?sp=r&st=2025-09-28T07:49:06Z&se=2025-09-28T16:04:06Z&sv=2024-11-04&sr=c&sig=Pe5UwQsOpEkHhMyYMKd7sTI0R8%2FadxQgFVjsMACXVNA%3D"

# Mount point in Databricks
mount_point = "/mnt/bronze"

# Mount the blob storage
dbutils.fs.mount(
  source = f"wasbs://{container_name}@{storage_account}.blob.core.windows.net",
  mount_point = mount_point,
  extra_configs = {f"fs.azure.sas.{container_name}.{storage_account}.blob.core.windows.net": sas_token}
)


# List files in the container

display(dbutils.fs.ls("/mnt/bronze"))



from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/mnt/bronze/your_file.csv")

df.show(5)
