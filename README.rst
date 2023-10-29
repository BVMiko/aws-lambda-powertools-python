.. role:: raw-html-m2r(raw)
   :format: html


:raw-html-m2r:`<!-- markdownlint-disable MD013 MD041 MD043  -->`

Powertools for AWS Lambda (Python)
==================================


.. image:: https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/quality_check.yml/badge.svg
   :target: https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/python_build.yml
   :alt: Build


.. image:: https://codecov.io/github/aws-powertools/powertools-lambda-python/branch/develop/graphs/badge.svg
   :target: https://app.codecov.io/gh/aws-powertools/powertools-lambda-python
   :alt: codecov.io


.. image:: https://img.shields.io/static/v1?label=python&message=%203.7|%203.8|%203.9|%203.10|%203.11&color=blue?style=flat-square&logo=python
   :target: https://img.shields.io/static/v1?label=python&message=%203.7|%203.8|%203.9|%203.10|%203.11&color=blue?style=flat-square&logo=python
   :alt: PythonSupport

.. image:: https://badge.fury.io/py/aws-lambda-powertools.svg
   :target: https://badge.fury.io/py/aws-lambda-powertools.svg
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/dm/aws-lambda-powertools
   :target: https://img.shields.io/pypi/dm/aws-lambda-powertools
   :alt: PyPi monthly downloads

.. image:: https://api.securityscorecards.dev/projects/github.com/aws-powertools/powertools-lambda-python/badge
   :target: https://api.securityscorecards.dev/projects/github.com/aws-powertools/powertools-lambda-python
   :alt: OpenSSF Scorecard

.. image:: https://dcbadge.vercel.app/api/server/B8zZKbbyET
   :target: https://discord.gg/B8zZKbbyET
   :alt: Join our Discord


Powertools for AWS Lambda (Python) is a developer toolkit to implement Serverless `best practices and increase developer velocity <https://docs.powertools.aws.dev/lambda/python/latest/#features>`_.

..

   Also available in `Java <https://github.com/aws-powertools/powertools-lambda-java>`_\ , `Typescript <https://github.com/aws-powertools/powertools-lambda-typescript>`_\ , and `.NET <https://github.com/aws-powertools/powertools-lambda-dotnet>`_.


**\ `📜Documentation <https://docs.powertools.aws.dev/lambda/python/>`_\ ** | **\ `🐍PyPi <https://pypi.org/project/aws-lambda-powertools/>`_\ ** | **\ `Roadmap <https://docs.powertools.aws.dev/lambda/python/latest/roadmap/>`_\ ** | **\ `Detailed blog post <https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/>`_\ **

..

   **An AWS Developer Acceleration (DevAx) initiative by Specialist Solution Architects | aws-devax-open-source@amazon.com**



.. image:: https://user-images.githubusercontent.com/3340292/198254617-d0fdb672-86a6-4988-8a40-adf437135e0a.png
   :target: https://user-images.githubusercontent.com/3340292/198254617-d0fdb672-86a6-4988-8a40-adf437135e0a.png
   :alt: hero-image


Features
--------


* **\ `Tracing <https://docs.powertools.aws.dev/lambda/python/latest/core/tracer/>`_\ ** - Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions
* **\ `Logging <https://docs.powertools.aws.dev/lambda/python/latest/core/logger/>`_\ ** - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details
* **\ `Metrics <https://docs.powertools.aws.dev/lambda/python/latest/core/metrics/>`_\ ** - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)
* **\ `Event handler: AppSync <https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/appsync/>`_\ ** - AWS AppSync event handler for Lambda Direct Resolver and Amplify GraphQL Transformer function
* **\ `Event handler: API Gateway and ALB <https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/api_gateway/>`_\ ** - Amazon API Gateway REST/HTTP API and ALB event handler for Lambda functions invoked using Proxy integration
* **\ `Bring your own middleware <https://docs.powertools.aws.dev/lambda/python/latest/utilities/middleware_factory/>`_\ ** - Decorator factory to create your own middleware to run logic before, and after each Lambda invocation
* **\ `Parameters utility <https://docs.powertools.aws.dev/lambda/python/latest/utilities/parameters/>`_\ ** - Retrieve and cache parameter values from Parameter Store, Secrets Manager, or DynamoDB
* **\ `Batch processing <https://docs.powertools.aws.dev/lambda/python/latest/utilities/batch/>`_\ ** - Handle partial failures for AWS SQS batch processing
* **\ `Typing <https://docs.powertools.aws.dev/lambda/python/latest/utilities/typing/>`_\ ** - Static typing classes to speedup development in your IDE
* **\ `Validation <https://docs.powertools.aws.dev/lambda/python/latest/utilities/validation/>`_\ ** - JSON Schema validator for inbound events and responses
* **\ `Event source data classes <https://docs.powertools.aws.dev/lambda/python/latest/utilities/data_classes/>`_\ ** - Data classes describing the schema of common Lambda event triggers
* **\ `Parser <https://docs.powertools.aws.dev/lambda/python/latest/utilities/parser/>`_\ ** - Data parsing and deep validation using Pydantic
* **\ `Idempotency <https://docs.powertools.aws.dev/lambda/python/latest/utilities/idempotency/>`_\ ** - Convert your Lambda functions into idempotent operations which are safe to retry
* **\ `Feature Flags <https://docs.powertools.aws.dev/lambda/python/latest/utilities/feature_flags/>`_\ ** - A simple rule engine to evaluate when one or multiple features should be enabled depending on the input
* **\ `Streaming <https://docs.powertools.aws.dev/lambda/python/latest/utilities/streaming/>`_\ ** - Streams datasets larger than the available memory as streaming data.

Installation
^^^^^^^^^^^^

With `pip <https://pip.pypa.io/en/latest/index.html>`_ installed, run: ``pip install aws-lambda-powertools``

Tutorial and Examples
---------------------


* `Tutorial <https://docs.powertools.aws.dev/lambda/python/latest/tutorial>`_
* `Serverless Shopping cart <https://github.com/aws-samples/aws-serverless-shopping-cart>`_
* `Serverless Airline <https://github.com/aws-samples/aws-serverless-airline-booking>`_
* `Serverless E-commerce platform <https://github.com/aws-samples/aws-serverless-ecommerce-platform>`_
* `Serverless GraphQL Nanny Booking Api <https://github.com/trey-rosius/babysitter_api>`_

How to support Powertools for AWS Lambda (Python)?
--------------------------------------------------

Becoming a reference customer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Knowing which companies are using this library is important to help prioritize the project internally. If your company is using Powertools for AWS Lambda (Python), you can request to have your name and logo added to the README file by raising a `Support Powertools for AWS Lambda (Python) (become a reference) <https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=customer-reference&template=support_powertools.yml&title=%5BSupport+Lambda+Powertools%5D%3A+%3Cyour+organization+name%3E>`_ issue.

The following companies, among others, use Powertools:


* `Capital One <https://www.capitalone.com/>`_
* `CPQi (Exadel Financial Services) <https://cpqi.com/>`_
* `CloudZero <https://www.cloudzero.com/>`_
* `CyberArk <https://www.cyberark.com/>`_
* `globaldatanet <https://globaldatanet.com/>`_
* `IMS <https://ims.tech/>`_
* `Jit Security <https://www.jit.io/>`_
* `Propellor.ai <https://www.propellor.ai/>`_
* `TopSport <https://www.topsport.com.au/>`_
* `Trek10 <https://www.trek10.com/>`_
* `Vertex Pharmaceuticals <https://www.vrtx.com/>`_

Sharing your work
^^^^^^^^^^^^^^^^^

Share what you did with Powertools for AWS Lambda (Python) 💞💞. Blog post, workshops, presentation, sample apps and others. Check out what the community has already shared about Powertools for AWS Lambda (Python) `here <https://docs.powertools.aws.dev/lambda/python/latest/we_made_this/>`_.

Using Lambda Layer or SAR
^^^^^^^^^^^^^^^^^^^^^^^^^

This helps us understand who uses Powertools for AWS Lambda (Python) in a non-intrusive way, and helps us gain future investments for other Powertools for AWS Lambda languages. When `using Layers <https://docs.powertools.aws.dev/lambda/python/latest/#lambda-layer>`_\ , you can add Powertools for AWS Lambda (Python) as a dev dependency (or as part of your virtual env) to not impact the development process.

Credits
-------


* Structured logging initial implementation from `aws-lambda-logging <https://gitlab.com/hadrien/aws_lambda_logging>`_
* Powertools for AWS Lambda (Python) idea `DAZN Powertools <https://github.com/getndazn/dazn-lambda-powertools/>`_

Connect
-------


* **Powertools for AWS Lambda on Discord**\ : ``#python`` - **\ `Invite link <https://discord.gg/B8zZKbbyET>`_\ **
* **Email**\ : aws-lambda-powertools-feedback@amazon.com

Security disclosures
--------------------

If you think you’ve found a potential security issue, please do not post it in the Issues.  Instead, please follow the instructions `here <https://aws.amazon.com/security/vulnerability-reporting/>`_ or `email AWS security directly <mailto:aws-security@amazon.com>`_.

License
-------

This library is licensed under the MIT-0 License. See the LICENSE file.
