import threading
import time
import subprocess


run_autoTOR = False
loop_mode = False
loop_time = 300


def execute_command(command):
    """
    Exécute la commande spécifiée et renvoie la sortie.
    Args:
        command (str): La commande à exécuter.
    Returns:
        str: La sortie de la commande.
    """
    try:
        command = subprocess.check_output(command, shell=True).decode("utf-8").strip()
        print(command)
        return command
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8").strip()


def start_tor():
    execute_command("brew services start tor")


def stop_tor():
    execute_command("brew services stop tor")


def tor_status():
    global run_autoTOR
    # If tor is running, return True
    status = execute_command("brew services list | grep tor | awk '{print $2}'")
    if status == "started":
        run_autoTOR = True
    else:
        run_autoTOR = False


def switch_loop():
    global loop_mode
    loop_mode = not loop_mode

    if run_autoTOR:
        if loop_mode:
            thread = threading.Thread(target=main_loop)
            thread.start()
        else:
            main()


def switch_autoTOR():
    global run_autoTOR
    run_autoTOR = not run_autoTOR
    if run_autoTOR:
        if loop_mode:
            thread = threading.Thread(target=main_loop)
            thread.start()
        else:
            main()
    else:
        stop_tor()


def change_ip():
    execute_command("brew services restart tor")


def main_loop():
    while run_autoTOR:
        change_ip()
        time.sleep(loop_time)


def main():
    start_tor()
