
one = 'appendix expose ensure salon north'.split()
two = 'food forethought muscle stadium'.split()


# подключаем модуль time
import time

# фиксируем время старта работы кода
start = time.process_time()


print(any(list(map(lambda w: w[-5:].lower() == 'ought', one))))
print(any(list(map(lambda w: w[-5:].lower() == 'ought', two))))
#фиксируем время окончания работы кода
finish = time.process_time()

# вычитаем время старта из времени окончания и выводим результат
print('Время работы: ' + str(finish - start))


print('2222222222')

# подключаем модуль time
import time

# фиксируем время старта работы кода
start = time.process_time()


print(any(word.endswith('ought') for word in one))
print(any(word.endswith('ought') for word in two))
#фиксируем время окончания работы кода
finish = time.process_time()

# вычитаем время старта из времени окончания и выводим результат
print('Время работы: ' + str(finish - start))