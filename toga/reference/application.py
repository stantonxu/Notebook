import toga


class MyApp(toga.App):
    def startup(self):
        pass


if __name__ == '__main__':
    app = MyApp('First App', 'org.pybee.helloworld')
    app.main_loop()
