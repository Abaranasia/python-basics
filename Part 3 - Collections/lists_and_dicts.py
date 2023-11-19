colors = ["white", "grey", "cyan", "green", "purple", "black"]
print(colors)


def insert_after(new_color, existing_color):
    # This function will insert a given color (newcolor) after an existing color

    start_position = colors.index(existing_color)
    colors.insert(start_position + 1, new_color)
    print(colors)


insert_after("yellow", "cyan")  # Should insert yellow between cyan and green

#####################################################################

items = [
    {"id": 11, "name": "aaa", "next": 22},
    {"id": 22, "name": "bbb", "next": 33},
    {"id": 33, "name": "zzz", "next": 999},
]

new_item = {"id": 23, "name": "ccc", "next": 0}


def print_object(item_id):
    for item in items:
        if item["id"] == item_id:
            print(item)


print_object(11)

#####################################################################


def insert_inbetween(new_item, previous_item_id):
    # This function will insert a given item inbetween two exisitng items and reconnect them
    print("Initial: ", items)
    previous_item = next(filter(lambda x: x["id"] == previous_item_id, items), None)
    # this code returns the previous item if found by its id or None if not

    if previous_item is not None:
        previous_item_position = items.index(previous_item)
        next_reference = previous_item[
            "next"
        ]  # We need to get the reference to the next item

        previous_item["next"] = new_item["id"]
        new_item["next"] = next_reference

        items.insert(previous_item_position + 1, new_item)

    print("after: ", items)


insert_inbetween(new_item, 22)  # Should insert the new item between 22 and 33
