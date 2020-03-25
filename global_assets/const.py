
name ='Flask Session Tutorial',
version ='0.0.1',
description ='Source code for the accompanying tutorial on how to use Blueprints in Flask.',
long_description ="long_description",
long_description_content_type ='text/markdown',
url ='https://github.com/hackersandslackers/flaskblueprint-tutorial',
author ='Todd Birchard',
author_email ='toddbirchard@gmail.com',
classifiers =[
                'Programming Language :: Python :: 3.7',
            ],
keywords ='Flask Flask-Assets Blueprints',
packages ="find_packages()",
install_requires =['Flask',
                  'Flask_assets'],
extras_require ={
                   'dev': ['check-manifest'],
                   'test': ['coverage'],
                   'env': ['python-dotenv']
               },
entry_points ={
                 'console_scripts': [
                     'install=wsgi:__main__',
                 ],
             },
project_urls ={
                 'Bug Reports': 'https://github.com/hackersandslackers/flaskblueprint-tutorial/issues',
                 'Source': 'https://github.com/hackersandslackers/flaskblueprint-tutorial/',
             },



inventory_dir = '/home/vttek/.ansible/inventory'
playbook_dir = '/home/vttek/.ansible/playbooks'
facts_dir = '/home/vttek/.ansible/facts'
role_dir = '/home/vttek/.ansible/roles'