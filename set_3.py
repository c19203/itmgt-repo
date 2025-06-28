'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
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
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    from_follow_list = social_graph[from_member]["following"] #list of people that from_member follows
    to_follow_list = social_graph[to_member]["following"] #list of people that to_member follows
       
    #if to_member is in the follow list of from_member AND from_member is in the follow list of to_member
    if to_member in from_follow_list and from_member in to_follow_list:  
        return "friends"
    
    #if to_member is in the follow list of from_member
    elif to_member in from_follow_list: 
        return "follower"
    
    #if from_member is in the follow list of to_member
    elif from_member in to_follow_list: 
        return "followed by"
        
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
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

    # check if there's a win among the rows
    for row_list in board: 
        x_row_count = 0 
        o_row_count = 0

        for row_symbol in row_list:
            if row_symbol == "X":
                x_row_count += 1
            elif row_symbol == "O":
                o_row_count += 1
    
        if x_row_count == n:
            return "X"
        elif o_row_count == n:
            return "O"

    # check if there's a win among the columns
    for col_index in range(n):
        col_list = [board[row_index][col_index] for row_index in range(n)]
        x_col_count = 0
        o_col_count = 0

        for col_symbol in col_list:
            if col_symbol == "X":
                x_col_count += 1
            elif col_symbol == "O":
                o_col_count += 1

        if x_col_count == n:
            return "X"
        elif o_col_count == n:
            return "O"
            
    # check if there's a win among the diagonals 
    x_diag1_count = 0 
    o_diag1_count = 0
    for diag1_index in range(n): 
        diag1_symbol = board[diag1_index][diag1_index] 
       
        if diag1_symbol == "X":
            x_diag1_count += 1
        elif diag1_symbol == "O":
            o_diag1_count += 1
    
    if x_diag1_count == n:
        return "X"
    elif o_diag1_count == n:
        return "O"
    
    x_diag2_count = 0
    o_diag2_count = 0
    for diag2_index in range(n): 
        diag2_symbol = board[diag2_index][n-diag2_index-1]
        
        if diag2_symbol == "X":
            x_diag2_count += 1
        elif diag2_symbol == "O":
            o_diag2_count += 1
    
    if x_diag2_count == n:
        return "X"
    elif o_diag2_count == n:
        return "O"
    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
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
    
    total_time = 0
    destination_reached = False

    while not destination_reached: #keep looping while destination_reached = False
        for key in route_map:
            from_stop = key[0]
            to_stop = key[1]
            travel_time = route_map[key]["travel_time_mins"]

            #check if first_stop starts at the from_stop
            if from_stop == first_stop: 
                
                # check if to_stop is the destination
                if to_stop == second_stop: 
                    total_time += travel_time
                    destination_reached = True 
                    
                # if to_stop is not yet the destination, update the time and the type of stop
                else: 
                    total_time += travel_time
                    first_stop = to_stop  
                    
                break  # move on to the next stop

    return total_time