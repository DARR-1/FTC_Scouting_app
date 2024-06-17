from Views.HomeView import homeView
from Views.DatabasesView import databaseView
from Views.AddDataView import dataView


class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.page_width = page.width
        self.page_height = page.height
        self.routes = {
            "/": homeView(page, self.page_width, self.page_height),
            "/Database": databaseView(page, self.page_width, self.page_height),
            "/AddData": dataView(page),
        }
        self.body = self.routes["/"]
        page.bottom_appbar = self.body.appbar

    def route_change(self, route):
        self.body = self.routes[route.route]
        self.body.update()

        page.bottom_appbar = self.body.appbar

        print("Ruta cambiada", route.route)

    def onPageResize(self):
        self.page_width = self.page.width
        self.page_height = self.page.height
        self.routes = {
            "/": homeView(self.page, self.page_width, self.page_height),
            "/Database": databaseView(self.page, self.page_width, self.page_height),
            "/AddData": dataView(self.page),
        }
        self.body = self.routes["/"]
