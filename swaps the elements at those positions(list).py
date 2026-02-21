def swap_elements(elem: list,first_index: int,second_index :int) -> list:
    first_pos = elem[first_index]
    second_pos = elem[second_index]
    elem[first_index] = second_pos
    elem[second_index] = first_pos
    print(elem)

swap_elements(["Name","Name","is","Md","Shafeeulla",
        ["My","usn"]],1,2)