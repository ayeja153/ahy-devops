# ahy-devops

To run container:

      docker run -d -p 8080:8080 flask-app

To deploy AWS cloudformation in CLI:

      aws cloudformation deploy --template-file cloudformation.yaml --stack-name cloudformation-cli
