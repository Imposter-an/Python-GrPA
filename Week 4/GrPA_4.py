def swap_halves(items):
    """Swap the first and second halves of a tuple with even length."""
    mid = len(items) // 2
    return items[mid:] + items[:mid]

def swap_at_index(items, k):
    """Break tuple at index k and swap the parts (element at k included in first half)."""
    return items[k+1:] + items[:k+1]

def rotate_k(items, k=1):
    """Rotate list elements k positions to the right."""
    if not items:
        return items
    
    # Handle cases where k is larger than list length
    k = k % len(items)
    
    # Take last k elements and put them at the beginning
    return items[-k:] + items[:-k]

def first_and_last_index(items, elem):
    """Get the indices of first and last occurrence of an element."""
    first_idx = items.index(elem)
    
    # Find last occurrence by searching from the end
    last_idx = len(items) - 1 - items[::-1].index(elem)
    
    return (first_idx, last_idx)

def reverse_first_and_last_halves(items):
    """Reverse the first and last halves of a list with even length in place."""
    mid = len(items) // 2
    
    # Reverse first half in place
    items[:mid] = items[:mid][::-1]
    
    # Reverse second half in place
    items[mid:] = items[mid:][::-1]