import sys
import os
import re

def default_html(template):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
       <meta charset="UTF-8">
        <title>{page_title}</title>
    </head>
    <body>
        <header>
            <h1>{full_name}</h1>
        </header>
        <main>
            <div>
                <p>Age: {age}</p>
            </div>
            <div>
                <p>Profession: {profession}</p>
            </div>
    """ + "\n" + template + "\n" """   
        </main>
    </body>
    </html>
    """

def create_html_file(content):
    try:
        f = open("file.html", 'w')
        f.write(content)
        f.close()
    except Exception:
        print("Error: An error occured")


def check_default_value(list, default, value):
    fount = False

    for item in list:
        if item[0] == default:
            fount = True
            break
    if not fount:
        list.append([default, value])
    return list


def modify_tmplate(file, content):
    f = open(file, 'w')
    f.write(content)
    f.close()

def repance_variable(content, variables):
    for variable in variables:
            content = content.replace('{'+variable[0]+'}', variable[1])
    return content

def main_function(file):
    try:
        #   *: Check if the file is a .template file
        if not file.endswith('.template'):
            print("Error: The file is not a .template file")
            return
        #   *: Read the file send in parametrer
        f = open(file, 'r')
        content_template = f.read()
        f.close()

        #   *: check if the file settings.py exist
        if not os.path.exists('settings.py'):
            print("Error: settings.py file not found")
            return
        #   *: Read the file settings.py and take the value of the variables
        f = open('settings.py', 'r')
        content_settings = f.read()
        f.close()
        #   *: take the content of the file and replace the {{variable}} by the value of the variable
        variables = re.findall(r'(\w+)\s*=\s*(.*)', content_settings) 
        #   *: Create aa new file html with the content of the file with the variable replaced
        content_html = default_html(content_template)

        # * add the de fefault value of the variables
        variables = check_default_value(variables, 'page_title', 'ex00')
        variables = check_default_value(variables, 'full_name', 'Diego Francisco Luna Lopez')
        variables = check_default_value(variables, 'age', '23')
        variables = check_default_value(variables, 'profession', 'profession')
        
        # *: Replace the variables in the template
        content_template = repance_variable(content_template, variables)

        # *: Create the file
        create_html_file(content_template)
        modify_tmplate(file, content_html)

    except FileExistsError:
        print("Error: File not found")
    except FileNotFoundError:
        print("Error: File not found")
    except Exception:
        print("Error: An error occured") 

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main_function(sys.argv[1])
    else:
        print("Error: only one argument is needed")
