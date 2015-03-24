#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin

import common

uri = boto.storage_uri('', common.GOOGLE_STORAGE)
for bucket in uri.get_all_buckets(headers=common.header_values):
  print bucket.name
