"""
@author:    TEKIN Abdurrahim Burak
@date:      2016-11-07
-- Addition of numbers with Threads (Locks) --
"""

# importing threading to be able to use Threads
import threading

class SumThread(threading.Thread):
    """
    class for addition
    """

    lock = threading.Lock()
    counter = 0
    summe = 0

    def __init__(self, num, thread_num):
        """
        init method
        """
        threading.Thread.__init__(self)
        self.num = num
        self.thread_num = thread_num

    def run(self):
        for i in range(self.num):
            with SumThread.lock:
                wert = SumThread.counter
                SumThread.summe += wert
                SumThread.counter = wert + 1

        print (SumThread.counter)


class Sum:
    def __init__(self):
        """
        Splits the number into the amount of threads -> 3 Threads
        :param number:
        :param thread_num:
        """

        threads = []
        number = int(input("Geben sie eine Zahl ein!"))
        num_thread = 3
        split = number / num_thread

        with SumThread.lock:
            SumThread.total = 0

        for i in range(num_thread):
            thread = SumThread(split, i)
            threads += [thread]
            thread.start()

        for thread in threads:
            thread.join()

        end_num = SumThread.total
        print (end_num)

Sum()