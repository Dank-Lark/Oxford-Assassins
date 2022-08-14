# Oxford-Assassins
Website for the Oxford Guild of Assassins.
Written in:
| Language | Feature |
| - | - |
| Python | Primary Language |
| Django | Web Framework |
| HTML | Page Templates |
| CSS | Page Styling |
| JavaScript | Page Responsiveness |

<br>

---

## Overview of File Structure:
| File | Description |
| - | - |
| account | The account app manages user accounts, sessions, and user information. |
| base | The base app manages the home page and other public facing information pages. |
| games | The games app manages games, gameplay, signup, and creation. |
| oxfordassassins | The Django entrypoint, contains the settings for the project and primary URLs. |
| static | The static directory contains styles (.css), scripts (.js), and resources (image, audio, etc) for the website. |
| templates | The templates directory contains generic html templates for the pages that are built upon. |

<br>

---

<!-- TODO Update Webpage structure section to reflect current urls -->
## Webpage Structure:
### /
| URL | Page |
| - | - |
| / | Home Page (all of the below) |
| /#home | Landing Page |
| /#about | About the Guild |
| /#termcard | Termcard of events |
| /#cabal | Profiles of the Cabal |
### /account/   
| URL | Page |
| - | - |
| ../ | User Account Settings |
| ../login/ | Login |
| ../logout/ | Logout |
| ../register/ | Register |
| ../profile/*id*/ | View *id*'s Profile |
### /admin/
| URL | Page |
| - | - |
| ../ | Admin Overview |
| ../about/ | Edit About Content |
| ../cabal/ | Edit Cabal Profiles DB |
| ../users/ | Edit Users DB |
| ../games/ | Manage Games/Events |
### /manage/   
| URL                | Page                    |
| - | - -----|
|   ../              | Play Overview           |
|   ../events/       | View In|Game Events     |
|   ../map/          | Map of Active Assassins |
|   ../report/       | Report a Kill/Death     |
|   ../stats/        | Veiw Stats for the game |
|   ../teams/        | View Teams              |
### /play/   
| URL                | Page                    |
| - | - -----|
|   ../              | Play Overview           |
|   ../events/       | View In|Game Events     |
|   ../map/          | Map of Active Assassins |
|   ../report/       | Report a Kill/Death     |
|   ../stats/        | Veiw Stats for the game |
|   ../teams/        | View Teams              |

<br>

---