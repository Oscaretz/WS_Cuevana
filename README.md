# Web Scraper 
![alt text](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) 	![alt text](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
![alt text](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

## What is LetterBoxd? :clapper:	

Letterboxd is a global social network for grass-roots film discussion and discovery. Use it as a diary to record and share your opinion about films as you watch them, or just to keep track of films you have seen in the past.

Showcase your favorites on your profile page. Rate, review and tag films as you add them. Find and follow your friends to see what they are enjoying.

### What is a web scraper for Letterboxd? :film_projector:	
A web scraper for Letterboxd is a tool or program designed to extract data from the Letterboxd website automatically. This data could include information such as movie titles, release dates, ratings, reviews, and more. Web scrapers can be used for various purposes, such as gathering statistics about user preferences, analyzing trends in film ratings, or creating personalized recommendation systems. However, it's essential to use web scraping responsibly and in accordance with the website's terms of service to avoid any legal or ethical issues.

This repository contains a simple web scraper built with Python using Flask and asyncio. It allows you to scrape data from a specified URL and receive the results in JSON format. Below are the details on how to set up and use this web scraper.

## Dependencies:
We will be using the next dependencies for our code, make sure you download them:

- aiohttp
- asyncio
- bs4
- Flask[async]

If you don't have them in your computer, run the next command changing the placeholder value with the name of the required dependency:

```
pip install <placeholder>
```

## Files Included: :pick:	

1. **app.py**: This file contains the Flask application with endpoints for welcoming messages, receiving data, executing the web scraper, and checking the server status.

2. **Dockerfile**: Dockerfile for building a Docker image to run the Flask application in a containerized environment.

3. **docker-compose.yml**: Docker Compose file for defining and running multi-container Docker applications. It specifies the Flask application service.

4. **requirements.txt**: File listing the Python dependencies required for this application.

## Setting Up and Running the Application:

To download the API and initialize it, open the terminal in yout chosen Directory and run the next commands in it:

1. **Clone the Repository**: 
```
git clone https://github.com/Oscaretz/WS_LetterBox/tree/Scraper_Phase2
```
This line clone the API from the repository to your machine

2. **Navigate to the Directory**:
```
cd Scraper_Phase2
```
Open the file you just created

3. **Run the Docker Container**:
```
docker-compose up --build
```
Build and run the container using docker compose

![alt text](https://github.com/Oscaretz/WS_LetterBox/blob/Scraper_Phase2/ss/Captura%20de%20pantalla%20(1654).png?raw=true)

![alt text](https://github.com/Oscaretz/WS_LetterBox/blob/Scraper_Phase2/ss/Captura%20de%20pantalla%20(1656).png?raw=true)

## Download Postman :office_worker:	

1. **Visit the Postman Website**:
   Visit the official Postman website at [postman.com](https://www.postman.com/).

2. **Download Postman**:
   Download the Postman application for your operating system (Windows, macOS, or Linux).

3. **Install Postman**:
   After downloading the installer, follow the on-screen instructions to install Postman on your system.

## Setup Postman

Once you've installed Postman, follow these steps to set it up and start using it:

1. **Launch Postman**:
   Open the Postman application on your system.

2. **Sign Up or Log In (Optional)**:
   - If you already have a Postman account, log in using your credentials.
   - If you don't have an account, you can sign up for free by providing your email address and creating a password.

3. **Explore the Postman Interface**:
   Take a moment to familiarize yourself with the Postman interface. You'll find different sections such as Collections, Requests, Environments, and more.

4. **Create a New Request**:
   - Click on the "New" button in the top-left corner to create a new request.
   - Choose the appropriate HTTP method (GET, POST, PUT, DELETE, etc.) for your request.

5. **Enter Request URL**:
   - Enter the URL of the API endpoint you want to test in the address bar.
   - If necessary, add parameters, headers, body, etc., based on the request type.

6. **Send the Request**:
   - Click on the "Send" button to send the request to the container URL.
   - Postman will display the response received from the server.

7. **View Response**:
   - Once the request is sent, you can view the response body, headers, status code, and more in the response section below.

![alt text](https://github.com/Oscaretz/WS_LetterBox/blob/Scraper_Phase2/ss/Captura%20de%20pantalla%20(1647).png?raw=true)

8. **Explore More Features**: :construction_worker:	
    Postman offers many advanced features such as scripting, testing, sharing collections, generating documentation, and more. Explore these features to get the most out of Postman.

## Endpoints:

- **Welcome Message**:
- **Endpoint**: `/`
- **Method**: GET 
- Returns a welcome message.

---
- **Receive Data**: :satellite:	
- **Endpoint**: `/data`
- **Method**: POST 
- Accepts data in JSON format and returns a confirmation message. For example:
```json
{
    "url": https://letterboxd.com/film/the-wizard-of-oz-1939/
    } 
```
---
- **Execute Web Scraper**: :microscope:	
- **Endpoint**: `/scraper`
- **Method**: POST
- Accepts data with a URL in JSON format, scrapes the data asynchronously, and returns the results in JSON format.
---
- **Server Status**: :white_check_mark:
- **Endpoint**: `/status`
- **Method**: GET 
- Returns the status of the server.


## Notes:

- This web scraper is a simple example and may require further customization based on specific scraping needs.
- Ensure that the specified URL for scraping is accessible and returns the expected data.

Feel free to modify and expand upon this web scraper according to your requirements. If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or pull request. Happy scraping!

## Contributors:
- https://github.com/Oscaretz 
- https://github.com/LuisMichelP
- https://github.com/Moisescar3008
- https://github.com/Vale1930
