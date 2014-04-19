import os, boto, mimetypes, gzip
from io import StringIO, BytesIO
from jsmin import JavascriptMinify
from cssmin import *
 
# The list of content types to gzip, add more if needed
COMPRESSIBLE = [ 'text/plain', 'text/csv', 'application/xml',
                'application/javascript', 'text/css' ]
 
def s3_uploader(src_folder_name, bucket_name):
    src_folder = os.path.normpath(src_folder_name)
 
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)
 
    namelist = []
    for root, dirs, files in os.walk(src_folder):
        if files and not '.svn' in root:
            path = os.path.relpath(root, src_folder)
            namelist += [os.path.normpath(os.path.join(path, f)) for f in files]
 
    print 'Uploading %d files to bucket %s' % (len(namelist), bucket.name)
    for name in namelist:
        key_name = name.replace('\\', '/')
#         print name, key_name
#         continue
        content = open(os.path.join(src_folder, name))
        key = bucket.new_key(key_name)
        type, _ = mimetypes.guess_type(name)
        type = type or 'application/octet-stream'
        headers = { 'Content-Type': type, 'x-amz-acl': 'public-read' }
        states = [type]
 
        # We only use HTTP 1.1 headers because they are relative to the time of download
        # instead of being hardcoded.
        headers['Cache-Control'] = 'max-age %d' % (3600 * 24 * 365)
 
        if type == 'application/javascript':
            outs = StringIO()
            JavascriptMinify().minify(content, outs)
            content.close()
            content = outs.getvalue()
            if len(content) > 0 and content[0] == '\n':
                content = content[1:]
            content = BytesIO(content)
            states.append('minified')
 
        if type == 'text/css':
            outs = cssmin(content.read())
            content.close()
            content = outs
            if len(content) > 0 and content[0] == '\n':
                content = content[1:]
            content = BytesIO(content)
            states.append('minified')
 
        if type in COMPRESSIBLE:
            headers['Content-Encoding'] = 'gzip'
            compressed = StringIO()
            gz = gzip.GzipFile(filename=name, fileobj=compressed, mode='w')
            gz.writelines(content)
            gz.close()
            content.close
            content = BytesIO(compressed.getvalue())
            states.append('gzipped')
 
        states = ', '.join(states)
        print '- %s > %s (%s)' % (name, key.name, states)
        key.set_contents_from_file(content, headers)
        content.close();
 
