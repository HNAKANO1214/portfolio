import firebase_admin

from firebase_admin import credentials, storage
from django.core.files.storage import Storage
from django.conf import settings

# Firebase の初期化
cred = credentials.Certificate(settings.FIREBASE_AUTH_JSON)
firebase_admin.initialize_app(cred, {'storageBucket': settings.FIREBASE_STORAGE_BUCKET})


class FirebaseStorage(Storage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bucket = storage.bucket()

    def _save(self, name, content):
        blob = self.bucket.blob(name)
        blob.upload_from_string(content.read(), content_type=content.content_type)
        return name

    def url(self, name):
        blob = self.bucket.blob(name)
        return blob.generate_signed_url(version='v4', expiration=3600, method='GET')

    def delete(self, name):
        blob = self.bucket.blob(name)
        blob.delete()

    def exists(self, name):
        blob = self.bucket.blob(name)
        return blob.exists()
