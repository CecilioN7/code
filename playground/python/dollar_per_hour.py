import time
from datetime import datetime, timedelta

def main():
    # curr_time = time.time()
    # local_time = time.localtime(curr_time)
    # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    # print()
    # print(f"{curr_time} \n")
    # print(f"{local_time} \n")
    # print(f"{formatted_time}")

    now = datetime.now()
    print("Current time: ", now)

if __name__ == "__main__":
    main()