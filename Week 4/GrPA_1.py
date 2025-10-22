# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <nofor>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# The values of the below variables will be changed by the evaluator
int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple 

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# <nofor>
# <eoi>

#Write your code below this line
# --- Empty collections ---

empty_list = []
empty_set = set()
empty_tuple = ()

# --- Singleton collections ---
singleton_list = [42]
singleton_set = {42}
singleton_tuple = (42,)

# --- Truthiness ---
a_falsy_list = []          # falsy
a_falsy_set = set()        # falsy
a_truthy_tuple = (0,)      # truthy (non-empty)

# --- int_iterable calculations (dynamic, no loops) ---
int_iterable_min = min(int_iterable)
int_iterable_max = max(int_iterable)
int_iterable_sum = sum(int_iterable)
int_iterable_len = len(int_iterable)
int_iterable_sorted = sorted(int_iterable)
int_iterable_sorted_desc = sorted(int_iterable, reverse=True)

# --- Reversal ---
if hasattr(int_iterable, "__reversed__"):
    int_iterable_reversed = list(reversed(int_iterable))
else:
    int_iterable_reversed = list(reversed(sorted(int_iterable)))

# --- Indexing ---
if isinstance(some_collection, (list, tuple, range, str)):
    third_last_element = some_collection[-3]
else:
    third_last_element = None

# --- Slicing ---
if isinstance(some_collection, (list, tuple, range, str)):
    odd_index_elements = some_collection[1::2]
else:
    odd_index_elements = None

# --- Membership ---
is_some_value_in_some_collection = some_value in some_collection

# --- Even index check (no loops) ---
if isinstance(some_collection, (list, tuple, range, str)):
    is_some_value_in_even_indices = some_value in some_collection[::2]
else:
    is_some_value_in_even_indices = None

# --- Combine all iterables ---
all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable)

# --- String concatenation (corrected) ---
if isinstance(string_iterable, (list, tuple)):
    all_concat = "-".join(string_iterable)
else:
    all_concat = "-".join(sorted(string_iterable))