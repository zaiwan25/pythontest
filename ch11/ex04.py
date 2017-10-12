# 리스트 컴프리헨션
even_nums = [num for num in range(10) if num % 2 == 0]
print(even_nums)

# 딕셔너리 컴프리헨션
squares = {num: num * num for num in range(10)}
print(squares)

# 셋 컴프리헨션
odd_nums = {num for num in range(10) if num % 2}
print(odd_nums)

# 제너레이트 컴프리헨션
gots = (word for word in 'gots ')
nums = (num for num in range(6))
print(gots)
print(nums)

def get_odds(idx):
    odds = [num for num in range(10) if (num % 2 == 1)]
    return odds[idx - 1]

print(get_odds(3))