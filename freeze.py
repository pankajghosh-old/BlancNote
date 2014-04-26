import os

from flask_frozen import Freezer

from sitebuilder import app
from s3_uploader import s3_uploader
import shutil


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
    s3_uploader(src_folder_name='build', bucket_name='blancnote.com')

def create_sitemap():
    import subprocess
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