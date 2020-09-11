def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    # if not graph.has_key(start):
    #     return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    # if not graph.has_key(start):
    #     return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


graph = {"omaha"        : ["dallas", "houston"],
         "louisvie"     : ["dallas", "houston", "baltimore", "chicago"],
          "baltim"  	: ["jacksonville", "houston", "dallas", "chicago"],
          "portland"   	: ["baltimore"],
          "jacksonvie"  : ["dallas", "houston", "baltimore", "chicago"],
          "belize city" : [""],
          "dallas"  	: ["houston", "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
          "houston"  	: ["dall ",  "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
          "chico"		: ["dall ",  "baltimore", "jacksonville", "louisville", "omaha"]
        }


def main():
    find_shortest_path(graph, 'omaha', 'Louisville')

if __name__ == "__main__":
    main()
