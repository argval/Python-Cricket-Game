import random

print('''
Welcome to Cricket! (but in Python! 🐍🏏)
How is Cricket played in the first place? Well here's a brief overview: 
A guy is batting, another guy is bowling, and there are fielders all around the field. 
The bowler bowls the ball, the batter hits the ball, and the fielders try to catch the ball. 
The batter can run between the wickets to score runs. The bowler tries to get the batter out. 
The batter tries to score as many runs as possible. The team with the most runs wins. Simple, right? 🏏

But how do you represent this in Python? 🤔
Now that's a challenging question. Well here's the basic layout:
1. We create a coin toss in the beginning to decide who bats/bowls first.
2. Both the teams will have 6 players each.
3. This can be a multiplayer game or a single player game. In the case of a singleplayer game, the computer will play as the second team.
4. The game will have 3 overs in total.
5. Both the teams have a choice to choose between the numbers 1-6. The number chosen will be the runs scored.
6. What's the point of the bowling team choosing the numbers then? Well, the idea is, if the bowling team chooses the same number as the batting team, the batting team will be out.
7. The aim of the batting team is to score as many runs as possible. The aim of the bowling team is to get the batting team out as quickly as possible.
8. This game will be played in a turn-based format. The batting team will bat first, followed by the bowling team. So basically, two innings.
9. The team with the most runs at the end of the game wins.
''')

teams = {
    'MI': ['Rohit Sharma', 'Ishan Kishan', 'Suryakumar Yadav', 'Hardik Pandya', 'Gerald Coetzee', 'Jasprit Bumrah'],
    'CSK': ['MS Dhoni', 'Rachin Ravindra', 'Ruturaj Gaikwad', 'Shivam Dube', 'Ravindra Jadeja', 'Mustafizur Rahman'],
    'RCB': ['Virat Kohli', 'Faf du Plessis', 'Rajat Patidar', 'Glenn Maxwell', 'Lockie Ferguson', 'Mohammed Siraj'],
    'KKR': ['Shreyas Iyer', 'Sunil Narine', 'Nitish Rana', 'Andre Russell', 'Mitchell Starc', 'Rinku Singh'],
    'DC': ['Rishabh Pant', 'David Warner', 'Mitchell Marsh', 'Jhye Richardson', 'Shai Hope', 'Ravichandran Ashwin'],
    'PK': ['Shikhar Dhawan', 'Jonny Bairstow', 'Sam Curran', 'Arshdeep Singh', 'Kagiso Rabada', 'Chris Woakes'],
    'RR': ['Sanju Samson', 'Jos Buttler', 'Ben Stokes', 'Riyan Parag', 'Avesh Khan', 'Yuzvendra Chahal'],
    'SRH': ['Travis Head', 'Heinrich Klassen', 'Abhishek Sharma', 'Pat Cummins', 'T Natarajan', 'Bhuvneshwar Kumar'],
    'GT': ['Shubman Gill', 'David Miller', 'Shahrukh Khan', 'Kane Williamson', 'Mohammed Shami', 'Umesh Yadav'],
    'LSG': ['KL Rahul', 'Devdutt Padikkal', 'Marcus Stoinis', 'Krunal Pandya', 'Naveen Ul Haq', 'Shamar Joseph']
}

class Cricket:
    def __init__(self, team1, team2, single):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 0
        self.team2_score = 0
        self.team1_wickets = 0
        self.team2_wickets = 0
        self.team1_players = teams[team1]
        self.team2_players = teams[team2]
        self.current_batsman = 0
        self.current_bowler = 0
        self.current_over = 0
        self.current_innings = 1
        self.team1_overs = []
        self.team2_overs = []
        self.team1_bowling = []
        self.team2_bowling = []
        self.team1_bowling_wickets = 0
        self.team2_bowling_wickets = 0
        self.single = single
        self.target = 0
        self.batting_team = ''
        self.bowling_team = ''
        
    def coin_toss(self):
        '''toss = random.choice([self.team1, self.team2])
        print(f'{toss} won the toss and chose to bat first!')
        if toss == self.team1:
            self.batting_team = self.team1
            self.bowling_team = self.team2
        else:
            self.batting_team = self.team2
            self.bowling_team = self.team1
        print(f'{self.batting_team} will bat first and {self.bowling_team} will bowl first!')'''
        toss = random.randint(1, 2)
        toss_choice = int(input('Enter 1 for heads and 2 for tails: '))
        if toss == toss_choice:
            print(f'{self.team1} won the toss!')
            choice = int(input(f'{self.team1}, enter 1 to bat first and 2 to bowl first: '))
            if choice == 1:
                self.batting_team = self.team1
                self.bowling_team = self.team2
                print(f'{self.team1} will bat first and {self.team2} will bowl first!')
            else:
                self.batting_team = self.team2
                self.bowling_team = self.team1
                print(f'{self.team2} will bat first and {self.team1} will bowl first!')
        else:
            if single == True:
                print('Computer won the toss!')
                choice = random.randint(1, 2)
                if choice == 1:
                    self.batting_team = self.team2
                    self.bowling_team = self.team1
                    print(f'{self.team2} will bat first and {self.team1} will bowl first!')
                else:
                    self.batting_team = self.team1
                    self.bowling_team = self.team2
                    print(f'{self.team1} will bat first and {self.team2} will bowl first!')
            else:
                print(f'{self.team2} won the toss!')
                choice = int(input(f'{self.team2}, enter 1 to bat first and 2 to bowl first: '))
                if choice == 1:
                    self.batting_team = self.team2
                    self.bowling_team = self.team1
                    print(f'{self.team2} will bat first and {self.team1} will bowl first!')
                else:
                    self.batting_team = self.team1
                    self.bowling_team = self.team2
                    print(f'{self.team1} will bat first and {self.team2} will bowl first!')
                
            
    def multiplayer(self):
        if self.batting_team == self.team1:
            print(f'1st Innings underway, {self.team1} is batting first! And {self.team2} is bowling!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team1_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Dot ball!')
                        runs = 0 # Dot ball
                        continue
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Wide Ball!')
                        runs += 1
                        continue
                    if runs == bowl:
                        print(f'{self.team2_players[self.current_bowler]} has taken a wicket!')
                        self.team2_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team1_score += runs
                        self.team1_overs.append(runs)
                    self.current_ball += 1
                self.current_bowler += 1
                if self.team1_wickets == 5 or self.current_over == 3:
                    break
                self.current_over += 1
                
            self.target = self.team1_score + 1
            print(f'{self.team1} has scored {self.team1_score} runs!')
            print(f'{self.team2} needs {self.target} runs to win!')
            
            self.batting_team = self.team2
            self.bowling_team = self.team1
            print(f'2nd Innings underway, {self.team2} is batting now! And {self.team1} is bowling! {self.team2} needs {self.target} runs to win!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team2_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Dot ball!')
                        runs = 0 # Dot ball
                        continue
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Wide Ball!')
                        runs += 1
                        continue
                    if runs == bowl:
                        print(f'{self.team1_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team2_score += runs
                        self.team2_overs.append(runs)
                        if self.team2_score >= self.target:
                            break
                    self.current_ball += 1
                    if self.team2_wickets == 5 or self.current_over == 3:
                        break
                self.current_over += 1
                self.current_bowler += 1

            print(f'{self.team2} has scored {self.team2_score} runs!')
            if self.team2_score >= self.target:
                print(f'{self.team2} has won the match')
            elif self.team2_score == self.team1_score:
                print('The match is a tie!')
            elif self.team2_score < self.target:
                print(f'{self.team1} has won the match!')
        
        else:
            print(f'1st Innings underway, {self.team2} is batting first! And {self.team1} is bowling!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team2_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    if runs == bowl:
                        print(f'{self.team1_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team2_score += runs
                        self.team2_overs.append(runs)
                    self.current_ball += 1
                if self.team2_wickets == 6 or self.current_over == 3:
                    break
                self.current_over += 1
            self.target = self.team2_score + 1    
            if self.current_over == 3 or self.team2_wickets == 6:
                print(f'{self.team2} has scored {self.team2_score} runs!')
                print(f'{self.team1} needs {self.target} runs to win!')
            
            self.batting_team = self.team1
            self.bowling_team = self.team2
            print(f'2nd Innings underway, {self.team1} is batting now! And {self.team2} is bowling! {self.team1} needs {self.target} runs to win!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team1_players[self.current_bowler]} is bowling!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    if runs == bowl:
                        print(f'{self.team2_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team1_score += runs
                        self.team1_overs.append(runs)
                        if self.team1_score >= self.target:
                            break
                    self.current_ball += 1
                if self.team1_score >= self.target or self.team1_wickets == 6:
                    break
                self.current_over += 1
                if self.current_over == 3:
                    break
            print(f'{self.team1} has scored {self.team1_score} runs!')
            if self.team1_score >= self.target:
                print(f'{self.team1} has won the match')
            elif self.team1_score == self.team2_score:
                print('The match is a tie!')
            elif self.team1_score < self.target:
                print(f'{self.team2} has won the match!')
                
    def singleplayer(self):
        if self.batting_team == self.team1:
            print(f'1st Innings underway, {self.team1} is batting first! And {self.team2} is bowling!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team1_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Dot ball!')
                        runs = 0 # Dot ball
                        continue
                    bowl = random.randint(1,6)
                    if runs == bowl:
                        print(f'{self.team2_players[self.current_bowler]} has taken a wicket!')
                        self.team2_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team1_score += runs
                        self.team1_overs.append(runs)
                    self.current_ball += 1
                self.current_bowler += 1
                if self.team1_wickets == 5 or self.current_over == 3:
                    break
                self.current_over += 1
                
            self.target = self.team1_score + 1
            print(f'{self.team1} has scored {self.team1_score} runs!')
            print(f'{self.team2} needs {self.target} runs to win!')
            
            self.batting_team = self.team2
            self.bowling_team = self.team1
            print(f'2nd Innings underway, {self.team2} is batting now! And {self.team1} is bowling! {self.team2} needs {self.target} runs to win!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team2_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = random.randint(1,6)
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Wide Ball!')
                        runs += 1
                        continue
                    if runs == bowl:
                        print(f'{self.team1_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team2_score += runs
                        self.team2_overs.append(runs)
                        if self.team2_score >= self.target:
                            break
                    self.current_ball += 1
                    if self.team2_wickets == 5 or self.current_over == 3:
                        break
                self.current_over += 1
                self.current_bowler += 1

            print(f'{self.team2} has scored {self.team2_score} runs!')
            if self.team2_score >= self.target:
                print(f'{self.team2} has won the match')
            elif self.team2_score == self.team1_score:
                print('The match is a tie!')
            elif self.team2_score < self.target:
                print(f'{self.team1} has won the match!')
        
        else:
            print(f'1st Innings underway, {self.team2} is batting first! And {self.team1} is bowling!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team2_players[self.current_batsman]} is on strike!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = random.randint(1,6)
                    bowl = int(input('Enter a ball between 1-6: '))
                    if bowl < 1 or bowl > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    if runs == bowl:
                        print(f'{self.team1_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team2_score += runs
                        self.team2_overs.append(runs)
                    self.current_ball += 1
                if self.team2_wickets == 6 or self.current_over == 3:
                    break
                self.current_over += 1
            self.target = self.team2_score + 1    
            if self.current_over == 3 or self.team2_wickets == 6:
                print(f'{self.team2} has scored {self.team2_score} runs!')
                print(f'{self.team1} needs {self.target} runs to win!')
            
            self.batting_team = self.team1
            self.bowling_team = self.team2
            print(f'2nd Innings underway, {self.team1} is batting now! And {self.team2} is bowling! {self.team1} needs {self.target} runs to win!')
            self.current_over = 0
            while self.current_over < 3:
                print(f'\n{self.current_over + 1} over is in progress!')
                print(f'{self.team2_players[self.current_bowler]} is bowling!')
                self.current_ball = 0
                while self.current_ball < 6:
                    runs = int(input('Enter the number of runs (1-6): '))
                    if runs < 1 or runs > 6:
                        print('Invalid input! Please enter a number between 1-6.')
                        continue
                    bowl = random.randint(1,6)
                    if runs == bowl:
                        print(f'{self.team2_players[self.current_bowler]} has taken a wicket!')
                        self.team1_wickets += 1
                        self.current_batsman += 1
                    else:
                        self.team1_score += runs
                        self.team1_overs.append(runs)
                        if self.team1_score >= self.target:
                            break
                    self.current_ball += 1
                if self.team1_score >= self.target or self.team1_wickets == 6:
                    break
                self.current_over += 1
                if self.current_over == 3:
                    break
            print(f'{self.team1} has scored {self.team1_score} runs!')
            if self.team1_score >= self.target:
                print(f'{self.team1} has won the match')
            elif self.team1_score == self.team2_score:
                print('The match is a tie!')
            elif self.team1_score < self.target:
                print(f'{self.team2} has won the match!')
    
    def play_game(self):
        self.coin_toss()
        if self.single == True:
            self.singleplayer()
        else:
            self.multiplayer()

        
team1 = input('Enter the name of the first team: ')
team2 = input('Enter the name of the second team: ')
mode = input('Enter "single" for single player mode or "multi" for multiplayer mode: ').lower()
if mode == 'single':
    single = True
else:
    single = False
game = Cricket(team1, team2, single)
game.play_game()