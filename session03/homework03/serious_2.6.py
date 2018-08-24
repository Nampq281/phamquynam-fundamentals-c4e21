
flock_sheep = [5, 7, 300, 90, 24, 50, 75]
print ("Hello, my name is Nam, and here are my ship sizes ", flock_sheep)

n = 3
for i in range(n):
    print("MONTH ", i+1)
    growth = 50
    for y in range(len(flock_sheep)):
        flock_sheep[y] += growth
    print ("One month has passed, now here is my flock ", flock_sheep)

    biggest = max(flock_sheep)
    print ("Now my biggest sheep has size ", biggest, "let's sheer it")

    sheep_no = flock_sheep.index(biggest)
    flock_sheep[sheep_no] = 8
    print ("After sheering, here is my flock ", flock_sheep)
price = 2
total_size = 0
for i in range(len(flock_sheep)):
    total_size += flock_sheep[i]
print("My flock has size in total:", total_size)
print("I would get ", total_size, "* ",price,"= ", total_size*price)