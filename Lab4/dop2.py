import os
import yaml
import json
import re

def preprocess_json_string(string):
    string = re.sub(r'\s+', ' ', string)  # Заменяем несколько пробелов на один
    string = string.strip()  # Удаляем пробелы в начале и конце
    string = re.sub(r"'", '"', string)  # Заменяем одинарные кавычки на двойные
    string = re.sub(r'//.*?\n', '', string)  # Удаление однострочных комментариев
    string = re.sub(r'/\*.*?\*/', '', string, flags=re.DOTALL)  # Удаление многострочных комментариев

    return string

def parse(string):
    preprocessed_string = preprocess_json_string(string)
    return yaml.dump(json.loads(preprocessed_string), default_flow_style=False, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), "taskdop2.json")
    output_file = os.path.join(os.path.dirname(__file__), "taskdop2.yaml")

    if not os.path.exists(input_file):
        print(f"Ошибка: Файл не найден по пути {input_file}. Проверьте правильность пути.")
        exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            string = infile.read()

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(parse(string))

        print("Конвертация завершена. Результат сохранен в 'taskdop2.yaml'.")

    except json.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON. Проверьте содержимое файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")