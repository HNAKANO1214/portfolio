from google.api_core.exceptions import NotFound
from google.cloud import storage
from google.oauth2 import service_account
from django.conf import settings


def get_storage_client():
    credentials = service_account.Credentials.from_service_account_file(
        settings.FIREBASE_AUTH_JSON
    )
    return storage.Client(credentials=credentials)


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = get_storage_client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    try:
        blob.delete()
        print(f"Blob {blob_name} deleted.")
    except NotFound:
        print(f"Blob {blob_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
