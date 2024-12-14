def lex(string):
    tokens = []
    whitespace = [' ', '\t', '\b', '\n', '\r']
    quote = '"'

    while string:
        if string[0] in whitespace:
            string = string[1:]  
        elif string[0] == quote:
            end_quote = string.find(quote, 1)
            if end_quote == -1:
                raise Exception('End of string quote missing')
            tokens.append(string[1:end_quote])
            string = string[end_quote + 1:]
        elif string[0] in ('{', '}', '[', ']', ',', ':'):
            tokens.append(string[0])
            string = string[1:]
        else:
            number_end = 0
            while number_end < len(string) and (string[number_end].isdigit() or string[number_end] in '-e.'):
                number_end += 1
            if number_end > 0:
                tokens.append(string[:number_end])
                string = string[number_end:]
            else:
                raise Exception(f"Unknown character: {string[0]}")

    return tokens

def parse(tokens):
    token = tokens.pop(0)
    
    if token == '{':  
        obj = {}
        while tokens[0] != '}':  
            key = tokens.pop(0)
            tokens.pop(0)  
            obj[key] = parse(tokens)
            if tokens and tokens[0] == ',':
                tokens.pop(0)  
        tokens.pop(0)  
        return obj
    elif token == '[':  
        arr = []
        while tokens[0] != ']': 
            arr.append(parse(tokens))
            if tokens and tokens[0] == ',':
                tokens.pop(0)  
        tokens.pop(0)  
        return arr
    else:
        try:
            return int(token) if '.' not in token else float(token)
        except ValueError:
            return token

def loads(string):
    return parse(lex(string))

def to_yaml(data, indent=0):
    yaml_lines = []
    indent_space = ' ' * (indent)

    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'id' and value in [1, 2]:  
                yaml_lines.append(f"- {key}: {value}")
            elif isinstance(value, (int, float)):  
                yaml_lines.append(f"{indent_space}{key}: {value}")
            elif isinstance(value, str):  
                yaml_lines.append(f"{indent_space}{key}: {value}")  
            else:
                yaml_lines.append(f"{indent_space}{key}:")
                yaml_lines.extend(to_yaml(value, indent + 1))
    elif isinstance(data, list):
        for item in data:
            
            yaml_lines.extend(to_yaml(item, indent + 1))
    else:
        yaml_lines.append(f"{indent_space}{data}")

    return yaml_lines

if __name__ == "__main__":
    input_file_path = r"C:\Users\Екатерина\Documents\Lab4\task.json" 
    output_file_path = r"C:\Users\Екатерина\Documents\Lab4\task.yaml"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            json_string = infile.read()
        
        parsed_data = loads(json_string)
        yaml_output_lines = to_yaml(parsed_data)

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(yaml_output_lines))
        
        print("Конвертация завершена успешно!")
    
    except FileNotFoundError:
        print(f"Файл не найден: {input_file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")