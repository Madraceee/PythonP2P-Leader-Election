from BullyNode import BullyNode

print('Master[Controller]')
master = BullyNode("127.0.0.1", 8000, id = 0)
master.start()

print("Master Node is ONLINE")

N = int(input("Enter the number of systems :"))

print('Connecting to Nodes')

for i in range(N):
    master.connect_with_node('127.0.0.1', 8001+i)

while True:
    print("1) Broadcast Message \n2) Node-to-Node Message\n3) Terminate Master\n4) Terminate All nodes")
    choice = int(input())
    if choice==1:
        data = {"name":"Master","message":"I am the master"}
        master.send_to_nodes(data)
    if choice==2:
        n = int(input("Enter ID:"))
        data = {"name":"Master","message":"Node 2 Node"}
        print(master.all_nodes)
        master.send_to_node(master.all_nodes[n],data,'none')
    if choice==3:
        master.stop()
        break
    if choice==4:
        master.send_to_nodes("STOP")