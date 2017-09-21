lambda-python-local-sample
===

## Keywords
- AWS Lambda
- Python
- [awslabs/aws-sam-local](https://github.com/awslabs/aws-sam-local)
- [localstack/localstack](https://github.com/localstack/localstack)

## Setup
```bash
# create network
$ docker network create localstack_network
```

## Commands
```bash
# start localstack
$ docker-compose up

# start api
$ sam local start-api --docker-network localstack_network
```
