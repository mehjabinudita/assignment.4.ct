def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count

while True:
    user_input = input("Enter a positive integer: ")
    
    if user_input.lower() == 'done':
        print("bye !!")
        break
    
    try:
        num = int(user_input)
        if num > 0:
            result = num_divide3(num)
            print(f"Numbers divisible by 3 from 1 to {num}: {result}")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a positive integer.")
