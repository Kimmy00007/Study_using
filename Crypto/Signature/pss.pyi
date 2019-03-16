from types import ModuleType
from typing import Union, Callable

from Crypto.PublicKey.RSA import RsaKey


class PSS_SigScheme:
    def __init__(self, key: RsaKey, mgfunc: Callable, saltLen: int, randfunc: Callable) -> None: ...
    def can_sign(self) -> bool: ...
    def sign(self, msg_hash: ModuleType) -> bytes: ...
    def verify(self, msg_hash: ModuleType, signature: bytes) -> None: ...

def MGF1(mgfSeed: bytes, maskLen: int, hash_gen: ModuleType) -> bytes: ...
def _EMSA_PSS_ENCODE(mhash: ModuleType, emBits: int, randFunc: Callable, mgf: Callable, sLen: int) -> str: ...
def _EMSA_PSS_VERIFY(mhash: ModuleType, em: str, emBits: int, mgf: Callable, sLen: int) -> None: ...
def new(rsa_key: RsaKey, **kwargs: Union[Callable, int]) -> PSS_SigScheme: ...