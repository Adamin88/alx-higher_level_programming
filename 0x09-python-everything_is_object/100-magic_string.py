def magic_string():
    if not hasattr(magic_string, "count"):
        magic_string.count = 0
    else:
        magic_string.count += 1
    return "BestSchool" + ", BestSchool" * magic_string.count

