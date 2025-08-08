# AWS S3 Lifecycle Policy Utility

This Python script allows you to easily configure **Amazon S3 Lifecycle policies** for your buckets.  
It supports applying lifecycle rules to:

- The **entire bucket**
- A **specific folder** (prefix)

The lifecycle policy created by this script applies the following rules to **current versions** of objects:

<img width="533" height="184" alt="image" src="https://github.com/user-attachments/assets/19d12671-90dc-441a-8807-00e6b7ce5ef6" />


- **Day 0** – Objects uploaded to S3 (no action)
- **Day 30** – Transition to `STANDARD_IA` (Standard-Infrequent Access)
- **Day 60** – Transition to `ONEZONE_IA` (One Zone-Infrequent Access)
- **Day 90** – Expire (permanently delete) the objects

It also lists all available buckets in your AWS account so you can easily select the target bucket.

---

## Prerequisites

- Python **3.6** or above installed.
- AWS credentials configured on your machine with sufficient permissions to apply lifecycle policies (`s3:PutLifecycleConfiguration` and `s3:GetLifecycleConfiguration`) using the AWS CLI or environment variables.
- `boto3` Python library and dependencies installed (listed in `requirements.txt`).

---

## Setup Instructions

1. **Create & activate a virtual environment**:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

2. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Configure AWS credentials**:
    - Via CLI:
      ```
      aws configure
     

4. **Run the script**:
    ```
    python lifecyclepolicy.py
    ```

---

## Execution & Outputs

