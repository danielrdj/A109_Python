user_val = 0

cond_str = ''

if user_val < 0:
    cond_str = "negative"
else:
    cond_str = "non-negative"


print(user_val, 'is', cond_str)
