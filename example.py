from abc import ABCMeta, abstractmethod

class Component(metaclass=ABCMeta):
    @abstractmethod
    def print(self,num:int)->None:
        pass
    
    @abstractmethod
    def add(self,component)->None:
        pass

class AbstractComponent(Component):
    
    def getName(self):
        return self.name
    
    def createIndent(self,num:int):
        return " " * num

    def add(self,component:Component):
        raise Exception("add is not defined")
    
    def print(self,num:int)->None:
        pass

class Category(AbstractComponent):

    def __init__(self,name:str) -> None:
        self.name = name
        self.components = []
    
    def print(self,index:int = 0):
        INDENT = self.createIndent(index)
        print(INDENT + "#" + self.getName())
        index += 1
        for component in self.components:
            component.print(index)
    
    def add(self, component: Component):
        self.components.append(component)

class Shop(AbstractComponent):
    
    def __init__(self,name) -> None:
        self.name = name
    
    def print(self,index:int = 0):
        INDENT = self.createIndent(index)
        print(INDENT + "##" + self.getName())

ROOT_CATEGORY = Category('フレンチ')
CHILD_CATEGORY_1 = Category('レストラン')
CHILD_CATEGORY_2 = Category('ビストロ')
SHOP1 = Shop('ショップ1')
SHOP2 = Shop('ショップ2')
SHOP3 = Shop('ショップ3')
SHOP4 = Shop('ショップ4')
SHOP5 = Shop('ショップ5')
SHOP6 = Shop('ショップ6')

ROOT_CATEGORY.add(SHOP1)
ROOT_CATEGORY.add(SHOP2)
ROOT_CATEGORY.add(SHOP3)
ROOT_CATEGORY.add(CHILD_CATEGORY_1)
CHILD_CATEGORY_1.add(SHOP4)
CHILD_CATEGORY_1.add(SHOP5)
ROOT_CATEGORY.add(CHILD_CATEGORY_2)
CHILD_CATEGORY_2.add(SHOP6)

ROOT_CATEGORY.print()
print('======')
SHOP1.print()
print('======')
CHILD_CATEGORY_1.print()


