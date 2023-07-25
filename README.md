# data_pusher

## Description
This is a Django web application that provides JSON REST APIs for managing accounts and destinations. An account can have multiple destinations, and if an account is deleted, its associated destinations will also be deleted.

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies using pip.
3. Run the Django development server.

## JSON REST APIs
### Accounts API
- GET /api/accounts/ - Get a list of all accounts.
- POST /api/accounts/ - Create a new account.
- GET /api/accounts/<account_id>/ - Get details of a specific account.
- PUT /api/accounts/<account_id>/ - Update details of a specific account.
- DELETE /api/accounts/<account_id>/ - Delete a specific account and its destinations.

### Destinations API
- GET /api/destinations/ - Get a list of all destinations.
- POST /api/destinations/ - Create a new destination.
- GET /api/destinations/<destination_id>/ - Get details of a specific destination.
- PUT /api/destinations/<destination_id>/ - Update details of a specific destination.
- DELETE /api/destinations/<destination_id>/ - Delete a specific destination.

### Get Destinations for Account
- GET /api/accounts/<account_id>/destinations/ - Get a list of destinations associated with a specific account.

## API for Receiving Data
### Incoming Data
- POST /server/incoming_data/
- JSON Format:
  {
    "data": "Your data here",
    "app_secret_token": "Your secret token here"
  }

## Notes
- Make sure to provide the correct app secret token while sending data to the server.
- Use appropriate HTTP status codes and error handling in your requests.
- The project utilizes Django Rest Framework (DRF) for easier API development.
