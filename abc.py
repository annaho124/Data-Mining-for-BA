import requests

# Define the login credentials and form data
username = "cel"
password = "cel"
login_url = "https://fba.simcel.io/"
form_data = {
    "username_field_name": username,
    "password_field_name": password,
    # other form data fields as needed
}

# Make the POST request to log in
response = requests.post(login_url, data=form_data)

# Check if login was successful
if response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")
