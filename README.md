# home-security
Home security project with Rasberry Pi3 Model B+
Using Camera Module for enhanced security when not at Home 

## Setup

### Obtaining a Google Photos API key

1. Obtain a Google Account API key (Client ID and Client Secret) by following the instructions on [Getting started with Google Photos REST APIs](https://developers.google.com/photos/library/guides/get-started)

**NOTE** When selecting your application type in Step 4 of "Request an OAuth 2.0 client ID", please select "Other". There's also no need to carry out step 5 in that section.

2. Replace `YOUR_CLIENT_ID` in the client_id.json file with the provided Client ID.
3. Replace `YOUR_CLIENT_SECRET` in the client_id.json file wiht the provided Client Secret.

### Installing dependencies and running the script

1. Make sure you have [Python 3.7](https://www.python.org/downloads/) installed on your system
2. Also, install [pipenv] (if not already present)

### Running the application
1. Clone the repo in your machine `git clone <repo_url>`
2. Goto project root `cd <project_name>`
3. Update the client_id.json file with your <YOUR_CLIENT_ID> and <YOUR_CLIENT_SECRET>
4. Give permission to execute the script start.sh `chmod 777 start.sh`
5. Run the start script to launch the application `./start.sh`

**NOTE**
If there are existing api credential files under the folder /home/pi/.credentials for example email-credential.json, photo-credential.json please delete them as the google api tokens are likely to expire and needs to be refreshed (if running the program after a longtime).
