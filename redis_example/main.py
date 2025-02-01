import redis

redis_client = redis.Redis(
    host='localhost',  # Redis 서버의 호스트명 (로컬 Redis 서버일 경우 'localhost')
    port=6379,  # Redis 기본 포트 (기본값: 6379)
    db=0,  # 사용할 Redis 데이터베이스 번호 (기본값: 0)
    decode_responses=True  # 문자열 응답을 디코딩 (Python 3에서는 일반적으로 사용)
)

# 1. 키-값 저장
redis_client.set('my_key', 'my_value')

# 2. 키-값 조회
value = redis_client.get('my_key')
print(f"Value for 'my_key': {value}")

# 3. 리스트에 값 추가 및 조회
redis_client.lpush('my_list', 'item1', 'item2', 'item3')
list_items = redis_client.lrange('my_list', 0, -1)
decoded_items = [item for item in list_items]
print(f"Items in 'my_list': {decoded_items}")

# 4. 키 만료 시간 설정
redis_client.set('temp_key', 'temporary_value', ex=10)
print("Key 'temp_key' set with expiration of 10 seconds.")
