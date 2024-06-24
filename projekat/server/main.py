import requests
import redis
import consul

client = consul.Consul(host='localhost', port=8500)
r = redis.Redis(host='localhost', port=6379, db=0)


if __name__=='__main__':


# Consul example
    client.kv.put('myapp/config', '{"name": "example", "value": 123}')
    index, data = client.kv.get('myapp/config')
    if data:
        print('Consul data:', data['Value'].decode('utf-8'))

    # Redis example
    r.set('foo', 'bar')
    print('Redis data:', r.get('foo').decode('utf-8'))