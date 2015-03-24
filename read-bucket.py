#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin
import time

import common

uri = boto.storage_uri(common.bucket_file, common.GOOGLE_STORAGE)

while 1:
  try:
    now = time.time()
    contents = uri.get_key().get_contents_as_string()
    skew = now - float(contents)
    print now, contents, skew
  except boto.exception.GSResponseError, e:
    print 'Failed to read bucket:', e.status



