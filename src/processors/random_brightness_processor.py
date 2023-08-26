class ImageProcesor:

    def __init__(self, img):
        self.img = img
    @abstractmethod
    def process(self):
        pass