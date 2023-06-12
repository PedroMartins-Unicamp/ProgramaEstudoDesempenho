from Core.Resources.ExecTime import get_time
from datetime import datetime
from collections import namedtuple

class ExecController():
    def __init__(self, target: list, 
                 target_model: str, algorithm, 
                 repetitions: int=1) -> None:


        self.target = target
        self.target_model = target_model
        self.target_size = len(self.target)
        self.algorithm = algorithm
        self.repetitions = repetitions
        self.date = datetime.now()
        self.results = []

        self.successfully_executed = False

        self._progress = 0


    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
        print(f"Progress: {self._progress}/{self.repetitions}")


    def run(self):
        if self.target_model == "Random":
            Result = namedtuple("Result", ["test_number", "exec_time"])
            self.repetitions = len(self.target)
            self.target_size = len(self.target[0])
            while self._progress < self.repetitions:
                lst = self.target[self._progress].copy()

                exec_time = get_time(self.algorithm, lst)
                self.progress += 1

                self.results.append(Result(self._progress, exec_time))


            self.successfully_executed = True
        
        else:        
            Result = namedtuple("Result", ["test_number", "exec_time"])

            while self._progress < self.repetitions:
                lst = self.target.copy()

                exec_time = get_time(self.algorithm, lst)
                self.progress += 1

                self.results.append(Result(self._progress, exec_time))


            self.successfully_executed = True
