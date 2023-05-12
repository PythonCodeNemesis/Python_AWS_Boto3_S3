import boto3

# Create a new S3 bucket
def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

# Upload a file to the bucket
def upload_file(bucket_name, file_path, object_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name)

# List objects in the bucket
def list_objects(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print('Bucket is empty')

# Demo
if __name__ == '__main__':
    # Set your bucket name and file details
    bucket_name = 'your-bucket-name'
    file_path = 'path/to/your/file.jpg'
    object_name = 'file.jpg'
    
    # Create a new bucket
    create_bucket(bucket_name)
    print('Bucket created successfully!')
    
    # Upload a file to the bucket
    upload_file(bucket_name, file_path, object_name)
    print('File uploaded successfully!')
    
    # List objects in the bucket
    print('Objects in the bucket:')
    list_objects(bucket_name)
