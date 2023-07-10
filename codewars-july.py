def likes(names):
    num = len(names)
    
    if num == 0:
        return "no one likes this"
    elif num == 1:
        return f"{names[0]} likes this"
    elif num == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        diff = num - 2
        return f"{names[0]}, {names[1]} and {diff} others like this"