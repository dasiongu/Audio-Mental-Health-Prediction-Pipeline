from sklearn.svm import SVC
from .ml_model_base import MLModel

class SVM(MLModel):
    def __init__(self, params_file):
        super().__init__(SVC, params_file)