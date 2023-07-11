# Spotify Playlist Generator
By utilizing the Open AI API and Spotipy API, this repository allows users to submit a desired playlist theme and have an AI generated playlist automatically created in your Spotify account. I have included two versions of the program - a terminal based program as well as a program including a simple front end which is locally hosted using Flask.

Some playlist theme examples include: "best pop songs from the 2010's", "classical music for studying", "best songs from the artist coldplay", "upbeat songs for a morning run", etc.  
The more specific the prompt, the easier it will be for Open AI to interpret. 

Keep in mind the AI provided by Open AI is only trained up to September 2021, so it may not know current artists, songs, or music trends.
# Getting Started
- **Step 1:** Create an Open AI account (if necessary) and create an [API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
- **Step 2:** Follow "getting started" on [this page](https://developer.spotify.com/documentation/web-api) and save your Spotify keys. For redirect URI, set it to http://127.0.0.1:8080/
- **Step 3:** Install necessary dependencies
```bash
pip install spotipy
pip install openai
pip install flask
 ```
- **Step 4:** Install this repository to your machine and open the folder in your favorite IDE.

In app.py, replace "YOUR API KEY" on line 12 with your Open AI API key from step 1.

Open a new terminal and declare environment variables using the following commands. Replace YOUR CLIENT ID and YOUR CLIENT SECRET with the keys obtained in step 2 respectively.

WINDOWS:  
```bash
$Env:SPOTIPY_CLIENT_ID = "YOUR CLIENT ID"
$Env:SPOTIPY_CLIENT_SECRET = "YOUR CLIENT SECRET"
$Env:SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8080/"
 ```

OTHER OS:  
```bash
export SPOTIPY_CLIENT_ID="YOUR CLIENT ID"
export SPOTIPY_CLIENT_SECRET="YOUR CLIENT SECRET"
export SPOTIPY_REDIRECT_URI="http://127.0.0.1:8080/"
 ```
- **Step 5:** In your terminal run
```bash
python3 app.py
```
and open the local dev server http://127.0.0.1:5000
