import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                logs.append(log_entry)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level not in counts:
            counts[level] = 0
        counts[level] += 1
    return counts

def display_log_counts(counts: dict):
    print(f"{'Уровень логирования':<20} | {'Количество':<10}")
    print('-' * 32)
    for level, count in counts.items():
        print(f"{level:<20} | {count:<10}")

def display_log_details(logs: list, level: str):
    print(f"\nДетали логов для уровня '{level}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print(r"Использование: python hw3.py C:\Users\br4vetrave1er\Desktop\projects\goit-algo-hw-05\logs.txt [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter.upper())
        display_log_details(filtered_logs, level_filter.upper())

if __name__ == "__main__":
    main()

