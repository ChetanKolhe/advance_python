class A:
    def __init__(self):
        print("Class A init")

    def add(self):
        print("Add method")


class B(A):  # B --> A--> object
    def __init__(self):
        print("Class B init")
        super().__init__()

        super(B, self).__init__()

    def add(self):
        print("B")

class C(B): # C --> B --> A --> obj
    def add(self):
        super(B,self).add()


#
# class C(B):
#     def __init__(self):
#         print("Class C init")
#         super(C, self).__init__()


if __name__ == '__main__':
    c = C()
    c.add()

    # b_obj = B()
    #
    # s_proxy = super(B, b_obj)
    # print(s_proxy)
    #
    # s_proxy.add()
    #
    #
    # # class Bound proxy
    # # super(base_class , sub_class)
    #
    # class_bound_proxy = super(B, B)
    # class_bound_proxy.add(b_obj)
    #
    #
    # c_obj = C()
    # c.add()
    #
    #
    #
    #
    #
    #
