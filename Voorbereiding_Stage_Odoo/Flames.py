#Approach: Take two names as input then remove the common characters with their respective common occurrences. 
# For removing purpose we create a user-defined function with two arguments as list1 and list2 which stores list of characters of two players name respectively and return list of concatenated list(list1 + "*" flagst2) and flag value which we store in ret_list variable.
# After removing all the common characters, count the total no. of remaining characters then create a result list with FLAMES acronym 
# i.e ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]. 
# Now start removing word one by one until list does not contain only one word, using the total count which we got. 
# the word which remains in the last, is the result.

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return list3, True

    list3 = list1 + ["*"] + list2
    return list3, False


if __name__ == "__main__":
    player1 = input("Enter the name of player 1: ").lower().replace(" ", "")
    p1_list = list(player1)
    
    player2 = input("Enter the name of player 2: ").lower().replace(" ", "")
    p2_list = list(player2)
    
    flag = True
    
    while flag:
        
        return_list = remove_match_char(p1_list, p2_list)
        
        concatinated_list = return_list[0]
        
        flag = return_list[1]
        
        star_index = concatinated_list.index("*")
        
        p1_list = concatinated_list[: star_index]
        
        p2_list = concatinated_list[star_index + 1 :]
        
    count_remaining_chars = len(p1_list) + len(p2_list)
        
    result_list = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        
    while len(result_list) > 1:
        split_index = (count_remaining_chars % len(result_list) -1)
        
        if split_index >= 0:
            right = result_list[split_index + 1:]
            left = result_list[: split_index]
            
            result_list = right + left
        else:
            result_list = result_list[: len(result_list) -1]  
    
    print("Relationship status is: ", result_list[0])