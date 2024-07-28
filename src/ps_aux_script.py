import subprocess
import datetime


def get_ps_aux_output():
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def parse_ps_aux_output(output):
    lines = output.strip().split('\n')
    headers = lines[0].split()
    process_list = lines[1:]

    processes = []
    for process in process_list:
        process_data = process.split(maxsplit=len(headers) - 1)
        process_info = dict(zip(headers, process_data))
        processes.append(process_info)

    return processes


def generate_report(processes):
    users = set()
    user_process_count = {}
    total_memory = 0.0
    total_cpu = 0.0
    max_memory_process = ('', 0.0)
    max_cpu_process = ('', 0.0)

    for process in processes:
        user = process['USER']
        cpu = float(process['%CPU'])
        mem = float(process['%MEM'])
        cmd = process['COMMAND']

        users.add(user)
        if user in user_process_count:
            user_process_count[user] += 1
        else:
            user_process_count[user] = 1

        total_memory += mem
        total_cpu += cpu

        if mem > max_memory_process[1]:
            max_memory_process = (cmd[:20], mem)

        if cpu > max_cpu_process[1]:
            max_cpu_process = (cmd[:20], cpu)

    report = f"""
Отчёт о состоянии системы:
Пользователи системы: {', '.join(users)}
Процессов запущено: {len(processes)}

Пользовательских процессов:
"""
    for user, count in user_process_count.items():
        report += f"{user}: {count}\n"

    report += f"""
Всего памяти используется: {total_memory:.1f}%
Всего CPU используется: {total_cpu:.1f}%
Больше всего памяти использует: {max_memory_process[0]} ({max_memory_process[1]:.1f}%)
Больше всего CPU использует: {max_cpu_process[0]} ({max_cpu_process[1]:.1f}%)
"""
    return report


def save_report(report):
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")
    filename = f"{current_time}-scan.txt"
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Отчёт сохранён в файл: {filename}")


def main():
    output = get_ps_aux_output()
    processes = parse_ps_aux_output(output)
    report = generate_report(processes)
    print(report)
    save_report(report)


if __name__ == "__main__":
    main()
