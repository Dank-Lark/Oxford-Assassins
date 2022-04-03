# Oxford-Assassins
Website for the Oxford Guild of Assassins.
Written in:
| Python     | Primary Language
| Django     | Web Framework
| HTML       | Page Templates
| CSS        | Page Styling 
| JavaScript | Page Responsiveness


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
The templates directory contains generic html templates for the pages that are built upon.


## Webpage Structure:
### /
|   /                | Home Page               |
|   /about/          | About the Guild         |
|   /blog/           | Recent Guild Activity   |
|   /cabal/          | Profiles of the Cabal   |
|   /discord/        | Invite to the Discord   |
### /account/   
|   ../              | User Account Settings   |
|   ../login/        | Login                   |
|   ../logout/       | Logout                  |
|   ../signup/       | Signup                  |
|   ../profile/*id*/ | View *id*'s Profile     |
### /admin/
|   ../              | Admin Overview          |
|   ../about/        | Edit About Content      |
|   ../blog/         | Edit Blog Posts DB      |
|   ../cabal/        | Edit Cabal Profiles DB  |
|   ../users/        | Edit Users DB           |
|   ../games/        | Manage Games            |
### /games/   
|   ../              | List of all Games       |
|   ../*id*/         | View Game (or signup)   |
### /play/   
|   ../              | Play Overview           |
|   ../events/       | View In|Game Events     |
|   ../map/          | Map of Active Assassins |
|   ../report/       | Report a Kill/Death     |
|   ../stats/        | Veiw Stats for the game |
|   ../teams/        | View Teams              |


## Task List:
| [ ] Create a Task List