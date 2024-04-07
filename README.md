Referral System API
Objective
The objective of this project is to build a referral system API that allows users to register, view their details, and view their referrals.

Requirements
User Registration Endpoint:

Accepts POST requests
Required fields: name, email, password
Optional field: referral_code (if provided, the user who referred this user should receive a point)
Returns a unique user ID and a success message
User Details Endpoint:

Accepts GET requests
Requires an Authorization header with a valid token
Returns the user's details (name, email, referral_code, timestamp of registration)
Referrals Endpoint:

Accepts GET requests
Requires an Authorization header with a valid token
Returns a list of users who registered using the current user's referral_code (if any)
Returns a paginated response (e.g. 20 users per page)
Returns the timestamp of registration for each referral
Additional Requirements
The API should be built using either Django.
Unit tests should be written for each endpoint.
Timestamps should be used for any field that is meant to be a datetime field.
The API should be well-documented and easy to use.
This API must be deployed using Docker & Docker Compose.
Use Git for version control.
Commit messages should be clear and concise.
Setup and Usage
Install Docker and Docker Compose.
Clone this repository.
Navigate to the project directory.
Run docker-compose up to build and start the containers.
Access the API at http://localhost:8000.
API Endpoints
User Registration Endpoint: POST /register/
User Details Endpoint: GET /details/
Referrals Endpoint: GET /referrals/
