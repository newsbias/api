from rest_framework import renderers
from openapi_codec import OpenAPICodec


class SwaggerRenderer(renderers.BaseRenderer):
    media_type = 'application/openapi+json'
    format = 'swagger'

    def __init__(self):
        self.codec = OpenAPICodec()

    def render(self, data, media_type=None, renderer_context=None):
        return self.codec.dump(data)
