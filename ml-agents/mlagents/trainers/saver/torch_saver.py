from mlagents.trainers.saver.saver import Saver

class TorchSaver(Saver):
    """
    Saver class for PyTorch
    """

    def __init__(self):
        self.modules = {}

    def register(self, name, module):
        pass
    
    def save_checkpoint(self):
        pass

    def maybe_load(self):
        pass

    def export(self):
        pass