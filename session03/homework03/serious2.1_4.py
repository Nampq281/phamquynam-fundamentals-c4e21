
flock_sheep = [5, 7, 300, 90, 24, 50, 75]
print ("Hello, my name is Nam, and here are my ship sizes ", flock_sheep)

biggest = max(flock_sheep)
print ("Now my biggest sheep has size ", biggest, "let's sheer it")

sheep_no = flock_sheep.index(biggest)
flock_sheep[sheep_no] = 8
print ("After sheering, here is my flock ", flock_sheep)

growth = 50
for i in range(len(flock_sheep)):
    flock_sheep[i] += growth
print ("One month has passed, now here is my flock ", flock_sheep)