from flask import Flask, request, render_template_string
import boto3
import os

# ✅ Fix: name instead of name
app = Flask(__name__)

# Connect to LocalStack S3
try:
    s3 = boto3.client(
        's3',
        endpoint_url=os.environ.get('AWS_ENDPOINT_URL', 'http://localstack:4566'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'test'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'test'),
        region_name=os.environ.get('AWS_REGION', 'us-east-1')
    )

    BUCKET_NAME = "my-localstack-bucket"

    # ✅ Make sure bucket exists
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"✅ Using bucket: {BUCKET_NAME}")

except Exception as e:
    s3 = None
    BUCKET_NAME = None
    print(f"⚠️ S3 not available: {e}")

# HTML form
form_html = '''
    <h2>Upload a file</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file"/>
        <input type="submit"/>
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if s3 and BUCKET_NAME:
            s3.upload_fileobj(f, BUCKET_NAME, f.filename)
            return f"✅ File '{f.filename}' uploaded to S3 bucket '{BUCKET_NAME}'!"
        else:
            # Save locally if S3 is not available
            save_path = os.path.join("uploads", f.filename)
            os.makedirs("uploads", exist_ok=True)
            f.save(save_path)
            return f"💾 File saved locally at {save_path}"
    return render_template_string(form_html)

# ✅ Fix: name instead of name
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)