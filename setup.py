# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="aws_lambda_powertools",
    version="2.26.0",
    description="Powertools for AWS Lambda (Python) is a developer toolkit to implement Serverless best practices and increase developer velocity.",
    python_requires="==3.*,>=3.7.4",
    project_urls={
        "documentation": "https://docs.powertools.aws.dev/lambda/python/",
        "repository": "https://github.com/aws-powertools/powertools-lambda-python",
    },
    author="Amazon Web Services",
    license="MIT",
    keywords="aws_lambda_powertools aws tracing logging lambda powertools feature_flags idempotency middleware",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT No Attribution License (MIT-0)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=[
        "aws_lambda_powertools",
        "aws_lambda_powertools.event_handler",
        "aws_lambda_powertools.event_handler.middlewares",
        "aws_lambda_powertools.event_handler.openapi",
        "aws_lambda_powertools.exceptions",
        "aws_lambda_powertools.logging",
        "aws_lambda_powertools.logging.formatters",
        "aws_lambda_powertools.metrics",
        "aws_lambda_powertools.metrics.provider",
        "aws_lambda_powertools.metrics.provider.cloudwatch_emf",
        "aws_lambda_powertools.metrics.provider.datadog",
        "aws_lambda_powertools.middleware_factory",
        "aws_lambda_powertools.shared",
        "aws_lambda_powertools.tracing",
        "aws_lambda_powertools.utilities",
        "aws_lambda_powertools.utilities._data_masking",
        "aws_lambda_powertools.utilities._data_masking.provider",
        "aws_lambda_powertools.utilities._data_masking.provider.kms",
        "aws_lambda_powertools.utilities.batch",
        "aws_lambda_powertools.utilities.data_classes",
        "aws_lambda_powertools.utilities.data_classes.appsync",
        "aws_lambda_powertools.utilities.feature_flags",
        "aws_lambda_powertools.utilities.idempotency",
        "aws_lambda_powertools.utilities.idempotency.persistence",
        "aws_lambda_powertools.utilities.idempotency.serialization",
        "aws_lambda_powertools.utilities.jmespath_utils",
        "aws_lambda_powertools.utilities.parameters",
        "aws_lambda_powertools.utilities.parser",
        "aws_lambda_powertools.utilities.parser.envelopes",
        "aws_lambda_powertools.utilities.parser.models",
        "aws_lambda_powertools.utilities.streaming",
        "aws_lambda_powertools.utilities.streaming.transformations",
        "aws_lambda_powertools.utilities.typing",
        "aws_lambda_powertools.utilities.validation",
        "examples.parameters.tests.src",
        "layer.layer",
    ],
    package_dir={"": "."},
    package_data={"aws_lambda_powertools": ["*.typed"]},
    install_requires=["typing-extensions==4.*,>=4.6.2"],
    extras_require={
        "all": ["aws-xray-sdk==2.*,>=2.8.0", "fastjsonschema==2.*,>=2.14.5", "pydantic==1.*,>=1.8.2"],
        "aws-sdk": ["boto3==1.*,>=1.20.32"],
        "datadog": ["datadog-lambda==4.*,>=4.77.0"],
        "datamasking-aws-sdk": ["aws-encryption-sdk==3.*,>=3.1.1"],
        "dev": [
            "aws-cdk.aws-apigatewayv2-alpha==2.*,>=2.38.1.a0",
            "aws-cdk.aws-apigatewayv2-authorizers-alpha==2.*,>=2.38.1.a0",
            "aws-cdk.aws-apigatewayv2-integrations-alpha==2.*,>=2.38.1.a0",
            "aws-cdk-lib==2.*,>=2.103.0",
            "aws-requests-auth==0.*,>=0.4.3",
            "bandit==1.*,>=1.7.5",
            "black==23.*,>=23.3.0",
            "checksumdir==1.*,>=1.2.0",
            "coverage[toml]==7.*,>=7.2.0",
            "filelock==3.*,>=3.12.2",
            "hvac==1.*,>=1.2.1",
            "ijson==3.*,>=3.2.2",
            "isort==5.*,>=5.11.5",
            "mike==1.*,>=1.1.2",
            "mkdocs-git-revision-date-plugin==0.*,>=0.3.2",
            "mkdocs-material==9.*,>=9.2.7",
            "mypy-boto3-appconfig==1.*,>=1.28.68",
            "mypy-boto3-appconfigdata==1.*,>=1.28.36",
            "mypy-boto3-cloudformation==1.*,>=1.28.64",
            "mypy-boto3-cloudwatch==1.*,>=1.28.36",
            "mypy-boto3-dynamodb==1.*,>=1.28.66",
            "mypy-boto3-lambda==1.*,>=1.28.63",
            "mypy-boto3-logs==1.*,>=1.28.52",
            "mypy-boto3-s3==1.*,>=1.28.55",
            "mypy-boto3-secretsmanager==1.*,>=1.28.36",
            "mypy-boto3-ssm==1.*,>=1.28.68",
            "mypy-boto3-xray==1.*,>=1.28.64",
            "pdoc3==0.*,>=0.10.0",
            "pytest==7.*,>=7.4.3",
            "pytest-asyncio==0.*,>=0.21.1",
            "pytest-benchmark==4.*,>=4.0.0",
            "pytest-cov==4.*,>=4.1.0",
            "pytest-mock==3.*,>=3.11.1",
            "pytest-xdist==3.*,>=3.3.1",
            "radon==6.*,>=6.0.1",
            "types-requests==2.*,>=2.31.0",
            "xenon==0.*,>=0.9.1",
        ],
        "parser": ["pydantic==1.*,>=1.8.2"],
        "tracer": ["aws-xray-sdk==2.*,>=2.8.0"],
        "validation": ["fastjsonschema==2.*,>=2.14.5"],
    },
)
