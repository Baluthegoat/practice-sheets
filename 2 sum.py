
        dict_of_seen_values = {}   
        for idx, value in enumerate(nums):
            required_number = target - value   
            if required_number in dict_of_seen_values:
                return [dict_of_seen_values[required_number], idx]   
                
            dict_of_seen_values[value] = idx  
nums = [2,7,11,15]
print(idx)