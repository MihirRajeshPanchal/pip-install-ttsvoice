from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ttsvoice',
  version='0.0.2',
  description='Simple Text-to-Speech functions',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Mihir Panchal',
  author_email='mihirpanchal5400@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['text-to-speech','ttsvoice','speech','text'], 
  packages=find_packages(),
  install_requires=['gtts','pyttsx3'] 
)