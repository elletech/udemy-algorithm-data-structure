from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    # 連結リストの最後にdataを追加する
    def append(self, data: Any) -> None:
        new_node = Node(data)
        # headがNoneの場合、つまりLinkedListが空の場合はnew_nodeを入れて返す
        if self.head is None:  # is Noneは省略不可
            self.head = new_node
            return

        # LinkedListが空ではない場合
        last_node = self.head  # last_nodeを一番最初のノードで初期化する
        while last_node.next:  # 次のノードがnoneになるまで繰り返す(is not Noneは省略できる)
            last_node = last_node.next  # last_nodeの参照先を次のノードに更新する
        last_node.next = new_node

    # 連結リストの最初にdataを追加する
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # 連結リストを辿って最初に一致したdataを削除する
    def remove(self, data: Any) -> None:
        current_node = self.head
        # 先頭で一致した場合
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None  # current_nodeは不要になったため参照を削除する(ガーベッジコレクションでも削除可能)
            return

        # 先頭以外で一致した場合
        previous_node = None  # 最初以外のNodeを削除する場合、前のノードのnextを書き換える必要があるため一個前のNode(参照)を保存する
        # nodeのdataが一致するまで次のnodeをcurrent_nodeに入れる
        while current_node and current_node.data != data:
            previous_node = current_node
            # current_nodeにcurrent_node.nextの参照を代入する
            # 元々の参照先と変わらないためLinkedListには影響がない
            current_node = current_node.next

        # current_nodeがNoneということは、LinkedListを最後まで辿った事になる。
        # つまり、最後までdataが一致しなかったことを表すため何もせずにreturn
        if current_node is None:
            return

        # previous_node.nextの参照先にcurrent_node.nextの参照先を入れている
        # 元々の参照先を変えてしまっているので、LinkedListに影響あり
        previous_node.next = current_node.next
        current_node = None

    # 反復的にLinkedListを逆にする
    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        # 最後のノードになるまで繰り返す(current_nodeがNoneになるまで)
        while current_node:
            next_node = current_node.next  # next_nodeにcurrent_node.nextを退避させる
            current_node.next = previous_node  # current_node.nextの参照先をprevious_nodeにすることでLinkedListを逆にする

            previous_node = current_node  # 次のノードからみるとcurrent_nodeはprevious_nodeとなるため退避させる
            current_node = next_node  # 次のノード

        self.head = previous_node

    # 再帰的にLinkedListを逆にする
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node) -> Node:
            if not current_node:
                return previous_node
            next_node = current_node.next  # next_nodeにcurrent_node.nextを退避させる
            current_node.next = previous_node  # current_node.nextの参照先をprevious_nodeにすることでLinkedListを逆にする
            previous_node = current_node  # 次のノードからみるとcurrent_nodeはprevious_nodeとなるため退避させる
            current_node = next_node  # 次のノード
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)

    # ## TODO やり残し
    # def reverse_even(self) -> None:
    #     # 1, 4, 6, 8, 9 => 1, 8, 6, 4, 9
    #     # 1, 4, 6, 8, 9, 1, 4, 6, 8, 9 => 1, 8, 6, 4, 9, 1, 8, 6, 4, 9
    #     # 1, 2, 3, 4, 5, 6 => 1, 2, 3, 4, 5, 6

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(4)
    l.append(6)
    l.append(8)
    l.append(9)
    l.print()
    print('#### reverse_even')
    l.reverse_even
    l.print()