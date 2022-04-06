# Oxford-Assassins
Website for the Oxford Guild of Assassins.
Written in:
| Language   | Feature             |
|------------|---------------------|
| Python     | Primary Language    |
| Django     | Web Framework       |
| HTML       | Page Templates      |
| CSS        | Page Styling        |
| JavaScript | Page Responsiveness |\
<br>
<br>

## Overview of File Structure:
### oxfordassassins
The Django entrypoint, contains the settings for the project and primary URLs.
### base
The base app manages the home page and other public facing information pages.
### account
The account app manages user accounts, sessions, and user information.
### admin
The admin app allows administrator level users to view and modify the website's databases.
### games
The games app shows all games, historic, ongoing, and upcoming, and manages sign-ups.
### play
The play app is what assassins interact with in-game, it manages all the game mechanics and info.
### static
The static directory contains styles (.css), scripts (.js), and resources (image, audio, etc) for the website.
### templates
The templates directory contains generic html templates for the pages that are built upon.\
<br>
<br>

## Webpage Structure:
### /
| URL                | Page                    |
|--------------------|-------------------------|
|   /                | Home Page               |
|   /about/          | About the Guild         |
|   /blog/           | Recent Guild Activity   |
|   /cabal/          | Profiles of the Cabal   |
|   /discord/        | Invite to the Discord   |
### /account/   
| URL                | Page                    |
|--------------------|-------------------------|
|   ../              | User Account Settings   |
|   ../login/        | Login                   |
|   ../logout/       | Logout                  |
|   ../register/     | Register                |
|   ../profile/*id*/ | View *id*'s Profile     |
### /admin/
| URL                | Page                    |
|--------------------|-------------------------|
|   ../              | Admin Overview          |
|   ../about/        | Edit About Content      |
|   ../blog/         | Edit Blog Posts DB      |
|   ../cabal/        | Edit Cabal Profiles DB  |
|   ../users/        | Edit Users DB           |
|   ../games/        | Manage Games            |
### /games/   
| URL                | Page                    |
|--------------------|-------------------------|
|   ../              | List of all Games       |
|   ../*id*/         | View Game (or signup)   |
### /play/   
| URL                | Page                    |
|--------------------|-------------------------|
|   ../              | Play Overview           |
|   ../events/       | View In|Game Events     |
|   ../map/          | Map of Active Assassins |
|   ../report/       | Report a Kill/Death     |
|   ../stats/        | Veiw Stats for the game |
|   ../teams/        | View Teams              |\
<br>
<br>

## Todo List:
### Website Text:
- [ ] About the Guild Text
- [ ] About the Cabal Text
- [ ] About the Games Text
- [ ] About the Discord Small Paragraph\
<br>
- [ ] Guildmaster Role Paragraph
- [ ] Treasurer Role Paragraph
- [ ] Archivist Role Paragraph
- [ ] Social Sec Role Paragraph
- [ ] MWP Role Paragraph\
<br>
- [ ] Freshers Game Summary Paragraph
- [ ] Freshers Game Blog Post Text
- [ ] Data Breach Game Summary Paragraph
- [ ] Data Breach Game Blog Post Text
- [ ] Infection Game Summary Paragraph
- [ ] Infection Game Blog Post Text
- [ ] Varsity Match Summary Paragraph
- [ ] Varsity Match Blog Post Text
- [ ] Lightbringers Game Summary Paragraph
- [ ] Lightbringers Game Blog Post Text

### Website Design and Non-Functional Mockups:
- [ ] Colour Palette
- [ ] Assets
- [ ] Logo with Transparency
- [ ] Logo as 32x32 icon
- [ ] General Styling\
<br>
- [ ] Home Page
- [ ] About the Guild Page
- [ ] Blog Page
- [ ] Cabal Page
- [ ] Discord Page\
<br>
- [ ] Account Settings Page
- [ ] Account Login Page
- [ ] Account Logout Page
- [ ] Account Register Page
- [ ] User Profile Page\
<br>
- [ ] Games Page
- [ ] Historic Game Page
- [ ] Signup Game Page\
<br>
- [ ] Play Overview Page
- [ ] In-Game Events Page
- [ ] In-Game Map Page
- [ ] In-Game Report Page
- [ ] In-Game Stats Page
- [ ] In-Game Teams Page

### Website Backend:
- [ ] URL Tree (Per App)
- [ ] Data Models (Per App)
- [ ] Database Setup\
<br>
- [ ] Navigation Bar
- [ ] Main Template\
<br>
- [ ] Home Page
- [ ] About the Guild Page
- [ ] Blog Page
- [ ] Cabal Page
- [ ] Discord Page\
<br>
- [ ] Account Settings Page
- [ ] Account Login Page
- [ ] Account Logout Page
- [ ] Account Register Page
- [ ] User Profile Page\
<br>
- [ ] Admin Pages\
<br>
- [ ] Games Page
- [ ] Historic Game Page
- [ ] Signup Game Page\
<br>
- [ ] Play Overview Page
- [ ] In-Game Events Page
- [ ] In-Game Map Page
- [ ] In-Game Report Page
- [ ] In-Game Stats Page
- [ ] In-Game Teams Page