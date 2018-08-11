class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = new Node();
    }

    addToHead(value) {
        const new_node = new Node(value);
        var current_node = this.head
        while(current_node.next !== null){
            current_node = current_node.next;
        }
        current_node.next = new_node;
    }

    length(){
        let current_node = this.head;
        var length = 0;
        while (current_node.next !== null){
            length += 1;
            current_node = current_node.next;
        }
        console.log(length)
        return length
    }

    display(){
        var list = []
        var current_node = this.head
        while (current_node.next !== null){
            current_node = current_node.next;
            list.push(current_node.data);
        }
        console.log(list)
    }

    get(index){
        if(index >= this.length()){
            let error = "The index is beyond the linked list count"
            console.log(error)
            return error;
        }
        let current_index = 0;
        let current_node = this.head;
        while(true){
            current_node = current_node.next
            if(current_index == index){
                console.log(current_node.data)
                return current_node.data
            }
            current_index += 1
        }
    }

    erase(index){
        if(index >= this.length()){
            let error = "The index is beyond the linked list count"
            console.log(error)
            return error;
        }
        let current_index = 0;
        let current_node = this.head;

        while(true){
            let last_node = current_node;
            current_node = current_node.next
            if(current_index == index){
                last_node.next = current_node.next
                return false
            }
            current_index += 1
        }
    }

    eraseDups(){
        let current_node = this.head;
        let hash = {}
        while(current_node.next !== null){
            let prev_node = current_node
            current_node = current_node.next
            if(current_node.data in hash){
                // test
                // prev_node 
                // end test
                // console.log('Number why it tripped the if >>>>> ',current_node.data);
                prev_node.next = current_node.next
            } else {
                hash[current_node.data] = true
                // prev_node.next = current_node.next
            }
        }
        // console.log(hash)
    }
};

var test = new LinkedList()
test.addToHead(1)
test.addToHead(2)
test.addToHead(3)
test.addToHead(3)
test.addToHead(4)
test.addToHead(5)
test.addToHead(3)
test.addToHead(33)
test.addToHead(3)
test.addToHead(34)
test.addToHead(3)
test.addToHead(3)

test.display()
test.eraseDups()
test.display()
