# Oxford-Assassins
Website for the Oxford Guild of Assassins.
Written in:
| Language   | Feature             |
|------------|---------------------|
| Python     | Primary Language    |
| Django     | Web Framework       |
| HTML       | Page Templates      |
| CSS        | Page Styling        |
| JavaScript | Page Responsiveness |
<br>
<br>


## Overview of File Structure:
| File | Description |
| ---- | ----------- |
| oxfordassassins | The Django entrypoint, contains the settings for the project and primary URLs. |
| base            | The base app manages the home page and other public facing information pages. |
| account         | The account app manages user accounts, sessions, and user information. |
| admin           | The admin app allows administrator level users to view and modify the website's databases. |
| games           | The games app shows all games, historic, ongoing, and upcoming, and manages sign-ups. |
| play            | The play app is what assassins interact with in-game, it manages all the game mechanics and info. |
| static          | The static directory contains styles (.css), scripts (.js), and resources (image, audio, etc) for the website. |
| templates       | The templates directory contains generic html templates for the pages that are built upon. |
| Website-Design  | Directory for non-functional mockups of the website. |
<br>
<br>


## Webpage Structure:
### /
| URL                | Page                    |
|--------------------|-------------------------|
|   /                | Home Page               |
|   /#home           | Landing Page            |
|   /#about          | About the Guild         |
|   /#termcard       | Termcard of events      |
|   /#cabal          | Profiles of the Cabal   |
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
|   ../cabal/        | Edit Cabal Profiles DB  |
|   ../users/        | Edit Users DB           |
|   ../games/        | Manage Games/Events     |
### /play/   
| URL                | Page                    |
|--------------------|-------------------------|
|   ../              | Play Overview           |
|   ../events/       | View In|Game Events     |
|   ../map/          | Map of Active Assassins |
|   ../report/       | Report a Kill/Death     |
|   ../stats/        | Veiw Stats for the game |
|   ../teams/        | View Teams              |
<br>
<br>


## Todo List:
### Website Text:
- [X] About the Guild Text
- [X] About the Cabal Text
- [X] About the Games Text
- [X] About the Discord Small Paragraph
<br>

- [X] Guildmaster Role Paragraph
- [X] Treasurer Role Paragraph
- [X] Archivist Role Paragraph
- [X] Social Sec Role Paragraph
- [X] MWP Role Paragraph
<br>

### Website Design and Non-Functional Mockups:
- [X] Colour Palette
- [X] Assets
- [X] Logo with Transparency
- [X] Logo as 32x32 icon
- [X] General Styling
<br>

- [X] Home Page
- [X] About the Guild Page
- [X] Termcard Page
- [X] Cabal Page
<br>

- [ ] Account Settings Page
- [ ] Account Login Page
- [ ] Account Logout Page
- [ ] Account Register Page
- [ ] User Profile Page
<br>

- [ ] Games Page
- [ ] Historic Game Page
- [ ] Signup Game Page
<br>

- [ ] Play Overview Page
- [ ] In-Game Events Page
- [ ] In-Game Map Page
- [ ] In-Game Report Page
- [ ] In-Game Stats Page
- [ ] In-Game Teams Page

### Website Backend:
- [X] URL Tree (Per App)
- [ ] Data Models (Per App)
- [ ] Database Setup
<br>

- [X] Navigation Bar
- [X] Main Template
<br>

- [X] Home Page
- [X] About the Guild Page
- [X] Termcard Page
- [X] Cabal Page
<br>

- [ ] Account Settings Page
- [ ] Account Login Page
- [ ] Account Logout Page
- [ ] Account Register Page
- [ ] User Profile Page
<br>

- [ ] Admin Pages
<br>

- [ ] Games Page
- [ ] Historic Game Page
- [ ] Signup Game Page
<br>

- [ ] Play Overview Page
- [ ] In-Game Events Page
- [ ] In-Game Map Page
- [ ] In-Game Report Page
- [ ] In-Game Stats Page
- [ ] In-Game Teams Page
