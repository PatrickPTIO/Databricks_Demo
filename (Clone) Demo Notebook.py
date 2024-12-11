# Databricks notebook source


# COMMAND ----------

# MAGIC %run /Workspace/Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
display(files)

# COMMAND ----------


