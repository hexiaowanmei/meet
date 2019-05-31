import logging
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration

vcr_host = "vcr.bj.baidubce.com"
access_key_id = "AK"
secret_access_key = "SK"


logger = logging.getLogger('baidubce.http.bce_http_client')
fh = logging.FileHandler("sample.log")
fh.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = 'vcr.bj.baidubce.com')