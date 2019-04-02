# a4.py
# Beverly Balasu bb532
# 4/20/17
# Skeleton by Lillian Lee (LJL2), April 2017


class Outcome(object):
    """An instance is an outcome in a tournament tree.

    Attributes:
    winner [nonempty str]: name of the winner in this Outcome
        Must be the same as the name of *exactly one* of attributes input1 or
            input2, defined next.

    input1 [Outcome or nonempty string]:
        If a nonempty string, the name of a competitor in the tournament, and
            we say that the name of input1 is that string.
        If an Outcome, then the name of input1 is its winner attribute.

    input2 [Outcome or nonempty string]:
        If a nonempty string, the name of a competitor in the tournament, and
            we say that the name of input2 is that string
        If an Outcome, then the name of input2 is its winner attribute.

    Note that the constraints (invariants) on winner imply that the names of
        input1 and input2 must be different.
    """

    def __init__(self, in1, in2, one_won=True):
        """Makes an Outcome have input1 set to in1, input2 set to in2, and winner
        set as follows:
            If one_won is True or not given, winner is in1's winner (if in1 is
                an Outcome) or in1 itself (if in1 is a string)
            Otherwise, winner is set to in2's winner (if in2 is an Outcome) or
                in2 itself (if in2 is a string)

            We choose the default value of one_won as True because tournaments
                are often set up so that input1 is the competitor favored to win.

        Preconditions:
            in1 is either a nonempty string or an Outcome
            in2 is either a nonempty string or an Outcome.
            name1 is different from name2, where:
              if in1 is an Outcome, name1 is in1's winner, otherwise name1 is in1
              if in2 is an Outcome, name2 is in2's winner, otherwise name2 is in2
            one_won is a boolean."""
        self.input1 = in1
        self.input2 = in2
        if one_won == True:
            self.winner = _extract_name(in1)
        else:
           self.winner = _extract_name(in2)


    def __str__(self):
        """String representation of this Outcome"""

        output = self.winner + "\n"

        output += "\t" # start indenting for the sub-Outcomes
        s1 = str(self.input1) # A recursive call
        # Inspiration for using splitlines with True, which preserves newlines
        #  at line ends:
        # http://stackoverflow.com/questions/18389454/add-some-characters-at-the-beginning-of-each-line
        s1_lines = s1.splitlines(True)
        #
        # The join in the next line of code indents the 2nd through the last
        # line of s1, since it puts tabs "between" all the lines in the
        # split-line version.
        output += "\t".join(s1_lines)
        #
        if isinstance(self.input1,str):
            output += "\n"

        # More compact version of above recursion except on self.input2
        output += "\t" + "\t".join(str(self.input2).splitlines(True))
        if isinstance(self.input2,str):
            output += "\n"

        return output

    def teams(self):
        """Returns: alphabetized list of names of teams participating in this Outcome
        or any of its sub-Outcomes or any of their sub-Outcomes, and so on.
        No team should be included more than once."""
        teamList = []
        team1 = self.input1
        team2 = self.input2
        
        if type(team1) == Outcome:
            teamList = teamList + team1.teams()
        else:
            teamList.append(team1)
        if type(team2) == Outcome:
            teamList+=team2.teams()
        else:
            teamList.append(team2)
        
        duplicate_free_list = []
        for x in range(len(teamList)):
            if teamList[x] not in duplicate_free_list:
                duplicate_free_list.append(teamList[x])
                
        duplicate_free_list.sort()
        return duplicate_free_list



    def pathToVictory(self):
        """Returns: list of teams that the winner of this Outcome defeated in
        this Outcome and all of its sub-Outcomes, sorted in order of earliest
        opponents first."""
        losers = []
        team1 = self.input1
        team2 = self.input2
         
        if self.winner == _extract_name(team1):
            if type(team1) == Outcome:
                losers = team1.pathToVictory() + [_extract_name(team2)] + losers
            else:
                losers.append(team2)
        else:
            if type(team2) == Outcome:
                losers = team2.pathToVictory() + [_extract_name(team1)] + losers
            else:
                losers.append(team1)
        
        return losers 

    def hasHeadToHead(self, c1, c2):
        """Returns True if anywhere in the tournament tree represented by this
        Outcome there is an Outcome oc where the name of one of oc's inputs
        is c1 and the name of the other of oc's inputs is c2.
        Returns False otherwise, including if c1 and c2 are not in self.teams()

        Precondition: c1 and c2 are different non-empty strings."""
        faceOff = False
        if c1 not in self.teams():
            return False
        if c2 not in self.teams():
            return False
        
        team1 = self.input1
        team2 = self.input2
        team1_name = _extract_name(team1)
        team2_name = _extract_name(team2)
        
        if team1_name in [c1,c2] and team2_name in [c1,c2]:
                faceOff = True
        else:
                faceOff = False
      
        if type(team1) == Outcome:
            faceOff = faceOff or team1.hasHeadToHead(c1,c2)
            
        if type(team2) == Outcome:
            faceOff = faceOff or team2.hasHeadToHead(c1,c2)
            
        return faceOff


## NON-METHOD FUNCTIONS GO BELOW THIS LINE

def _extract_name(x):
    """Returns: string that is the "name" of x, defined as follows:
    If x is an Outcome, then the name is x's winner.
    If x is a string, then the name of x is x itself.

    Precondition: x is either a non-empty string or an Outcome."""
    if isinstance(x, Outcome):
        return x.winner
    else:
        # x must be a string, by precondition
        assert isinstance(x, str), "_extract_name: bad input x: " + str(x)
        return x


