import time

start = time.time()

num_input = int(input("Enter a number: "))

prime_list = []



if (num_input > 10000):
    print("Please enter a number less than 10,000")

else:

    for num in range(1, num_input + 1):
   
        if num > 1:

            for i in range(2, num):

                if (num % i) == 0:

                    break
            else:
    
                prime_list.append(num)


print(prime_list)

print("--- %s seconds ---" % (time.time() - start))