def resize_list(lst, new_size: int, default_value= None) -> list:
    current_size = len(lst)
    
    if new_size > current_size:
        lst.extend([default_value] * (new_size - current_size))
    elif new_size < current_size:
        del lst[new_size:]
    
    return lst