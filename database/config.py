import json
import os

from google.cloud import secretmanager

secrets = secretmanager.SecretManagerServiceClient()


class Config:
    POSTGRES_SECRETS = json.loads(
        secrets.access_secret_version(
            request={
                "name": "projects/439044485118/secrets/postgres_secrets/versions/3"
            }
        ).payload.data.decode("utf-8")
    )
    POSTGRES_DB = "postgres"
    SQLALCHEMY_DATABASE_BASE = (
        f"postgresql+psycopg2://{POSTGRES_SECRETS['user']}:"
        f"{POSTGRES_SECRETS['password']}"
    )
    INSTANCE_CONNECTION = "impactful-ring-314819:europe-west1:clothing-rater-postgres"
    SQLALCHEMY_DATABASE_URI = f"{SQLALCHEMY_DATABASE_BASE}@/{POSTGRES_DB}?host=/cloudsql/{INSTANCE_CONNECTION}"
