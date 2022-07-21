

original_list = [1, 1, 1, 3, 7, 7, 9]
# expected_result = [1, 3, 7, 9]

def remove_duplicates(duplicate_list):
    final_list = []
    for item in duplicate_list:
        if item not in final_list:
            final_list.append(item)
    return final_list

print(remove_duplicates(original_list))