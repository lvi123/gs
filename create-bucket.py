#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin

import common

# Instantiate a BucketStorageUri object.
uri = boto.storage_uri(common.bucket, common.GOOGLE_STORAGE)
# Try to create the bucket.
try:
    uri.create_bucket(headers=common.header_values)
    print 'Successfully created bucket "%s"' % common.bucket
except boto.exception.StorageCreateError, e:
    print 'Failed to create bucket:', e
