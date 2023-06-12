import Core.Persistence.PersistenceModels.ExecResultModel
import Core.Persistence.ResultPersistence
from Core.ExecController import ExecController


class ExecContext():
    """Open a context manager for a more standardized test and result file creation.
    
    overwrite - Indicates whether the result file to be created will overwrite/create the entire file (if True) or be included at the end of an existing file (if False).
    """
    def __init__(self, exec_controller: ExecController, filename: str) -> None:
        self.exec_controller = exec_controller
        self.persistence = Core.Persistence.ResultPersistence.ResultPersistence(self.exec_controller, filename)

    def __enter__(self):
        return self.exec_controller

    def __exit__(self, *exc_info):
        self.persistence.save()
        self.persistence.close()
