from google.cloud import storage
from google.auth import default

# Initialize the Google Cloud Storage client
credentials, project = default()
client = storage.Client(credentials=credentials, project=project)

# List all buckets
buckets = list(client.list_buckets())

# Convert bucket information to JSON format, including soft delete policy
bucket_info = [
    {
        "name": bucket.name,
        "location": bucket.location,
        "storageClass": bucket.storage_class,
        "timeCreated": bucket.time_created.isoformat() if bucket.time_created else None,
        "updated": bucket.updated.isoformat() if bucket.updated else None,
        "softDeletePolicy": bucket.soft_delete_policy,
        "lifeCycleRules": [i for i in bucket.lifecycle_rules]
    }
    for bucket in buckets
]

import json
print(json.dumps(bucket_info, indent=2))