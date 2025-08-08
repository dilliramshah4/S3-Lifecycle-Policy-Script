import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_buckets(s3_client):
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response.get('Buckets', [])]
    return buckets

def copy_s3_bucket(source_bucket, destination_bucket, aws_region=None):
    try:
        session = boto3.Session(region_name=aws_region) if aws_region else boto3.Session()
        s3 = session.resource('s3')
        source = s3.Bucket(source_bucket)
        dest = s3.Bucket(destination_bucket)

        objects = list(source.objects.all())
        print(f"Found {len(objects)} objects in bucket '{source_bucket}' to copy.")

        for obj in objects:
            dest_key = obj.key  # Preserves folder structure
            copy_source = {'Bucket': source_bucket, 'Key': obj.key}
            print(f'Copying {obj.key} to {destination_bucket}/{dest_key}')
            dest.copy(copy_source, dest_key)

        print("All files copied successfully.")

    except NoCredentialsError:
        print("AWS credentials not found. Please configure them (e.g., via awscli or environment variables).")
    except PartialCredentialsError:
        print("Incomplete AWS credentials found. Please check your configuration.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Use low-level client to list buckets
        s3_client = boto3.client('s3')
        buckets = list_buckets(s3_client)
        if not buckets:
            print("No S3 buckets found in your AWS account.")
            exit(1)

        print("Available S3 buckets:")
        for idx, bucket_name in enumerate(buckets, 1):
            print(f"{idx}. {bucket_name}")

        source_bucket = input("\nEnter the source bucket name from the above list: ").strip()
        if source_bucket not in buckets:
            print(f"Error: Source bucket '{source_bucket}' not found in your bucket list.")
            exit(1)

        destination_bucket = input("Enter the destination bucket name from the above list: ").strip()
        if destination_bucket not in buckets:
            print(f"Error: Destination bucket '{destination_bucket}' not found in your bucket list.")
            exit(1)

        aws_region = input("Enter AWS region (press enter to skip): ").strip() or None

        copy_s3_bucket(source_bucket, destination_bucket, aws_region)

    except NoCredentialsError:
        print("AWS credentials not found. Please configure them before running the script.")
    except Exception as e:
        print(f"An error occurred: {e}")
