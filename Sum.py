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

    # num_thread = input("Geben Sie die Anzahl der Threads ein!")
    num = int(input("Geben Sie bitte eine Zahl ein, bis zu der addiert werden soll!"))

    lock = threading.Lock()

    counter = 0

    def __init__(self):
        """
        init method
        """
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.num):
            with SumThread.lock:

                curValue = SumThread.counter
                SumThread.counter = curValue


class Sum:
    pass