for index, value in enumerate('QWERTYUIOPASDFGHJKLZXCVBNM'):
    print(f"button{value} = Button(self.root, text = value, font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Labels.onClick(self, index))")
