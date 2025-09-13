import threading
import time

def count_down():
    for i in range(5, 0, -1):
        print(f"🔻 Counting down: {i}")
        time.sleep(1)

def count_up():
    for i in range(1, 6):
        print(f"🔺 Counting up: {i}")
        time.sleep(1)

def main():
    print("🚀 Starting threads...\n")

    # Create threads
    thread1 = threading.Thread(target=count_down)
    thread2 = threading.Thread(target=count_up)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("\n✅ Both threads finished.")

if __name__ == "__main__":
    main()
