import firebase_admin
from firebase_admin import credentials, storage
from django.core.files.storage import Storage

firebase_credentials: dict = {
    'apiKey': "AIzaSyD05stI5KKqqsmpqS2u_X3dN78CEQ-a9uE",
    'authDomain': "portfolio-374b7.firebaseapp.com",
    'projectId': "portfolio-374b7",
    'storageBucket': "portfolio-374b7.appspot.com",
    'messagingSenderId': "717861234923",
    'appId': "1:717861234923:web:5b9dc00981e8f5f99bf6ae"
}

# Firebase の初期化
cred = credentials.Certificate(
    '/etc/secrets/portfolio-374b7-firebase-adminsdk-lcwys-3097d4d29f.json'
)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'portfolio-374b7.appspot.com'
})


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
