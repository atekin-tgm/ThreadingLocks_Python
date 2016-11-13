"""
@author:    TEKIN Abdurrahim Burak
@date:      2016-11-07
-- Addition of numbers with Threads (Locks) --
"""

# importing threading to be able to use Threads
import threading

# inputs for number and amount of threads
num = int(input("What is your chosen number?"))
num_thread = int(input("How many Threads do you want?"))

class SumThread(threading.Thread):
    """
    class for counting with the run-method
    """
    lock = threading.Lock()
    counter = 0

    def __init__(self, num, thread_num):
        """
        init method
        """
        threading.Thread.__init__(self)
        self.num = num
        self.thread_num = thread_num

    # run-method for counting up
    def run(self):
        counter2 = 0
        for i in range(int(self.num + 1), self.thread_num + 1):
            counter2 += i

        with SumThread.lock:
            SumThread.counter += counter2


class Sum:
    def __init__(self):
        """
        Splits the number into the amount of threads and gives everything needed to SumThread
        :param number:
        :param thread_num:
        """

        threads = []

        # number gets splittet by amount of threads
        split = num / num_thread

        # start and end is defined -> SumThread
        for i in range(num_thread):
            start = i * split
            end = start + split

            thread = SumThread(round(start), round(end))
            threads += [thread]
            thread.start()

        for thread in threads:
            thread.join()

        # printing the result
        print ("=================================")
        print ("Number: " + str(num))
        print ("Threads: " + str(num_thread))
        print ("Result: " + str(SumThread.counter))

Sum()