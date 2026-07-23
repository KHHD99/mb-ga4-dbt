from google.cloud import bigquery

schema = [

bigquery.SchemaField("event_date","STRING"),

bigquery.SchemaField("event_timestamp","INTEGER"),

bigquery.SchemaField("event_name","STRING"),

bigquery.SchemaField("user_pseudo_id","STRING"),

bigquery.SchemaField("user_id","STRING"),

bigquery.SchemaField("platform","STRING"),

bigquery.SchemaField("stream_id","STRING"),

bigquery.SchemaField(
    "traffic_source",
    "RECORD",
    fields=[
        bigquery.SchemaField("name","STRING"),
        bigquery.SchemaField("medium","STRING"),
        bigquery.SchemaField("source","STRING")
    ]
),

bigquery.SchemaField(
    "geo",
    "RECORD",
    fields=[
        bigquery.SchemaField("country","STRING"),
        bigquery.SchemaField("city","STRING"),
        bigquery.SchemaField("region","STRING")
    ]
),

bigquery.SchemaField(
    "device",
    "RECORD",
    fields=[
        bigquery.SchemaField("category","STRING"),
        bigquery.SchemaField("browser","STRING"),
        bigquery.SchemaField("operating_system","STRING")
    ]
),

bigquery.SchemaField(
    "event_params",
    "RECORD",
    mode="REPEATED",
    fields=[

        bigquery.SchemaField("key","STRING"),

        bigquery.SchemaField(
            "value",
            "RECORD",
            fields=[
                bigquery.SchemaField("string_value","STRING"),
                bigquery.SchemaField("int_value","INTEGER"),
                bigquery.SchemaField("double_value","FLOAT")
            ]
        )
    ]
),

bigquery.SchemaField(
    "items",
    "RECORD",
    mode="REPEATED",
    fields=[

        bigquery.SchemaField("item_id","STRING"),
        bigquery.SchemaField("item_name","STRING"),
        bigquery.SchemaField("price","FLOAT"),
        bigquery.SchemaField("quantity","INTEGER")

    ]
)

]
