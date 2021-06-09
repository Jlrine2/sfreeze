import pickle
from uuid import uuid4
from base64 import decodebytes, encodebytes

import boto3

S3_CLIENT = boto3.client('s3')


def s3_freeze(obj, bucket, key=None, **kwargs):
    binary = pickle.dumps(obj)
    if not key:
        key = 'sfreeze' + str(uuid4())
    S3_CLIENT.put_object(Bucket=bucket, Key=key, Body=binary, **kwargs)
    obj_id = encode(f'{bucket}:{key}')
    return obj_id


def s3_thaw(obj_id, **kwargs):
    bucket, key = decode(obj_id).split(':')
    response = S3_CLIENT.get_object(Bucket=bucket, Key=key, **kwargs)
    binary = response['Body'].read()
    return pickle.loads(binary)


def encode(string):
    return encodebytes(string.encode()).decode()


def decode(string):
    return decodebytes((string.encode())).decode()
