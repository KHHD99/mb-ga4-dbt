from google.cloud import bigquery
from schema import schema

client = bigquery.Client()

table = "khhd-473723.ga4_export.events_20260722"

job = client.load_table_from_json(
    rows,
    table,
    job_config=bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_TRUNCATE"
    )
)

job.result()

print("Done")
