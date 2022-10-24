import sys
import time
from BullyNode import BullyNode

id = sys.argv[1]
print('Node '+id)
node1 = BullyNode("127.0.0.1", 8000+int(id), id = id)
node1.start()

time.sleep(20)

while True:
    msg = input("Message:")
    data = {"name":id,"message":msg}
    node1.send_to_nodes(data)