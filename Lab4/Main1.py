input_file_path = r"C:\Users\Екатерина\Documents\Lab4\task1.json"
output_file_path = r"C:\Users\Екатерина\Documents\Lab4\task1.yaml"

with open(input_file_path, encoding='utf-8') as f:
    json_data = f.read()  

yaml_lines = []
indent_level = 0

json_data = json_data.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', '')
json_lines = json_data.splitlines()

for line in json_lines:
    line = line.strip()
    if not line:  
        continue

    parts = line.split(':')
    key = parts[0].strip()
    
    if len(parts) > 1:
        value = ':'.join(parts[1:]).strip()  
        if value.endswith(','):
            value = value[:-1].strip()  
        if key == 'id' and value in ['1', '2']:  
            yaml_lines.append('  ' * (indent_level-2) + '- ' + key + ': ' + value)
        else:
            yaml_lines.append('  ' * indent_level + key + ': ' + value)
    
    if key == 'schedule':
        indent_level += 1
    elif key in ['type', 'campus', 'time', 'auditory', 'teacher']:
        indent_level += 1

    if ':' not in line:
        indent_level -= 1


with open(output_file_path, 'w', encoding='utf-8') as outfile:
    outfile.write("\n".join(yaml_lines).strip())  

print(f"Конвертация завершена. Результат сохранен в '{output_file_path}'.")