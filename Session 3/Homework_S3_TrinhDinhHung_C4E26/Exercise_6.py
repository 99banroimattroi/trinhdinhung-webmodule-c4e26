from Exercise_4 import river_collection


if __name__=="__main__":

    America= []
    America_list = river_collection.find(
        {
            "continent": "S. America",
            "length": {"$lt": 1000}
        }
    )
    for i in America_list:
        new_list = {
            "name" : i["name"],
            "continent": i["continent"],
            "length": i["length"]
        }
        America.append(new_list)


    print(America)