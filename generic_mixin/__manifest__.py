{
    'name': "Generic Mixin",

    'summary': """
    Technical module with generic mixins, that may help to build other modules
    """,

    'author': 'Trackedge',

    'category': 'Technical Settings',
    'version': '14.0.1.60.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'http_routing',
        'bus',
    ],
    'data': [
        'views/assets.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False
}
