from setuptools import setup, find_packages

setup(
    name='CMA_CAMERA_LIBRARIE',
    version='1.0.0',
    description='Librería para transmisión de frames de cámara con WebSocket',
    author='Gustavo Mayorga Gutierrez',
    author_email='gustavomayorgagtz@gmail.com',
    packages=find_packages(),
    install_requires=[
        'python-socketio',
        'opencv-python',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
