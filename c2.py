import sys
import time

from BullyNode import BullyNode

if( len(sys.argv) < 2):
    id = 3
else:
    id = sys.argv[1]

print('Node 2')
node1 = BullyNode("127.0.0.1", 8002, id = id)
node1.start()

print()

stop = 0
print("Press 1 to stop")
while(not stop):
    stop = int(input())
    
print("Exiting")

node1.stop()
    
    
