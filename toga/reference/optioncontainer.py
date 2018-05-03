import toga

container = toga.OptionContainer()

table = toga.Table(['Hello', 'World'])
tree = toga.Tree(['Navigate'])

container.add('Table', table)
container.add('Tree', tree)


def build(app):
    return container


toga.App('First App', 'org.pybee.helloworld', startup=build).main_loop()
