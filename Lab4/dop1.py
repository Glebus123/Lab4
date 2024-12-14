import os
import yaml
import json

def parse(string):
    return yaml.dump(json.loads(string), default_flow_style=False, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), "taskdop1.json")
    output_file = os.path.join(os.path.dirname(__file__), "taskdop1.yaml")

    if not os.path.exists(input_file):
        print(f"Ошибка: Файл не найден по пути {input_file}. Проверьте правильность пути.")
        exit(1)

    try:
        # Чтение входного файла
        with open(input_file, "r", encoding="utf-8") as infile:
            string = infile.read()

        # Запись результата в выходной файл
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(parse(string))

        print("Конвертация завершена. Результат сохранен в 'taskdop1.yaml'.")

    except json.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON. Проверьте содержимое файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
