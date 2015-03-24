#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin
import time

import common

uri = boto.storage_uri(common.bucket_file, common.GOOGLE_STORAGE)

while 1:
  now = time.time()
  uri.get_key().set_contents_from_string(now)
  print now



