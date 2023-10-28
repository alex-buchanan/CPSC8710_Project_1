## CPSC8710_Project_1

### Participating Group Members: Alex Buchanan, Pavan Sai Manam

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
This project was challenging due to the novelty of hosting and lack of documentation around pygbag for hosting python pygame projects.  The original source code borrowed from the above website had to be significantly refactored, and all of the variables encapsulated in classes.  For a demonstration of this project, please see the link below. There is a marked dip in performance when hosting the project as opposed to running it natively that was unexpected, and in the future the lesson appears to be that pygame is not the best or even most stable architecture on which to host a game.  

The intergroup challenges mainly stemmed from an inability of other group members to push to or pull from the github repository that was set up despite several attempts to resolve the issue on the owners part.  This apparently limited their ability to contribute to this project significantly.  Scheduling times and group meetings also proved a challenge, as did efforts to resolve issues such as the github issue mentioned above. 

Overall, this project was a good example of the man-month rule.  Adding members more often than not complicates and slows down a project, especially if the other members require significant training.

## External Links
Github - https://alex-buchanan.github.io/CPSC8710_Project_1/
Server Host - 127.0.0.1:8000


		
