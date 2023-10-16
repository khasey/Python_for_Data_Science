def all_thing_is_obj(object: any) -> int:
    # Identify the type of the object
    obj_type = type(object)
    
    # Print the appropriate message based on the object's type
    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    elif obj_type == str:
        print(f"Brian is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    # Return 42
    return 42
