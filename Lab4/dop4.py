import time
import subprocess
num_runs = 100
python_path = r'C:\Users\Екатерина\AppData\Local\Programs\Python\Python312\python.exe'  
total_time_main, total_time_dop1, total_time_dop2, total_time_dop3 = 0, 0, 0, 0

for _ in range(num_runs):
    start_time = time.time()
    subprocess.run([python_path, r'C:\Users\Екатерина\Documents\Lab4\Main.py'])  # Путь к Main.py
    end_time_main = time.time()
    subprocess.run([python_path, r'C:\Users\Екатерина\Documents\Lab4\dop1.py'])  # Путь к dop1.py
    end_time_dop1 = time.time()
    subprocess.run([python_path, r'C:\Users\Екатерина\Documents\Lab4\dop2.py'])  # Путь к dop2.py
    end_time_dop2 = time.time()
    subprocess.run([python_path, r'C:\Users\Екатерина\Documents\Lab4\dop3.py'])  # Путь к dop3.py
    end_time_dop3 = time.time()

   
    total_time_main += end_time_main - start_time
    total_time_dop1 += end_time_dop1 - end_time_main
    total_time_dop2 += end_time_dop2 - end_time_dop1
    total_time_dop3 += end_time_dop3 - end_time_dop2

print("Среднее время работы Main = {:.6f} секунд".format(total_time_main / num_runs))
print("Среднее время работы dop1 = {:.6f} секунд".format(total_time_dop1 / num_runs))
print("Среднее время работы dop2 = {:.6f} секунд".format(total_time_dop2 / num_runs))
print("Среднее время работы dop3 = {:.6f} секунд".format(total_time_dop3 / num_runs))
