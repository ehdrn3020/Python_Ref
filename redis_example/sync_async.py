import redis
import time
import psutil

# Redis 연결
redis_client = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

# 테스트 데이터 생성 (1,000,000 키)
# print("Generating test data...")
# for i in range(1000000):
#     redis_client.set(f"key:{i}", "value")
#
# print("Test data generated.\n")

# 메모리 사용량 체크 함수
def get_memory_usage():
    process = psutil.Process()
    mem = process.memory_info().rss / (1024 * 1024)
    return f"{mem:.2f} MB"

# 1. 동기 명령어 DEL 성능 테스트
print("Testing DEL (Synchronous)...")
start_time = time.time()
for i in range(1000000):
    redis_client.delete(f"key:{i}")
sync_duration = time.time() - start_time
print(f"DEL Duration: {sync_duration:.2f} seconds")
print(f"Memory Usage After DEL: {get_memory_usage()}\n")

# 테스트 데이터 재생성
print("Regenerating test data...")
for i in range(1000000):
    redis_client.set(f"key:{i}", "value")

print("Test data regenerated.\n")

# 2. 비동기 명령어 UNLINK 성능 테스트
print("Testing UNLINK (Asynchronous)...")
start_time = time.time()
for i in range(1000000):
    redis_client.unlink(f"key:{i}")
async_duration = time.time() - start_time
print(f"UNLINK Duration: {async_duration:.2f} seconds")
print(f"Memory Usage After UNLINK: {get_memory_usage()}\n")

# 결과 비교
print("====== Summary ======")
print(f"DEL (Sync) Duration: {sync_duration:.2f} seconds")
print(f"UNLINK (Async) Duration: {async_duration:.2f} seconds")
