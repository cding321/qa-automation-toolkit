import base64
import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright

load_dotenv()

# Basic Auth
def test_basic_auth(playwright: Playwright):
    request_context = playwright.request.new_context()

    credentials = base64.b64encode(b"user:pass").decode("utf-8")

    response = request_context.get("https://httpbin.org/basic-auth/user/pass",
                                   headers={"Authorization": f"Basic {credentials}"})

    assert response.status == 200

    response_body = response.json()  # 99% of the times you will see json format
    # response_body = response.text() -- HTML format response
    print("Response body: ",response_body)

    request_context.dispose()

# Bearer Token Authentication
def test_bearer_token_auth_github_repos(playwright: Playwright):
    token = os.getenv("GITHUB_TOKEN")

    # return the response for repository
    request_context = playwright.request.new_context()
    response = request_context.get("https://api.github.com/user/repos",
                                   headers={"Authorization": f"Bearer {token}"})
    # return the response for specific user
    # response = request_context.get("https://api.github.com/user",
    #                               headers={"Authorization": f"Bearer {token}"})

    assert response.status == 200
    response_body = response.json()
    print("Response body(Repositories): ",response_body)

    request_context.dispose()


# API Key Authentication - weatherAPI
def test_api_key_auth_openweather(playwright: Playwright):
    request_context = playwright.request.new_context()

    query_params = {
        "q":"Delhi",
        "appid":os.getenv("OPENWEATHER_API_KEY")
    }

    response = request_context.get("https://api.openweathermap.org/data/2.5/weather",
                                   params=query_params)

    assert response.status == 200
    response_body = response.json()
    print("weather info: ====> ",response_body)

    request_context.dispose()


# OAuth2 Authentication

# 1) From the application get the following. (Manual process)
# https://imgur.com/
#     1) Client ID
#     2) Client Secrete
#
# 2) Send Post request for getting token
# POST https://api.imgur.com/oauth2/token
# 	ClientID
# 	Client secrete
# 	tokenURL
# 	Redirect URL
# 	Grant type
# 	Authorization code
#
# you will get token once POST request is successful.
#
# 3) Use Token to do API call ( Get request).

'''
def test_verify_oauth2_authentication(playwright: Playwright):
    # Step 1: Initialize request context
    request_context = playwright.request.new_context()

    # Step 2: Define client credentials and OAuth2 parameters
    client_id = ""
    client_secret = ""
    redirect_uri = "https://www.getpostman.com/oauth2/callback"
    grant_type = "authorization_code"
    authorization_code = ""  # Replace with valid code

    # Step 3: Send POST request to get the access token
    token_response = request_context.post(
        "https://api.imgur.com/oauth2/token",
        form={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "code": authorization_code,
            "redirect_uri": redirect_uri
        }
    )

    # Step 4: Validate token response
    assert token_response.status == 200
    token_data = token_response.json()
    access_token = token_data.get("access_token")
    print(f"\nGenerated Access Token: {access_token}")

    assert access_token is not None, "Access token not found in response!"

    # Step 5: Use access token to make authenticated GET request
    image_response = request_context.get(
        "https://api.imgur.com/3/account/me/images",
        headers={
            "Authorization": f"Bearer {access_token}"}
    )

    # Step 6: Validate image API response
    assert image_response.status == 200
    print("\nResponse JSON:", image_response.json())

    # Step 7: Cleanup
    request_context.dispose()
'''

