import sys
import time


from BullyNode import BullyNode

if( len(sys.argv) < 2):
    id = 3
else:
    id = sys.argv[1]


print('Node 1')
node1 = BullyNode("127.0.0.1", 8001, id = id)
node1.start()

print()
print('Connecting to Node 2 and 3')

node1.connect_with_node('127.0.0.1', 8002)
node1.connect_with_node('127.0.0.1', 8003)


while(1):
    
    print("1.Send message")
    print("2.Quit other nodes")
    entry= int(input())
    if(entry == 1):
        msg=input("Enter message:")
        data = {"name":"Nitheesh","message":msg}
        node1.send_to_nodes(data)
    if(entry == 2):
        node1.stop()
        break
    
