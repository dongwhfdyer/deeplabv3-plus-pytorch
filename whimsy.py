import torch
import time

while True:
    mem = torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0  # GB
    print(f'memory reserved: {mem:>14.3f}')
    print(mem)
    time.sleep(3)
