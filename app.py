from flask import Flask, request, render_template_string
import boto3
import os

app = Flask(__name__)

# Connect to LocalStack's S3
s3 = boto3.client(
    's3',
    endpoint_url=os.environ.get('AWS_ENDPOINT_URL', 'http://localhost:4566'),
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'test'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'test'),
    region_name=os.environ.get('AWS_REGION', 'us-east-1')
)

BUCKET_NAME = 'my-localstack-bucket'

# HTML form
form_html = '''
    <h2>Upload a file to LocalStack S3</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file"/>
        <input type="submit"/>
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        s3.upload_fileobj(f, BUCKET_NAME, f.filename)
        return f"✅ File '{f.filename}' uploaded to S3 bucket '{BUCKET_NAME}'!"
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
