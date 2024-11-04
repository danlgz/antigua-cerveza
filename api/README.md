# API

This part of the project was made with the tools described bellow:

1. Python 3.11
2. Default unit test library
3. FastAPI
4. Pydantic


This project take adventage of Hexagonal Architeture in these parts:

1. Layer: domain, application, infrastructure
2. Domain entities to ensure the "objecets" adhere to the expected type and shape
3. Domin repositories: contracts that describe the way to connect with external services
4. Application: business logic
5. Infrastructure: implementation of repositories (currently memory data) and handlers
