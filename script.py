# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure.
# 
# Arguments: 
#   string_input: block of text containing the network information
# Return:
#   The newly created network data structure
def get_one(text):
    index1=text.find('is connected to ')
    index2=text.find('.')
    index3=text.find('play ')
    index4=text.find('.',index3-1)
    the_one=text[:index1-1]
    people_string=text[index1 + len('is connected to '):index2]
    name=people_string.split(', ')
    game_string=text[index3+len('play ') : index4]
    game=game_string.split(', ')
    return the_one,[name,game],index4

def create_data_structure(text):
    #{name1: [[name2,name3,,,],[game1,game2,,]],,}
    network={}
    while text.find('is connected')!=-1:
        result=get_one(text)
        network[result[0]]=result[1]
        text=text[result[2]+1:]
    return network
# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network,user):
    if user not in network:
        return None
    return network[user][0]
# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user not in network:
        return None
    return network[user][1]
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if (user_A not in network) or (user_B not in network):
        return False
    if user_B not in network[user_A][0]:
        network[user_A][0].append(user_B)
    return network
# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games,
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
def add_new_user(network, user, games):
    if not user in network:
        network[user]=[[],games]
    return network
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.

def get_secondary_connections(network, user):
    result=[]
    if not user in network:
        return None
    if network[user][0] == []:
        return []
    for name in network[user][0]:
        if network[name][0] !=[]:
            for name2 in network[name][0]:
                result.append(name2)
    return result
# -----------------------------------------------------------------------------     
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if (user_A not in network) or (user_B not in network):
        return False
    count=0
    for name in network[user_A][0]:
        if name in network[user_B][0]:
            count=count+1
    return count
# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#

checked=[]
def find_path_to_friend(network, user_A, user_B):
    # your RECURSIVE solution here!
    if (user_A not in network) or (user_B not in network):
        return None
    if user_B in network[user_A][0]:
        checked=[]
        return [user_A]
    else: 
        i=0
        while i<len(network[user_A][0]) and (network[user_A][0][i] in checked):
            i=i+1
        if i == len(network[user_A][0]):
            return None
        else:
            checked.append(user_A)
            return [user_A]+find_path_to_friend(network, network[user_A][0][i], user_B)
            