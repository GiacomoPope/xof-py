import sys

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    Buffer = bytes | bytearray | memoryview

class Shake128:
    def __init__(self, input_bytes: Buffer | None = None):
        ...

    def absorb(self, input_bytes: Buffer) -> "Shake128":
        ...

    def finalize(self) -> Sponge128:
        ...

class Sponge128:
    def read(self, n: int) -> bytes:
        ...

class Shake256:
    def __init__(self, input_bytes: Buffer | None = None):
        ...

    def absorb(self, input_bytes: Buffer) -> "Shake256":
        ...

    def finalize(self) -> Sponge128:
        ...

class Sponge256:
    def read(self, n: int) -> bytes:
        ...

class TurboShake128:
    def __init__(self, domain_sep: int, input_bytes: Buffer | None = None):
        ...

    def absorb(self, input_bytes: Buffer) -> "TurboShake128":
        ...

    def finalize(self) -> Sponge128:
        ...

class TurboSponge128:
    def read(self, n: int) -> bytes:
        ...

class TurboShake256:
    def __init__(self, domain_sep: int, input_bytes: Buffer | None = None):
        ...

    def absorb(self, input_bytes: Buffer) -> "TurboShake256":
        ...

    def finalize(self) -> Sponge128:
        ...

class TurboSponge256:
    def read(self, n: int) -> bytes:
        ...

def shake128(input_bytes: Buffer) -> Sponge128:
    ...

def shake256(input_bytes: Buffer) -> Sponge256:
    ...

def turbo_shake128(domain_sep: int, input_bytes: Buffer) -> TurboSponge128:
    ...

def turbo_shake256(domain_sep: int, input_bytes: Buffer) -> TurboSponge256:
    ...
