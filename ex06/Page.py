from elements import *

class Page:
    def __init__(self, elem):
        self.elem = elem
    
    def is_valid(self):
        # * check the HTML structure
        if not isinstance(self.elem, (Html, Head, Body, Title, Meta, Img, Table, 
                                    Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, 
                                    Span, Hr, Br, Text)):
            return False
        return self._validate_node(self.elem)
    
    def _validate_node(self, node):
        # * Recursive validation
        try:
            # ! Html with recursivities
            if isinstance(node, Html):
                if len(node.content) != 2:
                    return False
                return (
                isinstance(node.content[0], Head) 
                        and 
                isinstance(node.content[1], Body) 
                        and
                self._validate_node(node.content[0]) 
                        and 
                self._validate_node(node.content[1])
                )
            
            # ! Head with recursiviytes
            if isinstance(node, Head):
                return (
                    len(node.content) == 1 
                        and 
                    isinstance(node.content[0], Title)
                        and 
                    self._validate_node(node.content[0])
                    )
            
            # ! Body and Div content, with recursivities
            if isinstance(node, (Body, Div)):
                return all(
                    isinstance(elem, (H1, H2, Div, Table, Ul, Ol, Span, P)) 
                        and 
                    self._validate_node(elem) for elem in node.content
                    )
            
            #  ! ----- Fninish of recursivities ----- 

            # * Validate single Text content elements
            if isinstance(node, (Title, H1, H2, Li, Th, Td)):
                return len(node.content) == 1 and isinstance(node.content[0], Text)
            
            # *  Validate P content
            if isinstance(node, P):
                return all(isinstance(elem, Text) for elem in node.content)
            
            # * Validate Span content
            # ? Check if the content is not empty and all elements are Text or P and use de recursivity
            if isinstance(node, Span):
                return all(isinstance(elem, (Text, P)) and 
                         (not isinstance(elem, P) or self._validate_node(elem))
                         for elem in node.content)
            
            # * Validate List content
            # ? Check if the content is not empty and all elements are Li and use de recursivity
            if isinstance(node, (Ul, Ol)):
                return (len(node.content) > 0 and 
                       all(isinstance(elem, Li) and self._validate_node(elem) 
                           for elem in node.content))
            
            # * Validate Table structure
            # ? Check if the content is not empty and all elements are Tr and use de recursivity
            if isinstance(node, Table):
                return (len(node.content) > 0 and
                       all(isinstance(elem, Tr) and self._validate_node(elem) 
                           for elem in node.content))
            
            # * Validate Table row content
            # ? Check if the first element is a Th or Td, and all elements are of the same type, and use de recursivity
            if isinstance(node, Tr):
                if not node.content:
                    return False
                first_type = type(node.content[0])
                if first_type not in (Th, Td):
                    return False
                return all(isinstance(elem, first_type) and self._validate_node(elem)
                          for elem in node.content)
            
            # ! finish the validation
            return True
            
        except Exception:
            return False
    
    def __str__(self):
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + str(self.elem)
        return str(self.elem)
    
    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


if __name__ == '__main__':

    valid_html = Html([
        Head(Title(Text("Test Page"))),
        Body([
            H1(Text("Welcome")),
            Div([
                H2(Text("Section 1")),
                P(Text("Some text")),
                # Span([Text("In span"), H2(Text("Valid P in span"))]),
                Span([Text("In span"), P(Text("Valid P in span"))]),
                Table([
                    Tr([Th(Text("Name")), Th(Text("Age"))]),
                    Tr([Td(Text("John")), Td(Text("30"))])
                ]),
                Ul([
                    Li(Text("Item 1")),
                    Li(Text("Item 2"))
                ])
            ])
        ])
    ])
    
    page = Page(valid_html)
    print("\n=== Testing Valid Structure ===")
    print(f"Valid structure: {page.is_valid()}")
    print(page)
    page.write_to_file('test.html')
    
    print("\n=== Testing Invalid Cases ===")
    

    invalid_cases = [
        ("Missing Head", Html([Body([H1(Text("Title"))])])),
        ("Multiple Titles", Html([
            Head([Title(Text("T1")), Title(Text("T2"))]),
            Body([H1(Text("Content"))])
        ])),
        ("Mixed Th/Td", Html([
            Head(Title(Text("Test"))),
            Body([Table([Tr([Th(Text("Header")), Td(Text("Data"))])])])
        ])),
        ("Empty List", Html([
            Head(Title(Text("Test"))),
            Body([Ul([])])
        ])),
        ("Invalid Body Content", Html([
            Head(Title(Text("Test"))),
            Body([Text("Direct text not allowed")])
        ])),
        ("Empty Table", Html([
            Head(Title(Text("Test"))),
            Body([Table([])])
        ])),
        ("Invalid Span Content", Html([
            Head(Title(Text("Test"))),
            Body([Span([H1(Text("Invalid in span"))])])
        ]))
    ]
    
    for case_name, invalid_elem in invalid_cases:
        page = Page(invalid_elem)
        print(f"{case_name}: {page.is_valid()}")