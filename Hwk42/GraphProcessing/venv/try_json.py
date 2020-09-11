import json as js


# graph = { "omaha"    	: ["dallas", "houston"],
#         "louisville" 	: ["dallas", "houston", "baltimore", "chicago"],
#         "baltimore"  	: ["jacksonville", "houston", "dallas", "chicago"],
#         "portland"   	: ["baltimore"],
#         "jacksonville"  : ["dallas", "houston", "baltimore", "chicago"],
#         "belize city"   : [],
#         "dallas"  		: ["houston", "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
#         "houston"  		: ["dallas",  "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
#         "chicago"		: ["dallas",  "baltimore", "jacksonville", "louisville", "omaha"]
#         }

graph = {"omaha"        : ["dallas", "houston"],
          "louisvie" 	: ["dallas", "houston", "baltimore", "chicago"],
          "baltim"  	: ["jacksonville", "houston", "dallas", "chicago"],
          "portland"   	: ["baltimore"],
          "jacksonvie"  : ["dallas", "houston", "baltimore", "chicago"],
          "belize city" : [""],
          "dallas"  	: ["houston", "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
          "houston"  	: ["dall ",  "baltimore", "jacksonville", "louisville", "chicago", "omaha"],
          "chico"		: ["dall ",  "baltimore", "jacksonville", "louisville", "omaha"]

}


graphjs = js.dumps(graph)

json_object = js.loads(graphjs)

json_formatted_str = js.dumps(json_object, indent=2)

print(json_formatted_str)

print (graphjs)