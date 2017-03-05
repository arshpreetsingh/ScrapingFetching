import boto
import boto.s3
import sys
from boto.s3.key import Key
import os


def amazon_uploader():
	
    AWS_S3_ACCESS_KEY_ID='AKIAI7CZP7K3VZOZ7EYQ'
    AWS_S3_SECRET_ACCESS_KEY='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' 
    AWS_STORAGE_BUCKET_NAME='development-branch'
    SECRET_KEY='A long string with many different types of characters'
    bucket_name = 'development-branch'
    testfile = '/home/metal-machine/Pictures/cython.png'
    conn = boto.connect_s3(AWS_S3_ACCESS_KEY_ID,AWS_S3_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket('development-branch')
    k = Key(bucket)
    key_name = 'my test file'
    path = '/candidate-photos/'
#path = '/candidate-photos/hello' this make a directory inside candidate-photos as well. 
    full_key_name = os.path.join(path, key_name)
    k = bucket.new_key(full_key_name)
    return k.set_contents_from_filename(testfile)

