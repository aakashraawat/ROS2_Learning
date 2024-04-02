from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aakashrawat',
    maintainer_email='aakashrawat@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_first_node = my_py_pkg.my_first_node:main",#node_name install the node  write the ( package name.node_file.py)
            #"py_first_oop_node = my_py_pkg.my_first_node_oop:MyNode"# for the oop

            "robot_news_station= my_py_pkg.robot_news_station:main" , # usually the node name is similar to the file name
            "smartphone_sub= my_py_pkg.smartphone_sub:main",#subscriber
            "number_publisher =my_py_pkg.number_publisher:main",#publisher
            "number_count = my_py_pkg.number_count:main",#subscriber for number and publisher for number counter
            "add_two_ints_server= my_py_pkg.add_two_ints_server:main",# server
            
            "add_two_ints_client = my_py_pkg.add_two_ints_client:main",
            
            "hw_status_publisher=my_py_pkg.hw_status_publisher:main",# publishe for the custom harware status messages 
        ],
    },
)
