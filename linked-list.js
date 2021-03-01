class Node {
	constructor(data) {
		this.data=data;
		this.next=null; //다음 노드를 저장하는 변수
	}
}
class LinkedList{
	constructor() {
		this.length=0;//리스트 노드 개수
		this.head=null;
		this.tail=null;
    }
    addToTail(data) {
        let addData = new Node(data);
        if (this.head === null && this.tail === null) {
            this.head = addData;
            this.tail = addData;
        }
        if (this.head !== null) {
            //이때 tail은 그 전 맨끝 값 
            this.tail.next = addData;
            //여기서 tail은 새로 추가되는 맨 끝값
            this.tail = addData;
        }
        
        this.length++;
    };
    remove(data) {
        //데이터가 비어있으면 undefined 반환
        if (this.head === null) {
            return undefined;
        }
        //리스트 처음 값이 찾는 값과 같다면
        if (this.head.data === data) {
            //this.head를 다음 노드로 지정하여 아무도 가리키지 않게 만들어 가비지콜렉터에 추가
            this.head = this.head.next;
            this.length--;
        }
        let preNode = this.head;
        let curNode = this.head.next;
        console.log('pre,cur', preNode, curNode)
        //리스트 중간에 찾는 값이 존재하는지 확인
        //찾는 값이 리스트에 없으면 curNode가 tail.next가 되면 null이므로 루프 종료됨
        while (curNode) {
            if (curNode.data === data) {
                preNode.next = curNode.next;
                this.length--;
                break
            }
            else {
                //찾는 값이 나올 때까지 다음 노드로 초기화
                preNode = curNode;
                curNode = curNode.next;
            }
        }
    }
    
    getNodeAt(index) {
        //리스트의 처음부터 탐색
        let headNode = this.head;
        //인덱스 넘버가 리스트의 크기를 초과한다면 undefined
        if (index > this.length) {
            return undefined
        } else {
            //인덱스 넘버에 도달할 때까지 루프함
            for (let i = 0; i < index; i++) {
                //다음 노드로 계속 초기화
                headNode = headNode.next
            }
            return headNode;
        }
    }
    contains(data) {
        //리스트 처음부터 탐색함	
        let curNode = this.head;
        //리스트에 값이 존재하지 않는다면 ourNode는 null이 되므로 while루프는 종료되고 false가 리턴됨
        while (curNode) {
            if (curNode.data === data) {
                return true
            }
            else {
                //값을 찾을 때까지 다음 노드로 초기화
                curNode = curNode.next
            }
        }
        return false
    }
    indexOf(data) {
        let curNode = this.head;
        console.log(curNode)
        let indexCount = 0;
        while(curNode) {
            if (curNode.data === data) {
                return indexCount;
            }
            else {
                indexCount ++;
                curNode = curNode.next;
            }
        }
        return -1
    }

    size() {
        return this.length
    }
}
const Linked = new LinkedList();
// console.log(Linked)
Linked.addToTail('google')
// console.log(Linked)
console.log(Linked.tail.next)
Linked.addToTail('apple')
// console.log(Linked)
console.log(Linked.tail.next)
Linked.addToTail('samsung')
// console.log(Linked)
Linked.addToTail('yellow')
Linked.addToTail('yanolza')
Linked.addToTail('tesla')
// console.log(Linked)
Linked.remove('yellow')
Linked.remove('apple')
console.log(Linked)
console.log(Linked.getNodeAt(5))
console.log(Linked.getNodeAt(1))
console.log(Linked.contains('samsung'))
console.log(Linked.indexOf('samsung'))
console.log(Linked.size())

