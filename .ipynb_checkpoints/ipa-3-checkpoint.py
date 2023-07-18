#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member in social_graph and to_member in social_graph:
        if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
            return "friends"
        elif to_member in social_graph[from_member]["following"]:
            return "follower"
        elif from_member in social_graph[to_member]["following"]:
            return "followed by"
    return "no relationship"


# In[3]:


social_graph = {
    "@bongolpoc": {
        "first_name": "Joselito",
        "last_name": "Olpoc",
        "following": []
    },
    "@joaquin": {
        "first_name": "Joaquin",
        "last_name": "Gonzales",
        "following": ["@chums", "@jobenilagan"]
    },
    "@chums": {
        "first_name": "Matthew",
        "last_name": "Uy",
        "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]
    },
    "@jobenilagan": {
        "first_name": "Joben",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]
    },
    "@joeilagan": {
        "first_name": "Joe",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@jobenilagan", "@chums"]
    },
    "@eeebeee": {
        "first_name": "Elizabeth",
        "last_name": "Ilagan",
        "following": ["@jobenilagan", "@joeilagan"]
    },
}
relationship_status("@joaquin", "@bongolpoc", social_graph)


# In[4]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    n = len(board)

    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    # Check columns
    for col in range(n):
        if len(set(board[row][col] for row in range(n))) == 1 and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if len(set(board[i][i] for i in range(n))) == 1 and board[0][0] != '':
        return board[0][0]
    if len(set(board[i][n - 1 - i] for i in range(n))) == 1 and board[0][n - 1] != '':
        return board[0][n - 1]

    return "NO WINNER"


# In[5]:


board1 = [
    ['X','X','O'],
    ['O','X','O'],
    ['O','','X'],
]

board2 = [
    ['X','X','O'],
    ['O','X','O'],
    ['','O','X'],
]

board3 = [
    ['O','X','O'],
    ['','O','X'],
    ['X','X','O'],
]

board4 = [
    ['X','X','X'],
    ['O','X','O'],
    ['O','','O'],
]

board5 = [
    ['X','X','O'],
    ['O','X','O'],
    ['X','','O'],
]

board6 = [
    ['X','X','O'],
    ['O','X','O'],
    ['X','',''],
]

board7 = [
    ['X','X','O',''],
    ['O','X','O','O'],
    ['X','','','O'],
    ['O','X','',''],
]
tic_tac_toe(board4)


# In[6]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        next_stop = None
        for leg in route_map:
            if leg[0] == current_stop:
                next_stop = leg[1]
                total_time += route_map[leg]['travel_time_mins']
                break

        if next_stop is None:
            return -1  # No valid route found

        current_stop = next_stop

    return total_time


# In[7]:


legs = {
    ("upd", "admu"): {
        "travel_time_mins": 10
    },
    ("admu", "dlsu"): {
        "travel_time_mins": 35
    },
    ("dlsu", "upd"): {
        "travel_time_mins": 55
    }
}
eta("dlsu", "upd", legs)


# In[ ]:




