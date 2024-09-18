import os
import asyncio
import time
import jsonpickle
import io
import dns.message
import dns.query
import dns.rdatatype
import requests
from dns.rdatatype import RdataType

jsonpickle.set_preferred_backend('json')
jsonpickle.set_encoder_options('json', ensure_ascii=False, indent=4)


def jsonpickle_pretty():
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False, indent=4, separators=(', ', ': '))


def jsonpickle_compact():
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False, indent=None, separators=(',', ':'))


def string0(*args) -> str:
    sio = io.StringIO()
    for arg in args:
        sio.write(str(arg))
    return sio.getvalue()


async def generator_to_list1(generator, list0: list):
    async for item in generator:
        list0.append(item)


def file_size(path: str):
    try:
        result = os.path.getsize(path)
    except Exception as e:
        result = -1
    return result


async def generator_to_list2(generator, no_exception=False):
    list0 = []
    try:
        async for item in generator:
            list0.append(item)
    except BaseException as e:
        print(str(e))
        if not no_exception:
            raise e
    return list0


async def generator_foreach(generator, action, no_exception=False):
    try:
        async for item in generator:
            action(item)
    except BaseException as e:
        print(str(e))
        if not no_exception:
            raise e


def append_file(file_path: str, text: str) -> str:
    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    file = open(file_path, 'a+', encoding='utf8')
    file.write(text)
    file.close()
    return text



def write_text(file_path: str, text: str) -> str:
    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    file = open(file_path, 'w', encoding='utf8')
    file.write(text)
    file.close()
    return text


def write_obj(file_path: str, obj):
    jsonpickle_compact()

    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    file = open(file_path, 'w', encoding='utf8')
    file.write(jsonpickle.encode(obj, keys=True))
    file.close()


def write_list(file_path: str, iterable, plaintext=False):
    jsonpickle_compact()

    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    file = open(file_path, 'w', encoding='utf8')
    for item in iterable:
        if plaintext:
            file.write(str(item))
        else:
            file.write(jsonpickle.encode(item, keys=True))

        file.write('\n')
    file.close()


def read_file(file_path: str, default='') -> str:
    result = default
    try:
        file = open(file_path, 'r', encoding='utf8')
        result = file.read()
        file.close()
    except Exception as e:
        pass
    finally:
        try:
            file.close()
        except Exception:
            pass
    return result


def read_obj(file_path: str):
    result = None
    try:
        file = open(file_path, 'r', encoding='utf8')
        result = json_decode(file.read())
        file.close()
    except Exception as e:
        pass
    finally:
        try:
            file.close()
        except Exception:
            pass
    return result


def read_list(file_path: str):
    result = list()
    try:
        file = open(file_path, 'r', encoding='utf8')
        for line in file:
            result.append(json_decode(line))
        file.close()
    except Exception as e:
        print(str(e))
    finally:
        try:
            file.close()
        except Exception:
            pass
    return result


def json_encode(obj):
    jsonpickle_pretty()
    return jsonpickle.encode(obj, keys=True)


def json_decode(json0: str):
    jsonpickle_pretty()
    return jsonpickle.decode(json0, keys=True)


def to_int(s, default=None):
    try:
        return int(str(s))
    except Exception as e:
        return default


def to_float(s, default=None):
    try:
        return float(str(s))
    except Exception as e:
        return default


def intersect(list1, list2):
    if isinstance(list1, set) and isinstance(list2, set):
        return list1.intersection(list2)
    else:
        return set(list1).intersection(list2)


async def create_asyncio_threads_async(count: int, await_time=3):
    tasks = []
    for i in range(count):
        task = asyncio.create_task(asyncio.to_thread(time.sleep, await_time))
        tasks.append(task)
    await asyncio.gather(*tasks)


def create_asyncio_threads(count: int, await_time=3):
    asyncio.run(create_asyncio_threads_async(count, await_time))


def is_generator(obj):
    return str(type(obj)) == "<class 'async_generator'>"


def type0(o):
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__  # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__


def dns_query_doh(dns_server: str, domain: str, dns_record: RdataType):
    result = []
    query = dns.message.make_query(domain, dns_record)
    # Convert the DNS query to wire format
    query_wire = query.to_wire()
    # Make a POST request to the DoH server with the DNS query
    response = requests.post(dns_server, data=query_wire, headers={'Content-Type': 'application/dns-message'})
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as a DNS message
        response_message = dns.message.from_wire(response.content)
        # Print the response
        print("DNS Records for", domain, "of type", dns.rdatatype.to_text(dns_record))
        for answer in response_message.answer:
            result.append(answer)
    else:
        print("Error:", response.status_code)
