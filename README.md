Automated AWS CI/CD Pipeline with LocalStack
Project Overview

This project demonstrates a robust, cost-effective DevOps workflow for cloud-native applications. It uses LocalStack to emulate a full AWS environment, allowing for rigorous testing of underlying infrastructure without incurring live cloud costs or risking production stability.

Why this is relevant for DeFi & Trading Terminals
Zero-Downtime Infrastructure: By mocking services like S3, Lambda, and DynamoDB locally, we ensure that on-chain data processing scripts are bug-free before deployment.
Handling High Volume: The architecture includes stress-testing for Rate Limiting to prevent "Too Many Requests" (429) errors, which is critical during high-volatility trading periods.
Cost Efficiency: Reduces cloud "burn rate" by validating all Infrastructure as Code (IaC) changes in an emulated environment.
Technical Stack
Cloud Emulation: LocalStack (S3, IAM, Lambda, DynamoDB)
CI/CD: GitHub Actions
IaC: AWS CLI / Terraform Scripts
Automation: Shell Scripting / YAML

How to Run
Clone the repo: git clone https://github.com/OkoroJulian/localstack-ci-cd-project
Start LocalStack: docker-compose up
Run Pipeline: Push a change to the main branch to trigger the GitHub Action workflow for automated infrastructure validation.

# localstack-ci-cd-project

Managing of Infrastructure for CI/CD Development using IaC in all within a Local Development Environment



\# **LocalStack CI/CD Project** 



This project demonstrates a \*\*CI/CD pipeline\*\* for deploying a simple \*\*Flask application\*\* that interacts with \*\*AWS S3\*\*.  

Instead of using real AWS services for development, it uses \*\*\[LocalStack](https://localstack.cloud/)\*\* to simulate AWS locally.  



\## **Features**

\- Flask backend application

\- Dockerized app and LocalStack services

\- Terraform for S3 bucket provisioning

\- AWS CLI for file uploads

\- CI/CD pipeline configuration (`.gitlab-ci.yml`)

\- Local development without AWS costs



---



\## **Tech Stack**

\- \*\*Python 3 / Flask\*\*

\- \*\*Docker\*\* \& \*\*Docker Compose\*\*

\- \*\*LocalStack\*\* (for local AWS simulation)

\- \*\*Terraform\*\*

\- \*\*AWS CLI\*\*

\- \*\*GitLab CI/CD\*\*



---



**## Project Structure**

.

├── app.py # Flask app

├── Dockerfile # Flask app Docker image

├── docker-compose.yml # Multi-service Docker setup

├── main.tf # Terraform config for AWS S3

├── s3.tf # S3 bucket definition

├── variables.tf # Terraform variables

├── outputs.tf # Terraform outputs

├── requirements.txt # Python dependencies

├── .gitlab-ci.yml # GitLab CI/CD pipeline

└── README.md # Project documentation





**Start Services with Docker**



docker-compose up --build



This starts:



Flask app (http://localhost:5000)



LocalStack (http://localhost:4566)



**Provision S3 Bucket with Terraform**

Initialize Terraform



terraform init



**Apply Infrastructure**



terraform apply -auto-approve



**Upload a File to S3**

aws --endpoint-url=http://localhost:4566 s3 cp ./invoice.txt s3://my-test-bucket/



**List Files in S3**

aws --endpoint-url=http://localhost:4566 s3 ls s3://my-test-bucket/



**CI/CD Workflow**

Push changes to main branch



Pipeline runs automatically:



Build Docker image



Run tests



Deploy to LocalStack



Artifacts are stored for review



**Notes**

.terraform/ is ignored to prevent large files from being pushed to GitHub.



For real AWS deployment, update provider configs in Terraform and Flask app to use AWS endpoints.





[ASCII diagrams](https://chatgpt.com/s/m_6898cc03f2008191becfc466739f74f1)



**How it Works**



Developer writes code → pushes to GitHub/GitLab.



CI/CD Pipeline builds Docker images and runs tests.



Docker Compose starts both:



Flask app (your API)



LocalStack (mock AWS services)



Terraform provisions an S3 bucket inside LocalStack.



Flask app or CLI uploads files to the S3 bucket — all locally, no AWS charges.


