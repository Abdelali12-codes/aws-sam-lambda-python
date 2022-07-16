# aws sam tutorial



## first step 

* create the template file


## third step

* run the build command to install the dependencies of the lambda function
that reside in requirements.txt file or package.json

## create s3 bucket

```
aws s3 mb s3://name-of-bucket
``

## create package artificats 

```
sam package \
  --template-file template.yml \
  --output-template-file package.yml \
  --s3-bucket your-S3-bucket
```

## deploy the application


```
sam deploy \
  --template-file package.yml \
  --stack-name aws-lambda-function-python \
  --capabilities CAPABILITY_IAM

```

