title: Queues & Stacks
date: May 30th, 2020
slug: queues-and-stacks
category: Algorithms + Data Structures
status: active

Let's look at the differences between the two data structures:

1. **Queues**: First-In First-Out
2. **Stacks**: Last-In Last-Out

## Queues
This follows a **First-In First-Out** processing order i.e. the first element added to a queue will be processed first. A queue should support two operations:

- Enqueue
- Dequeue

### Enqueue
Adds the element to the tail of a queue. The tail position gets incremented.

### Dequeue
Removes the first element of a queue i.e. the head element. Once, it's removed, the subsequent element becomes the new head element of the queue. The position of the new head element gets incremented and the previous one is assigned a negative integer like -1 or some garbage value. 

**Implementation of a standard queue using C++:**
```cpp
class Queue {
    private:
        int pos;
        vector<int> data;

    public:
        Queue() {
            pos = 0;
        }

        bool enqueue(int value) {
            data.push_back(value);
            return true;
        }

        bool dequeue() {
            if(isEmpty()){
                return false;
            }
            pos++;
            return true;
        }

        int front() {
            return data[pos];
        }

        bool isEmpty() {
            return pos >= data.size();
        }
}
```
In terms of memory management, a standard Queue is quite inefficient and incapable of handling dynamic memory.

## Stacks
This follows a **Last-In First-Out** processing order i.e. the last element added to a queue will be the first to be removed. Just like queues, it has two simple operations:

- Push
- Pop

### Push
Each element is pushed towards the end of the stack. Think of it as a card deck where you stack a card on top of another card.

### Pop
It removes the most recent element i.e. the newly added element from the stack.

**Implementation of a stack using C++:**
```cpp
class Stack {
    private:
        vector&ltint> data;
    public:
        void push(int value) {
            data.push_back(value);
        }

        bool isEmpty() {
            return data.empty();
        }

        int top() {
            return data.back();
        }

        bool pop() {
            if(!isEmpty()) {
                data.pop_back();
                return true;
            }
            else {
                return false;
            }
        }
}
```
Unlike queues, stacks are easier to implement and pretty efficient at managing dynamic memory.

Oh, if you ever get to use these, don't worry about implementing them, nearly all programming languages have their own implementations of `stack` and `queue` that comes with it's own standard library.
