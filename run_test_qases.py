import subprocess
# Запуск первого теста
subprocess.call(["pytest", "-s", "main.py::test_csv_create"])
# Запуск второго теста
subprocess.call(["pytest", "-s", "upload_nom.py::test_loading_nom"])
# Запуск третьего теста
subprocess.call(["pytest", "-s", "get_nom.py::test_save_nom"])
# Запуск четвертого теста
subprocess.call(["pytest", "-s", "contractors.py::test_contractors_create"])