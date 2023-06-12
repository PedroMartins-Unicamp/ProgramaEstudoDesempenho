from Core.Persistence.PersistenceModels.ExecResultModel import result_text

class ResultPersistence:
    def __init__(self, exec_controller, filename: str):
        self.exec_controller = exec_controller
        self._path = ""
        
        if self.exec_controller.target_model == "Ordered":
            self._path = f"./Results/Ordered/[Result]{filename}.txt"

        elif self.exec_controller.target_model == "Reverse":
            self._path = f"./Results/Reverse/[Result]{filename}.txt"

        elif self.exec_controller.target_model == "Random":
            self._path = f"./Results/Random/[Result]{filename}.txt"

        else: self._path = f"./Results/Unknown/[Result]{filename}.txt"

        self.file = open(self._path, "w+")


    def save(self) -> None:
        self.file.write(result_text(self.exec_controller))
        pass

    def close(self) -> None:
        self.file.close()
    
