from sqlalchemy import create_engine, MetaData

URL="mysql+pymysql://c03qnu6khsbecn0hzptd:pscale_pw_2R9xqHJ7zsyuRvsTdhjkgcnrvQL6DeW3qQ6iDpS0JWA@aws.connect.psdb.cloud/pi_2023"
ca_path=".\config\cacert-2023-01-10.pem"

engine= create_engine(URL,connect_args={'ssl_ca':ca_path})

conn=engine.connect()

meta_data=MetaData()