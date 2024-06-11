from Views.HomeView import homeView


class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": homeView(page),
        }
        self.body = ft.Container(content=self.routes["/"])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()

        print("Ruta cambiada", route.route)
