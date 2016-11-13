"""
@author:    TEKIN Abdurrahim Burak
@date:      2016-11-07
-- Addition of numbers with Threads (Locks) --
"""

# importing threading to be able to use Threads
import threading

num = int(input("Geben Sie bitte eine Zahl ein, bis zu der addiert werden soll!"))
# num_thread = input("Geben Sie die Anzahl der Threads ein!")
num_thread = 3

class SumThread(threading.Thread):
    """
    class for addition
    """
    lock = threading.Lock()

    counter = 0

    def __init__(self, num):
        """
        init method
        """
        threading.Thread.__init__(self)

        num = num


    def run(self):
        counter = 0

        for i in range(self.num):
            counter += i

        with SumThread.lock:
            SumThread.counter += counter

        print (SumThread.counter)


class Sum:
    def __init__(self, number, thread_num):
        """
        Splits the number into the amount of threads -> 3 Threads
        :param number:
        :param thread_num:
        """

        number = num

        thread_num = 3

        threads = []

        split = number / thread_num

        with SumThread.lock:
            SumThread.total = 0

        for i in range(thread_num):
            start = split * i
            end = start + split

            thread = SumThread(round(start), round(end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_num = SumThread.total
        print (end_num)

Sum()
