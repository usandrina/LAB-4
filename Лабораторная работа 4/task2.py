# TODO импортировать необходимые молули

import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input,output) -> None:
    csv_rows = []
    # TODO считать содержимое csv файла
    with open(input) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]: row[field[i]] for i in range(len(field))}])
    # TODO Сериализовать в файл с отступами равными 4
    with open(output, "w") as f:
        f.write(json.dumps(csv_rows, indent=4))





with open(INPUT_FILENAME) as f:
    if __name__ == '__main__':
        # Нужно для проверки
        task(INPUT_FILENAME, OUTPUT_FILENAME)

        with open(OUTPUT_FILENAME) as output_f:
            for line in output_f:
                print(line, end="")
