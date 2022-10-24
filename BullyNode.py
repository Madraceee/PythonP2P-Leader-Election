from p2pnetwork.node import Node
#making changes

class BullyNode(Node):
    
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(BullyNode, self).__init__(host, port, id, callback, max_connections)
        print("BullyNode : Started")
    
    def node_message(self, node, data):
        if(data=="STOP"):
            self.stop()
            exit(1)
        elif data["message"][:5]=="PORTS":
            for i in data["message"][6:].split(","):
                self.connect_with_node('127.0.0.1',int(i))
        else:
            print("Message from " + node.id + ": " + str(data))

    def inbound_node_disconnected(self, node):
        if(node.id == 1):
            print("Main Node disconnected")
            self.stop() 


    
    

