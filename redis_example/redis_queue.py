import redis
import time

# Redis 연결
redis_client = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

### Producer ###
# 큐에 메시지 추가
queue_name = 'my_queue'
messages = ['메세지1', '메세지2', '메세지3']

for message in messages:
    redis_client.lpush(queue_name, message)  # 큐의 끝에 메시지 추가
    print(f'Produced: {message}')

### Consumer ###
while True:
    message = redis_client.rpop(queue_name)  # 큐의 앞에서 메시지 가져오기
    if message:
        print(f'Consumed: {message}')
    else:
        print('Queue is empty. Waiting for messages...')
        time.sleep(2)  # 대기 후 재시도