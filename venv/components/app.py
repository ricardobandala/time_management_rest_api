import falcon
from content import ContentTypeComponent
from db import DatabaseComponent
# from resources import v1


class App(falcon.API):

    def __init__(self):

        self.database_component = DatabaseComponent()
        self.content_type_component = ContentTypeComponent(content_type='application/json')

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component
        ])
