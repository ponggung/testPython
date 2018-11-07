import redis   # 導入redis模組，通過python操作redis 也可以直接在redis主機的服務端操作緩存資料庫

# host是redis主機，需要redis服务端和客户端都啟動 redis默認端口是6379
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('foo', 'bar')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['foo'])
print(r.get('foo'))  # 取出鍵foo對應的值
print(type(r.get('foo')))