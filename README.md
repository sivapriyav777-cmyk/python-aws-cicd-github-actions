# python-aws-cicd-github-actions
Python CI/CD pipeline using GitHub Actions and AWS Lambda

# Python AWS CI/CD Pipeline Using GitHub Actions

## Project Overview

This project demonstrates automated testing and deployment of a Python application to AWS Lambda using GitHub Actions.

## Technologies Used

- Python
- GitHub Actions
- AWS Lambda
- AWS IAM
- Pytest

## Features

- Automated Python unit testing
- CI/CD pipeline using GitHub Actions
- Secure AWS authentication using OIDC
- Automatic Lambda deployment
- Deployment only after successful tests

## Project Workflow

1. Developer pushes Python code to GitHub.
2. GitHub Actions starts the workflow.
3. Python dependencies are installed.
4. Automated tests are executed.
5. If tests pass on the main branch, the application is packaged.
6. Updated code is deployed to AWS Lambda.

## Learning Outcomes

- Understanding Continuous Integration and Continuous Deployment
- Writing GitHub Actions YAML workflows
- Testing Python applications using Pytest
- Automating AWS Lambda deployments
- Managing AWS deployment permissions securely
