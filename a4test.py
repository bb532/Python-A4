# a4test.py
# Beverly Balasu bb532
# 4/20/17
# Skeleton by Lillian Lee (LJL2), Apr 10, 2017

"""  'Pretty good' checks for code in a4.py. """

## STUDENTS: We are not going to demand exhaustive testing, but we do require
## you to create three reasonable test cases for each of your methods. These
## test cases should have representatives of each of the following sorts of Outcomes:
##      * a "base-case" Outcome whose input1 and input2 attributes are both strings
##      * a "standard" multi-layer balanced Outcome,
##      * an "unbalanced" Outcome, where one of input1/input2 is a string and the other
##          is an Outcome.  It doesn't have to be large: ours has just three
##          competitors in it.
## To make this easier for you, we include code below that will generate a
## standard Outcome for you, assuming your __init__method for Outcomes is correct.


from a4 import *
import cornelltest as ct
import inspect # for automatically getting function names


# Helper provided for student use; do not modify
def standard_outcome():
    """Returns the sweet-16 Outcome depicted in Figure 1 of the CS1110 Spring
    2017 A4 handout, assuming a correct implementation of the Outcome __init__
    method in a4."""

    # You can compose calls to Outcome()
    east = Outcome(Outcome("Wisconsin", "Florida", False),
                   Outcome("Baylor", "South Carolina", False),
                   False)
    west = Outcome(Outcome("Gonzaga","West Virginia"),
                   Outcome("Xavier", "Arizona"))
    midwest = Outcome(Outcome("Kansas", "Purdue"),
                      Outcome("Oregon","Michigan"),
                      False)
    south = Outcome(Outcome("North Carolina", "Butler"),
                    Outcome("UCLA", "Kentucky", False))

    return Outcome(Outcome(east, west, False), Outcome(midwest, south, False), False)

def baseCase_outcome():
    return Outcome('Texas A&M', 'UT', True)

def unbalanced_outcome():
    return Outcome(Outcome('Cornell','Harvard'),'Princeton')

def standard_outcome_str():
    """Returns the string that should be the result of str(standard_outcome()) if
    a4 contains a correct implementation of __init__"""
    output = 'North Carolina\n'
    output += '\tGonzaga\n'
    output += '\t\tSouth Carolina\n'
    output += '\t\t\tFlorida\n'
    output += '\t\t\t\tWisconsin\n'
    output += '\t\t\t\tFlorida\n'
    output += '\t\t\tSouth Carolina\n'
    output += '\t\t\t\tBaylor\n'
    output += '\t\t\t\tSouth Carolina\n'
    output += '\t\tGonzaga\n'
    output += '\t\t\tGonzaga\n'
    output += '\t\t\t\tGonzaga\n'
    output += '\t\t\t\tWest Virginia\n'
    output += '\t\t\tXavier\n'
    output += '\t\t\t\tXavier\n'
    output += '\t\t\t\tArizona\n'
    output += '\tNorth Carolina\n'
    output += '\t\tOregon\n'
    output += '\t\t\tKansas\n'
    output += '\t\t\t\tKansas\n'
    output += '\t\t\t\tPurdue\n'
    output += '\t\t\tOregon\n'
    output += '\t\t\t\tOregon\n'
    output += '\t\t\t\tMichigan\n'
    output += '\t\tNorth Carolina\n'
    output += '\t\t\tNorth Carolina\n'
    output += '\t\t\t\tNorth Carolina\n'
    output += '\t\t\t\tButler\n'
    output += '\t\t\tKentucky\n'
    output += '\t\t\t\tUCLA\n'
    output += '\t\t\t\tKentucky\n'
    return output

def baseCase_outcome_str():
    return str(baseCase_outcome())

def unbalanced_outcome_str():
    return str(unbalanced_outcome())

def standard_outcome_teams():
    """Returns the list that should be the result of standard_outcome().teams()
    if the code in a4 is correctly implemented."""

    # It's OK to let Python alphabetize rather than doing it oneself!
    return sorted(["Wisconsin", "Florida","Baylor", "South Carolina",
                   "Gonzaga","West Virginia","Xavier", "Arizona",
                   "Kansas", "Purdue","Oregon","Michigan",
                   "North Carolina", "Butler", "UCLA", "Kentucky"])

def baseCase_outcome_teams():
    return sorted(["Texas A&M", "UT"])

def unbalanced_outcome_teams():
    return sorted(["Cornell", "Harvard","Princeton"])


def standard_outcome_path():
    """Returns the list that should be the result of
    standard_outcome().pathToVictory() if the code in a4 is correctly
    implemented."""
    return ['Butler', 'Kentucky', 'Oregon', 'Gonzaga']

def unbalanced_outcome_path():
    return ['Harvard', 'Princeton']

def baseCase_outcome_path():
    return ['UT']


def test_init():
    """Test a4 Outcome __init__ using our prewritten __str__ method."""
    print "Running " + inspect.stack()[0][3] # prints out this test method

    ## STUDENTS: We've implemented testing of a standard Outcome for you.
    standard = standard_outcome()
    print "\t testing test case with winner " + str(standard.winner)
    right_answer = standard_outcome_str()
    output = str(standard)
    ct.assert_equals(right_answer, output)
    print '\t\t test passed'

    standard2 = baseCase_outcome()
    print "\t testing test case with winner " + str(standard2.winner)
    right_answer2 = baseCase_outcome_str()
    output2 = str(standard2)
    ct.assert_equals(right_answer2, output2)
    print '\t\t test passed'
    
    standard3 = unbalanced_outcome()
    print "\t testing test case with winner " + str(standard3.winner)
    right_answer3 = unbalanced_outcome_str()
    output3 = str(standard3)
    ct.assert_equals(right_answer3, output3)
    print '\t\t test passed'

def test_teams():
    """Test a4 Outcome teams() method"""
    print "Running " + inspect.stack()[0][3] # prints out this test method

    print "\t testing baseCase teams"
    base = baseCase_outcome().teams()
    right_answer = baseCase_outcome_teams()
    ct.assert_equals(right_answer, base)
    print '\t\t test passed'
    
    print "\t testing unbalancedCase teams"
    unbal = unbalanced_outcome().teams()
    right_answer1 = unbalanced_outcome_teams()
    ct.assert_equals(right_answer1, unbal)
    print '\t\t test passed'
    
    print "\t testing standardCase teams"
    stan = standard_outcome().teams()
    right_answer2 = standard_outcome_teams()
    ct.assert_equals(right_answer2, stan)
    print '\t\t test passed'
    
    print "\t testing duplicate teams"
    dupOutcome = Outcome(Outcome('Cornell','Harvard'), Outcome('Princeton','Cornell'))
    dup = dupOutcome.teams()
    right_answer3 = unbalanced_outcome_teams()
    ct.assert_equals(right_answer3, dup)
    print '\t\t test passed'

def test_path():
    """Test a4 Outcome pathToVictory method"""
    print "Running " + inspect.stack()[0][3] # prints out this test method

    print "\t testing baseCase path"
    base = baseCase_outcome().pathToVictory()
    right_answer = baseCase_outcome_path()
    ct.assert_equals(right_answer, base)
    print '\t\t test passed'
    
    print "\t testing unbalancedCase path"
    unbal = unbalanced_outcome().pathToVictory()
    right_answer1 = unbalanced_outcome_path()
    ct.assert_equals(right_answer1, unbal)
    print '\t\t test passed'
    
    print "\t testing standardCase path"
    stan = standard_outcome().pathToVictory()
    right_answer2 = standard_outcome_path()
    ct.assert_equals(right_answer2, stan)
    print '\t\t test passed'

def test_hasHeadToHead():
    """Test a4 Outcome hasHeadToHead method"""
    print "Running " + inspect.stack()[0][3] # prints out this test method

    #STUDENTS: We are providing some testing for the standard outcome for you.
    # You should think about whether you should add more test cases.
    outcome_standard = standard_outcome()
    test_cases = {
        ("Wisconsin", "Florida"): True, # no sub-outcomes
        # ("Florida", "Wisconsin"): True, # omit: we test both orders in for-loop
        ("Wisconsin", "Baylor"): False, # non-head2head teams in 1st sub-Outcome
        ("UCLA", "The Howling Fantods"): False, # team not in the tournament
        # STUDENTS: if you are adding more cases for the standard Outcome,
        # place them below this comment.
        ("Florida", "South Carolina"): True,
        ("Wisconsin", "South Carolina"): False
    }
    print "\t testing standardCase headToHead"
    for tc in test_cases:
        print "\t\t testing test case " + str(tc) + " in given order"
        output = outcome_standard.hasHeadToHead(tc[0], tc[1])
        ct.assert_equals(test_cases[tc], output)
        # test in other order
        print "\t\t testing test case " + str(tc) + " in reverse order"
        output = outcome_standard.hasHeadToHead(tc[1], tc[0])
        ct.assert_equals(test_cases[tc], output)
    
    
    outcome_unbalanced = unbalanced_outcome()
    test_cases2 ={
        ('Cornell','Harvard'): True,
        ('Princeton','Cornell'): True,
        ('Cornell','MIT'): False
    }
    print "\t testing unbalanced headToHead"
    for tc1 in test_cases2:
        print "\t\t testing test case " + str(tc1) 
        output1 = outcome_unbalanced.hasHeadToHead(tc1[0], tc1[1])
        ct.assert_equals(test_cases2[tc1], output1)


    outcome_baseCase = baseCase_outcome()
    test_cases3 = {
        ('Texas A&M','UT'): True,
        ('Texas A&M','UT Austin is a sorry excuse for a school'): False #True
        }
    print "\t testing baseCase headToHead"
    for tc2 in test_cases3:
        print "\t\t testing test case " + str(tc2) 
        output2 = outcome_baseCase.hasHeadToHead(tc2[0], tc2[1])
        ct.assert_equals(test_cases3[tc2], output2)
    
    

if __name__ == '__main__':
    test_init()
    test_teams()
    test_path()
    test_hasHeadToHead()
    print 'Finished running tests of A4'
