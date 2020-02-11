from google.cloud import storage
from datetime import datetime
# from google.cloud import bigquery
import pandas as pd
import os
import re

cred_json = "./tactile-wave-267212-cb3a280a483d.json"
CREDENTIAL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), cred_json)
# gcp credentailファイルの読み込み
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_PATH
# ipaexg = "./auth/ipaexg.ttf"
# ipaexg_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), ipaexg)

class UpDownLoad:
    # BQクライアント初期化
    # bq_client = bigquery.Client()

    # ファイルタイプ一覧の辞書
    content_dict = {
        "csv": "text/csv",
        "txt": "text/plain",
        "jpeg|jpg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "zip": "application/zip"
    }

    def data2gcs(self, data, bucket_name, folder_name, file_name):
        try:
            # GCSクライアント初期化
            client = storage.Client()

            # バケットオブジェクト取得
            bucket = client.get_bucket(bucket_name)

            # 保存先フォルダとファイル名作成
            blob = bucket.blob(os.path.join(folder_name, file_name))

            # コンテントタイプ判定
            for k, v in self.content_dict.items():
                if re.search(rf"\.{k}$", file_name):
                    content_type = v
            # 保存
            if content_type == 'text/csv':
                blob.upload_from_string(data=data.to_csv(sep=",", index=False), content_type=content_type)
            else:
                print("t")
                blob.upload_from_string(data=data, content_type=content_type)
            return "success"
        except Exception as e:
            return str(e)

    # def make_bq(self, df, table_name):
    #     try:
    #         # _TABLE_SUFFIX作成のためのdate
    #         date = datetime.today().strftime("%Y%m%d")
    #         dataset, new_table = table_name.split(".")
    #         dataset_ref = self.bq_client.dataset(dataset)
    #         table_ref = dataset_ref.table(f'{new_table}_{date}')
    #         self.bq_client.load_table_from_dataframe(df.astype("str"), table_ref).result()
    #         return "success"
    #     except Exception as e:
    #         return str(e)
    #
    # def read_bq(self, query):
    #     return self.bq_client.query(query).to_dataframe()



# 折りたたむ

# BigQueryへデータをアップロード
# load = UpDownLoad()
# table_name = "mytweets.tweets1"
# data = pd.DataFrame()
# res_bq = load.make_bq(data, table_name)
# print(res_bq)