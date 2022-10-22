import sys
from BullyNode import BullyNode

id = sys.argv[1]
print('Node '+id)
node1 = BullyNode("127.0.0.1", 8000+int(id), id = id)
node1.start()