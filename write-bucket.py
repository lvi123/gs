#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin
import time
import string
import random

import common

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

uri = boto.storage_uri(common.bucket_file, common.GOOGLE_STORAGE)

while 1:
  now = time.time()
  random_string = random_string_generator(64*1024)
  data = '%f %s' % (now, random_string)
  uri.get_key().set_contents_from_string(data)
  print now



