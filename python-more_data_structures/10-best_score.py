#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dict = sorted(a_dictionary.items(), key=lambda x:x[1])
        return(new_dict[-1][0])
    else:
        return None
