import random

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


# end def bfs_connected_component(graph, start):

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        #return "That was easy! Start = goal"
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
    return []

def friend_of_friend_finder(graph, entrant):
    print("Hi, {0}!".format(entrant))
    # find friend to suggest
    for f in graph[entrant]:
        for ff in graph[f]:
            # check if this friend of friend is not already direct friend
            if ff not in graph[entrant]:  # not already friends
                print("You should be friends with {0} becuase {1} is.".format(ff, f))
#end def friend_of_friend_finder(graph, entrant):

def most_popular(graph):
    pop = None #Issue will return None if none have friends.
    most = 0
    for k in graph.keys():
        if len(graph[k]) > most:
            most  = len(graph[k])
            pop = k
    return pop
#end def most_popular(graph):


def main():
    # graph = { "1" : ["2", "5"],
    #           "2" : ["1", '2', '5'],
    #           "3" : ["2", "4"],
    #           "4" : ["3", "5", "6"],
    #           "5" : ["1", "2", "4"],
    #           "6" : ["4"]
    #         }

    # graph = {"1": ["2", "3", "4"],
    #          "2": ["4", "5"],
    #          "3": ["6"],
    #          "4": ["3", "6", "7"],
    #          "5": ["4", "7"],
    #          "6": [],
    #          "7": ["6"]
    #          }

    graph = {"alice": ["bob", "esther"],
             "fanny": ["bob", "charlie"],
             "esther": ["fanny", "david"],
             "david": ["alice"],
             "charlie": ["bob", "esther"],
             "bob": ["charlie"]
             }

    entrant = 'alice'

    rani = random.randrange(0, len(graph.keys()))   #get valid index to keys of dict
    randp = list(graph.keys())[rani]

    print("Random person chosen is ", randp)
    #issue will arise if randp is entrant

    #
    # "

    path = bfs_shortest_path(graph, entrant, randp)

    if len(path) == 0: #if there is no way for these two to be friends
        #check if entrant has friends
        if len(graph[entrant]) == 0: # if not
            #find most popular person and suggets this person to them.
            sugg = most_popular(graph)
            reason = "They do not seem to care who they are friends with."
    elif len(path) < 3: #thses people are already friends, use random info.
        sugg = randp  # suggesting random person for no reason so far
        reason = "we need money."
    elif len(path) == 3: #mutuall friend of friend
        #since we get shortest path, target should not be friend of entrant
        sugg = path[2] #0 is entrant 1 is mutual and 2 is target
        reason = "you are both friends with " + path[1]
    else:
        #longer path tot freindship so pick closest person.
        #this is really the cas above, but we can also suggest
         # to target that they become friend of someone to step closer.

        #first sufggest nest closest perrson to entrant
        sugg_in = path[2] #0 is entant 1 is mutual and 2 is target
        reason_in = "you are both friends with " + path[1]
        print("Dear", target,  "befriend", sugg_in, "because", reason_in)

    print("Dear", entrant, "befriend", sugg, "because", reason)

    #print("Befriend", sugg,"because",reason)
    # print(bfs_connected_component(graph, '6'))
    # print(bfs_shortest_path(graph, '1', '2'))
    # print(bfs_shortest_path(graph, '2', '6'))
    # print(bfs_shortest_path(graph, '1', '6'))

    # path = bfs_shortest_path(graph, 'fanny', 'david')
    #path = bfs_shortest_path(graph, 'charlie', 'david')
    # path = bfs_shortest_path(graph, 'david', 'charlie')
    #
    # if len(path) > 2:
    #     print("Not friends, but they could be if you involve", path[1:-1])
    # else:
    #     print("Friends")

    #friend_of_friend_finder(graph, "alice")
    # entrant = 'alice'
    # print("Hi, {0}!".format(entrant))
    # #find friend to suggest
    # for f in graph[entrant]:
    #     for ff in graph[f]:
    #         #check if this friend of friend is not already direct friend
    #         if ff not in graph[entrant]: #not already friends
    #             print("You should be friends with {0} becuase {1} is.".format(ff,f))

# end def main():

if __name__ == "__main__":
    main()
