def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)

user_input = input("Գրեք թվերի ցանկը")
numbers = [int(num) for num in user_input.split()]

exclude = input("Ուզում եք բացառել բացասական թվերը? (այո/ոչ):")
exclude_negative = exclude == 'այո'

total_sum = sum_of_elements(numbers, exclude_negative)
print("Թվերի գումարը (բացառելով բացասականը):", total_sum)
