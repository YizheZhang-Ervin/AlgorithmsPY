from DataStructure.queue import Queue
import random


class Printer:
    def __init__(self, ppm):
        # 打印速度
        self.pagerate = ppm
        # 打印任务
        self.currentTask = None
        # 打印倒计时
        self.timeRemaining = 0

    # 打印1s
    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 判断打印是否繁忙
    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    # 打印新任务
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        # 打印时间戳
        self.timestamp = time
        # 打印页数
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    # 等待时间
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    # 时间流逝
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    # 1/180概率生成作业(实际:每小时要打印20个任务20/3600)
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)
