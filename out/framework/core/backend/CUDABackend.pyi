from cupyx.scipy import sparse as sparse
from framework.core.backend import Backend as Backend, CUDA_HOME as CUDA_HOME

class CUDABackend(Backend):
    def __getattribute__(self, name) -> None: ...
    @staticmethod
    def kron(a, b): ...
    @staticmethod
    def dot(a, b): ...
    @staticmethod
    def eye(n, m): ...
    @staticmethod
    def matrix(a): ...
    @staticmethod
    def nonzero(a): ...