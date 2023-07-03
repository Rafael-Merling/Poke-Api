from minio import Minio
from io import BytesIO


class Loader:
    def __init__(self, endpoint, access_key, secret_key) -> None:
        print("Starting loader\n")

        self.minioClient = Minio(
            endpoint, access_key=access_key, secret_key=secret_key, secure=False
        )

    def load_df(self, df, folder_name, file_name):
        print("Starting Load process to MinIO\n")

        # minioClient = Minio('127.0.0.1:9000',
        #                     access_key='minioadmin', secret_key='minioadmin', secure=False)

        csv_buffer = BytesIO(df)

        self.minioClient.put_object(
            "poke-api",
            object_name=f"{folder_name}/{file_name}.csv",
            data=csv_buffer,
            length=len(df),
            content_type="application/csv",
        )

        print(f"Inserted on MinIO csv {file_name}\n")

        print("Loading sucessful, returning to Handler\n")
