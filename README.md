## CPSC8710_Project_1

### Participating Group Members: Alex Buchanan, Pavan Sai Manam , Kishore Patam

## OBJECTIVES
This is a variant of the classic 'Sorry' game, where 4x players each roll a dice and move their pieces on a predermined track around the board.  Players roll once, and if they score a 6 on their roll, then they're released from their home base.  If, during their travels around the board, two player pieces happen to land on the same location, the player moving sends the other players piece back to their home base and they have to start over.  The player that makes a full run of the board first wins.

## TECHNOLOGY STACK
### Python - Webserver
### PyGame
### PygBag
### Openssl

## SETUP AND DEPLOYMENT
Note: Will only run on Windows
After unziping the folder ->

1. Run :
        pip install pygame pygbag
2. Ensure pygbag and pygame are both included in the PATH variable on Windows
3. Open the CMD prompt and navigate to the directory above the unzipped project folder
4. Run : 
		pygbag --bind [Local Host] --port 8000 --ume_block 0 [Folder Name]
5. Be sure to use the right local host address (127.0.0.1 if working locally) and the folder name is the same as the unzipped file that should be in your current directory
6. Open a browser and navigate to the ip address you inputted above and be sure to include :8000 at the end of it to specify the correct port
7. The game is played via spacebar and the players are cycled through automatically

## 3rd Party Asset Notes
* https://pypi.org/project/pygbag/
* https://www.pygame.org/docs/
* https://data-flair.training/blogs/python-ludo-game/ - Visual Assets / Basic Code Base

## Basic Info About The Game
1. The game is a multiplayer game (2-4 player game). The game can be played with friends or 2-player game with the computer.
2. Each player has 4 coins. Player can choose which coin to move based on his choice.
3. Who ever takes all the 4 coins to the end first will be the winner.
4. Each player spins the dice and moves the respective steps from starting position.
5. When a player throws a six, he gets to throw again.
6. Each player should throw a 6 for each coin to get to starting position. When a player throws a six, a coin gets ability to start moving.
7. Without a 6 there, players cannot start the game.
8. When a player is at a particular position and if another player lands on same position( other than safe zones) The player who is already in there needs to go to starting position.

## Notes/Reflections
This project presented a unique set of challenges from both a technical and collaborative standpoint. The initial hurdle was the novelty of hosting and the lack of documentation surrounding Pygame for hosting Python game projects. While Pygame is a versatile and widely used library for game development, its application for hosting online multiplayer games may not be the most optimal choice, as the project experienced a significant performance dip when hosted compared to running natively.

From a technical perspective, the necessity to refactor the borrowed source code and encapsulate variables within classes was a vital but demanding task. This process likely increased the project's maintainability and readability, but it also consumed a significant amount of time and effort.

Furthermore, the project highlighted the importance of documentation and thorough codebase explanations. This became especially evident when dealing with the complexities of hosting and online multiplayer integration. Future endeavors in similar domains should prioritize well-documented code and thorough resources to aid in the development process.

Collaboratively, intergroup challenges arose, primarily stemming from issues related to Git and GitHub. The inability of some group members to push to or pull from the GitHub repository posed a considerable obstacle. Despite numerous attempts to address this issue, it hindered the ability of these team members to contribute effectively to the project. This scenario emphasizes the importance of strong version control and Git proficiency within development teams, as well as the need for immediate issue resolution.

Scheduling and group meetings also proved to be challenging aspects of this project. Coordinating the availability of team members and ensuring that group meetings were productive required considerable effort.

The project's overall experience underscores the "man-month rule," which suggests that adding more members to a project can sometimes lead to complications and slow progress, especially if those members require extensive training or face technical difficulties. This observation highlights the significance of assembling a skilled and experienced team, as well as the importance of considering team dynamics and individual skill levels.

In conclusion, this project was a valuable learning experience, both in terms of technical skills and team dynamics. The challenges faced provided insights into the complexities of online game hosting and the significance of well-documented code. While difficulties with Git and group coordination arose, they serve as lessons for future endeavors, emphasizing the importance of technical proficiency and effective communication within a development team.

## External Links
Github - https://alex-buchanan.github.io/CPSC8710_Project_1/


		
