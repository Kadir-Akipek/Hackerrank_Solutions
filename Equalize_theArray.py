from collections import Counter

def equalizeArray(arr):
    narr = Counter(arr)
    mrn = max(narr.values())
    
    return len(arr) - mrn

