vegetable = ["青菜", "萝卜", "花菜"]
print(id(vegetable))

new_list_01 = vegetable.copy()
print(id(new_list_01))


new_list_02 = vegetable
print(id(new_list_02))

vegetable.append("卷心菜")

print(vegetable, new_list_01)
print(vegetable, new_list_02)

print("hello world")