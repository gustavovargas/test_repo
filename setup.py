from distutils.core import setup

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]
    
setup(
    name='ec_test',
    version='0.0.1',
    # url='https://gitlab.com/ecdatos/ec_piano',
    author='gus',
    # packages=[
    #     'piano', 'piano.api_client', 'piano.api_client.export', 'piano.reports_api_client'
    # ],
    include_package_data=True,
    author_email='ge.vargasn@gmail.com',
    description='Test methods',
    install_requires=read_requirements()
)