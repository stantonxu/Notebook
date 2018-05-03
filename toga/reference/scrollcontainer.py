import toga

content = toga.WebView()
content.url = 'http://www.google.com'
container = toga.ScrollContainer(content=content, horizontal=False)
container.vertical = False


def build(app):
    return container


toga.App('First App', 'org.pybee.helloworld', startup=build).main_loop()
