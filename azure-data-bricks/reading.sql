storage_account_name = "esgpredective"
container_name = "bronze"
sas_token = "sp=racwdlmeop&st=2025-09-28T09:37:52Z&se=2025-09-28T17:52:52Z&sv=2024-11-04&sr=c&sig=ndMr3byYwmmDTcoAxjOxQXxuueLi2wUPUGfJLR%2F7ZPI%3D"

spark.conf.set(
    f"fs.azure.sas.{container_name}.{storage_account_name}.blob.core.windows.net",
    sas_token
)

wasbs_path = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/"

# Replace "your_file.csv" with your actual file name
df = spark.read.format("csv").option("header", "true").load(wasbs_path + "your_file.csv")





# Show first 20 rows in proper column format


df.show(truncate=False)

# Or display as a Databricks table (clickable GUI table)
display(df)
