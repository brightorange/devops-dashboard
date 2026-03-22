import sysinfo
import logcheck
import tasklist

while True:
    choice = input(f"""Please select an option:
– [1] System Info
– [2] Log Checker
– [3] Task List
– [0] Exit
    """)
    if choice == "0":
        break;
    elif choice == "1":
        sysinfo.show_sysinfo()
    elif choice == "2":
        logcheck.check_log()
    elif choice == "3":
        tasklist.manage_tasks()
    else:
        print("Invalid option")