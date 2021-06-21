# Final Project - REST API

Contoso Medical wants to open a SARS-Cov2 test center. They have comissioned you with creating the necessary APIs!

## Booking API
- Everyone can book an appointment
- Appointments should be stored using a GUID (Globally unique identifier)
- Appointments should expect some parameters
- First name, last name, street, post code, city, email address
- User should be able to use their GUID to cancel their appointment
- There should be a way to list all open appointments
- Booked appointments may only be received when the GUID is used

## Test results API
- Admins publish test results using an API key or similar query-string or header-based authentication
- Admins can remove results using an API key or similar query-string or header-based authentication
- Users use their GUID to display their result

## Bonus features
- Appointment storage persistent in a database
- Authorization and authentication: Admins should be able to view and remove all appointments and tests after authenticating. This can be a database with users and hashed passwords, but ideally would use OAuth2 to allow Google and Microsoft accounts to be used

## Technical details:
- You can use any REST framework. Flask is easier to use, Django has more features.
- Store all your project files in your personal folder in this repository. If you are using Flask, you can simply use the little template app.py in your folder.
- For the project to be successful it is enough to use an in-memory database (i.e. an array or a hashtable)
- Your API can use the query string or a body to accept data
  - If you use a query string, take care to encode the parameter values! (Hint: from urllib.parse import urlencode, quote_plus)