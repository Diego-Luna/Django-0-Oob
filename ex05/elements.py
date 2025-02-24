from elem import Elem, Text

# *  The elements
class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

# * Head elements
class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')

# * Body elements
class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

# * Table elements
class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

# * List elements
class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)

# * Heading elements
class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

# * Text elements
class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)

# * Single elements
class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='hr', attr=attr, tag_type='simple')

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='br', attr=attr, tag_type='simple')


if __name__ == '__main__':
    # * Test the HTML structure from the exercise
    html = Html([
        Head(
            Title(
                Text('"Hello ground!"')
            )
        ),

        Body([
            H1(
                Text('"Oh no, not again!"')
            ),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(html)

    # * Additional tests
    print("\n=== PDF Test ===\n")
    print( Html( [Head(), Body()] ) )

    # * Additional tests
    print("\n=== 🥲 Additional Tests ===\n")
    
    # * Test table structure
    table = Table([
        Tr([
            Th(
                Text("Header 1")
            ), 
            Th(
                Text("Header 2")
            )
            ]),
        Tr([
            Td(Text("Cell 1"))
            , 
            Td(Text("Cell 2"))
            ]
        )
    ])
    print(table)
    
    # * Test lists
    print("\n=== List Tests 🎬  ===\n")
    ul = Ul([
        Li(Text("Item 1")),
        Li(Text("Item 2")),
        Li(Text("Item 3"))
    ])
    print(ul)