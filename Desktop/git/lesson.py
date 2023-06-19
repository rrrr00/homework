def count(s, char):
    counter = 0
    for i in range(len(s)):
        if s [i] == char:
            counter
    return counter

# def synbolCounter(s: str): 
#     for i in range(len(s)):
#         print(s.count(s[i]), s[i])

# def synbolCounter(s: str): 
#     for sym in set(s):
#         counter = 0
#         for i in s:
#             if sym == i:
#                 counter += 1
#         print(sym, counter)

def symbolCounter(s: str):
    syms_counter = {}
    for i in s:
        if syms_counter.get(i) is None:
            syms_counter[i] = 1
            continue
        syms_counter[i] += 1
    return syms_counter

print(synbolCounter(input()))