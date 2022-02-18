import json


def parse_json(file):
    """
    A function to parse JSON file
    returns obtained data
    file -> Dict
    """
    data = None
    with open(file) as f:
        data = json.load(f)
    return data


def find_element_by_key(data_object, element):
    """

    """
    if element in data_object:
        print(f"- {element}: {data_object[element]}")
    for _, value in data_object.items():
        if isinstance(value, dict):
            find_element_by_key(value, element)
        elif isinstance(value, list) and len(value) > 0:
            for list_object in value:
                if isinstance(list_object, dict):
                    find_element_by_key(list_object, element)
        else:
            continue


def prind_object(data_object):
    counter = 1
    for element in data_object:
        print(f"{counter}. {element}")
        counter += 1
        

def main():
    print("Please write a route to a file: ")
    print(">>> ", end="")
    try:
        data = parse_json(input())
    except FileNotFoundError:
        print("File does not exists!")
        main()
    print(f"There are {len(data)} objects in your json file")
    print(f"- To find some value of a key, write a number of object you want to search in (0-{len(data) - 1})")
    print("- To navigate thought all of them, write \"Navigate\"")
    print("- To exit, write\"Exit\"")
    while True:
        print("Write a command: ")
        print(">>> ", end="")
        response = input()
        if response.isnumeric():
            if int(response) < 0 or int(response) >= len(data):
                print("There is not an object with this index, try something else!")
                continue
            number_of_object = int(response)
            print("Good, which key you want to get?")
            print(">>> ", end="")
            key = input()
            find_element_by_key(data[number_of_object], key)
            print("Those are values that were found")
        elif response.lower() == "navigate":
            for i in range(len(data)):
                if isinstance(data[i], dict):
                    print(str(i) + ". {}")
            print(f"Choose an object (0-{len(data) - 1})")
            print(">>> ", end="")
            object_number = input()
            if object_number.isnumeric():
                object_number = int(object_number)
                print("Keys: ")
                prind_object(data[object_number])
        elif response.lower() == "exit":
            break


        
    # result = find_element_by_key(data[0], "indices")


if __name__ == '__main__':
    main()