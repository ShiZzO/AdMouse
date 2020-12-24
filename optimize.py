import time
input_filename = "filter.txt"
output_filename_success = "result.txt"
output_filename_delete = "delete.txt"

cache = {}

def load_file(input_filename):
    items = []
    start_time = time.time()
    print("Read file")
    with open(input_filename, "r") as file:
        content = file.read().split("\n")
        for cont in content:
            if(cont.strip() != ""):
                items.append(cont)
    print("Read complete. Time:", time.time() - start_time, "c")
    return items

def sorted_list(items):
    start_time = time.time()
    print("Sort")
    sorted_item = sorted(items, key=lambda x: len(x.split(".")))
    print("Sort complete. Time:", time.time() - start_time, "c")
    return sorted_item

def get_cache(item):
    try:
        current_item = cache[item]
        return True
    except Exception as e:
        print(item, "not found in cache")
        return False

def get_join(items):
    return '.'.join(items)

def processing_all(items):
    print("Processing")
    start_time = time.time()
    for item in items:
        processing(item)
    print("Complete. Time:", time.time() - start_time, "c")


def processing(item):
    print("Processing ", item)

    blocks = item.split(".")
    if(len(blocks) == 2):
        save(item, output_filename_success)
        cache[item] = item
    else:
        for index in range(len(blocks) - 1).__reversed__():
            print(get_join(blocks[index:]))
            if(get_cache(get_join(blocks[index:]))):
                save(item, output_filename_delete)
                print(item, "Deleted")
                return
            else:
                continue

        save(item, output_filename_success)
        cache[item] = item
        
def save(item, filename):
    with open(filename, "a") as file:
        file.write(item + "\n")

if __name__ == '__main__':
    start_time = time.time()
    items = load_file(input_filename)
    items = sorted_list(items)
    processing_all(items)