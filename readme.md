# Customer Order Service

This is a simple Python REST API service that  manages customers and orders. It includes authentication via OpenID Connect and sends SMS notifications to customers when new orders are created.

## Features

- Customer management (create, read, update, delete)
- Order management (create, read, update, delete)
- Authentication using Google OpenID Connect
- SMS notifications for new orders using Africa's Talking SMS gateway
- Containerized application using Docker
- Automated testing and deployment using GitHub Actions

## Tech Stack

- Python 
- Django 
- Django REST Framework
- PostgreSQL
- GitHub Actions

## Prerequisites

- Python 3.9 or higher
- PostgreSQL
- Pipenv (for managing virtual environments)
- An Google OpenID Connect provider account
- An Africa's Talking account for SMS functionality

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/peterowira/customer-order-service.git
   cd customer-order-service
   pipenv install
   ```

2. Create a `.env` file in the project root and add the following environment variables:
   ```
   AT_API_KEY=your_africastalking_api_key
   AT_USERNAME=your_africastalking_username
   OIDC_RP_CLIENT_ID=-your_google_oidc_client_id
   OIDC_RP_CLIENT_SECRET=your_google_oidc_client_secret
   OIDC_OP_AUTHORIZATION_ENDPOINT=your_google_authorization_endpoint
   OIDC_OP_TOKEN_ENDPOINT==your_google_token_endpoint
   OIDC_OP_USER_ENDPOINT==your_google_userinfo_endpoint
   DB_NAME=your_db
   DB_USER=your_db_username
   DB_PASSWORD=your_db_username_password
   DB_HOST=localhost
   DB_PORT=db_port_number
   ```


3. Apply database migrations:
   ```
   pipenv run python manage.py migrate
   ```

4. Run the API service:
   ```
   pipenv run python manage.py runserver
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:8000/api/`.

- Customers endpoint: `http://localhost:8000/api/customers/`
- Orders endpoint: `http://localhost:8000/api/orders/`

You can use tools like curl, Postman, or a web browser using swagger to interact with the API.

- Swagger endpoint: `http://localhost:8000/swagger/`


## Authentication

This service uses Google OpenID Connect for authentication.To access protected endpoints, you need to include valid cookis in the Authorization header of your requests:

To authenticate use this endpoint: `http://localhost:8000/oidc/authenticate/`




## Running Tests

To run the test suite:

```
python manage.py test

```

To run tests with coverage:

```
pipenv run coverage run manage.py test
pipenv run coverage report
```


## Acknowledgments

- Django and Django REST Framework communities
- Africa's Talking for SMS functionality
- Google OpenID Connect for authentication

