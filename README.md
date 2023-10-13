# Test Assignment (QA Engineer)

## 1. API Service Testing

Задача:
Using the Reqres service with a test  REST-API https://reqres.in/,  write 2 tests.

The first - retrieve a list of users (GET https://reqres.in/api/users?page=2) and check that all fields have arrived, also validate the email field.

The second - create a user (POST https://reqres.in/api/users) with data from the example on the site: prepare the request body, send the request, receive the server response, and check that the response contains the same values as the request.

Automated tests must be written using the following stack:
Python, Pytest, Request

## 2. UI Testing (Web Application)

Task:
* launch Chrome
* open https://www.yandex.ru
* type "Planet for me" in the search bar
* click Find
* check that https://planetfor.me is in the search results
* go to the website https://planetfor.me
* type “qa” in the “Search” field and check for search results.

The automated test must be written using the following stack:
Python, Pytest, Selenium (Selenoid)
## 3. UI Testing (Mobile Application)

To complete this task, it will be necessary to download the mobile application "Planet for me: notebook and organizer of places and links" from Google Play.
Auto test task:
* launch the application
* go through the authorization stage
* go to the Search section
* type “Moscow” in the “Search” field and check for search results.

The automated test must be written using the following stack:
Python, Pytest, Appium (Selenoid)