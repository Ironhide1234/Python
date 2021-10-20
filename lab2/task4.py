class Btree:
    price = []
    def __init__(self,data,quant):
        self.data = data
        self.quant = quant
        self.left = None
        self.right = None
    def create_price(self,*prices):
        Btree.price.append('')
        for price in prices:
            if isinstance(price,(int,float)) and price > 0:
                Btree.price.append(price)
            else:
                raise ValueError("Value error")
    def insert(self,data,quant):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Btree(data,quant)   
                else:
                    self.left.insert(data,quant)     
            elif data > self.data:
                if self.right is None:
                    self.right = Btree(data,quant)
                else:
                    self.right.insert(data,quant)                       
        else: 
            self.data = data
            self.quant = quant      

    def treeTraversal(self,root):
        res = []
        if root:
            res = self.treeTraversal(root.left)
            res.append(root.quant*Btree.price[root.data])
            res = res + self.treeTraversal(root.right)
        return res

code, qty = map(int, input().split())
if 0  < code <=10 and qty > 0:
    root = Btree(code,qty)
else:
    raise ValueError
root.create_price(1,2,3,4,5,6,7,8,9,10)
for i in range(4):
    code, qty = map(int, input().split())
    if 0<code<=10 and qty>0:
        root.insert(code,qty)
    else:
        raise ValueError

print(root.treeTraversal(root))            
