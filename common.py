#!/usr/bin/python

# URI scheme for Google Cloud Storage.
GOOGLE_STORAGE = 'gs'
# URI scheme for accessing local files.
LOCAL_FILE = 'file'

# Your project ID can be found at https://console.developers.google.com/
# If there is no domain for your project, then project_id = 'YOUR_PROJECT'
project_id = 'ethereal-casing-87219'
header_values = {"x-goog-project-id": project_id}

bucket_guid = 'bc47a9d2-16fe-4b13-b09b-34bfc8827e96'
bucket = 'bucket-%s' % bucket_guid
file = 'bucket-file.txt'
bucket_file = '%s/%s' % (bucket, file)



