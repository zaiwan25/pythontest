import multiprocessing as mp


def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_process = mp.Process(target=dryer, args=(dish_queue,))
    dryer_process.daemon = True
    dryer_process.start()
    dish_list = ['salad', 'bread', 'entree', 'dessert']
    washer(dish_list, dish_queue)
    dish_queue.join()