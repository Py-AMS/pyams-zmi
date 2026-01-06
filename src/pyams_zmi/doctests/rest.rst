
=======================
PyAMS utils rest module
=======================

PyAMS is using Cornice with a Swagger extension which allows to provide a documentation
for all REST APIs.

This module provides a single view which is used to render OpenAPI specification of all REST
API:

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp(hook_zca=True)

    >>> from cornice import includeme as include_cornice
    >>> include_cornice(config)
    >>> from cornice_swagger import includeme as include_swagger
    >>> include_swagger(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)

    >>> request = DummyRequest('/__api__')
    >>> from pyams_zmi.rest import openapi_specification

    >>> from pprint import pprint
    >>> specs = openapi_specification(request)
    >>> sorted(specs.keys())
    ['basePath', 'info', 'paths', 'swagger']
    >>> specs['basePath']
    '/'
    >>> specs['info']
    {'title': 'PyAMS', 'version': '1.0'}
    >>> specs['swagger']
    '2.0'
    >>> sorted(specs['paths'].keys())
    ['/__api__', '/api/rest/monitor']


The module also provides a custom handler for OPTIONS verb:

    >>> from pyams_zmi.rest import openapi_options

    >>> request = DummyRequest('/__api__', method='OPTIONS')
    >>> response = openapi_options(request)
    >>> response is None
    True


Tests cleanup:

    >>> tearDown()
