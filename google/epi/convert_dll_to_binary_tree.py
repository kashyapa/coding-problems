def convert_dll_to_tree(l):

    def build_bst(start, end):

        if start >= end:
            return None

        mid = (start + end)//2
        left = build_bst(start, mid)
        cur, head[0] = head[0], head[0].next
        cur.prev = left
        cur.next = build_bst(mid+1, n)
        return cur



    head = [l]
    n = len(l)
    return build_bst(0, n)