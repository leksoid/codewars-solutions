def descending_order(num):
    digits = [int(each) for each in str(num)] 
    result = ""
    for each in sorted(digits, reverse=True):
        result += str(each)
    return int(result)