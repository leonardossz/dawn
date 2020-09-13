# Dawn - AWS Aurora Serverless Client

A Command-line client to talk with Aurora Serverless Cluster.

# Requirements

1. Python 3.8+ (May work on 3.x versions, not tested. Feedbacks are welcome)
2. Aurora Serverless Cluster with Data API Enabled (https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)
3. AWS Client Credentials configured (https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) 

# Installation

## From PyPI Repository

Yet to be published ;)

TBD

## From Source

You do not have to wait for an Official release on PyPI. Clone this repository and run: 
    
    python setup.py install

# Running

    $ dawncli <cluster-arn> <secret-arn> <database>
    
See the example below:

    somedb | mysql> select 1 from dual;
    {
        "ResponseMetadata": {
            "HTTPHeaders": {
                "content-length": "58",
                "content-type": "application/json",
                "date": "Sun, 13 Sep 2020 13:10:17 GMT",
                "x-amzn-requestid": "4f2f1808-2a7c-4c4a-8148-d2208cc1079a"
            },
            "HTTPStatusCode": 200,
            "RequestId": "4f2f1808-2a7c-4c4a-8148-d2208cc1079a",
            "RetryAttempts": 0
        },
        "numberOfRecordsUpdated": 0,
        "records": [
            [
                {
                    "longValue": 1
                }
            ]
        ]
    }
    
    somedb | mysql> 
    
So far the output is JSON. A tabular output is planned!
