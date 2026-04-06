import requests
import threading
import time

URL = "http://127.0.0.1:5000/recommend/u1"

total_requests = 10
success = 0
fail = 0
times = []

lock = threading.Lock()


def hit(request_id):
    global success, fail

    start = time.time()

    try:
        response = requests.get(URL)
        elapsed = time.time() - start

        with lock:
            times.append(elapsed)

            if response.status_code == 200:
                success += 1
                print(f"[{request_id}] ✅ Success | Time: {round(elapsed,4)}s")
            else:
                fail += 1
                print(f"[{request_id}] ❌ Failed | Status: {response.status_code}")

    except Exception as e:
        with lock:
            fail += 1
        print(f"[{request_id}] ❌ Error:", str(e))


def run_load_test():
    threads = []

    print("\n🚀 Starting Load Test...\n")

    for i in range(total_requests):
        t = threading.Thread(target=hit, args=(i+1,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\n📊 Load Test Summary")
    print("---------------------------")
    print(f"Total Requests   : {total_requests}")
    print(f"Successful       : {success}")
    print(f"Failed           : {fail}")

    if times:
        print(f"Average Time     : {round(sum(times)/len(times),4)}s")
        print(f"Min Time         : {round(min(times),4)}s")
        print(f"Max Time         : {round(max(times),4)}s")

    print("\n✅ Load Test Completed Successfully 🚀")


if __name__ == "__main__":
    run_load_test()
    