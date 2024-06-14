from Views.HomeView import homeView


class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.page_width = page.width
        self.page_height = page.height
        self.routes = {
            "/": homeView(page, self.page_width, self.page_height),
        }
        self.body = self.routes["/"]

    def route_change(self, route):
        self.body = self.routes[route.route]
        self.body.update()

        print("Ruta cambiada", route.route)

    def onPageResize(self):
        self.page_width = self.page.width
        self.page_height = self.page.height
        self.routes = {
            "/": homeView(self.page, self.page_width, self.page_height),
        }
        self.body = self.routes["/"]
