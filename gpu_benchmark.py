# Подключаем PyTorch для работы с тензорами и GPU
import torch

# Подключаем time, чтобы измерять время выполнения
import time

# Размер квадратных матриц: 5000 x 5000
size = 5000

# Создаём две случайные матрицы на CPU
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

# Засекаем время перед умножением на CPU
start = time.time()

# Перемножаем матрицы на CPU
c_cpu = a_cpu @ b_cpu

# Считаем, сколько секунд заняло CPU-умножение
cpu_time = time.time() - start

# Печатаем результат CPU
print(f"CPU: {cpu_time:.3f}s")

# Проверяем, доступна ли CUDA/GPU
if torch.cuda.is_available():
    # Копируем матрицы с CPU на GPU
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    # Ждём, пока GPU закончит все предыдущие операции
    torch.cuda.synchronize()

    # Засекаем время перед умножением на GPU
    start = time.time()

    # Перемножаем матрицы на GPU
    c_gpu = a_gpu @ b_gpu

    # Ждём завершения вычислений на GPU
    torch.cuda.synchronize()

    # Считаем время GPU
    gpu_time = time.time() - start

    # Печатаем результат GPU
    print(f"GPU: {gpu_time:.3f}s")

    # Считаем, во сколько раз GPU быстрее CPU
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
else:
    # Если CUDA недоступна, сообщаем, что используется только CPU
    print("CUDA is not available, using CPU only")