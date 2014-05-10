import os

from flask_frozen import Freezer

from sitebuilder import app
import shutil
import subprocess
from pprint import pformat


def freeze():
    if os.path.exists(os.path.join(os.getcwd(), 'build')):
        shutil.rmtree('build')
    Freezer(app).freeze()

def set_aws_credentials():
    import ConfigParser
    Config = ConfigParser.ConfigParser()
    Config.read("aws.config")
    os.environ['AWS_ACCESS_KEY_ID'] = Config.get(section='aws', option='AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY'] = Config.get(section='aws', option='AWS_SECRET_ACCESS_KEY')
    
def upload_to_server():
    cmd_line = "aws s3 sync %s s3://%s"%('build', 'blancnote.com')
    print cmd_line.split(' ')
    process = subprocess.Popen(cmd_line.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if stderr:
        raise "error"
    print 'output of s3 sync'
    print pformat(stdout.split('\r\n'))

def create_sitemap():
    process = subprocess.Popen(['python', 'gensitemap.py'], stdout=subprocess.PIPE)
    out, _ = process.communicate()
    with open('static/sitemap.xml', 'w') as f:
        f.write(out)

def execute():
#     create_sitemap()
    freeze()
    set_aws_credentials()
    upload_to_server()

if __name__ == '__main__':
    execute()