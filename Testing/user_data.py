import json


def open_json_file(file_name):
    with open(file_name, "r") as f:
        return json.load(f)


def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(item) is dict:
            for key in item:
                data[key] = item[key]

    return data


def final_transform(transformed_data):
    """
    Transform address structures into a single structure
    """
    transformed_data['address'] = str.format(
        "{0}\n{1}, {2} {3}", transformed_data['street'],
        transformed_data['state'], transformed_data['city'],
        transformed_data['zip'])

    return transformed_data


def print_person(person_data):
    parents = "and".join(person_data['relationships']['parents'])
    siblings = "and".join(person_data['relationships']['siblings'])
    person_string = str.format(
        "Hello, my name is {0}, my siblings are {1}, "
        "my parents are {2}, and my mailing"
        "address is: \n{3}",
        person_data['name'],
        parents,
        siblings,
        person_data['address'])
    print(person_string)


if __name__ == "__main__":
    john_data = open_json_file("john_data.json")
    suzy_data = open_json_file("suzy_data.json")

    inputs = [suzy_data, suzy_data]
    for input_structure in inputs:
        initial_transformed = initial_transform(input_structure)
        final_transformed = final_transform(initial_transformed)
        print_person(final_transformed)