### To Install Pylint
https://gist.github.com/suiluj/3606f451b80dd840036d23833859d9f2
### Windows, Mac OS X & Debian:
```
   pip install pylint
```
### Fedora:
```
   sudo yum install pylint
```
### Ubuntu:
```
   sudo apt-get install pylint
```
### To Run Pylint
### Change the directory to where the file is located on command prompt
### Get Full Report
### Run the command pylint with the file name as shown below:
```
   pylint fileName.py
```
### Get Errors & Warnings
### To return all the errors within the file, run pylint -rn and the file name
```
   pylint -rn fileName.py
```
### To Get Errors
### To return all the errors within the file, run pylint -E (capital E) and the file name
```
   pylint -E fileName.py
```
### To Disable Warning
### To generate errors and warning with a disabled violation, use `-d` along with disable code or comment as shown below:
```
   pylint -rn -d unused-variable fileName.py
```
### or
```
   pylint -rn -d W06012 fileName.py
```
### To Use Configuration File
### The configuration file that is being used on jenkins pylint can be found in the following directory inside the mantid folder :
```
  mantid\tools\Pylint\pylint.cfg
```
### To generate the exact same errors and warning as displayed on jenkins pylint, run the following command:
```
  pylint --rcfile ..mantid\tools\Pylint\pylint.cfg fileName.py
```
### note: provide the full path of the configuration file
### To Run GUI
### Run the following command to get Pylint GUI
```
  pylint-gui
```
### To Integrate Pylint
### PyCharm - JetBrains
### To run pylint inside PyCharm, follow the steps. Note: these steps are for Windows, may slightly vary on different platforms
```
  1) File/Settings/Tools/External Tools/
  2) Click Add '+' button
  3) Fill in the arguments
     1) Name: pylint
     2) Program: C:\Python27\Scripts\pylint
     3) Parameters: --rcfile ...\mantid\tools\Pylint\pylint.cfg $FileName$
     # Note: Insert full path instead of ...\mantid\tools\Pylint\pylint.cfg 
     4) Working directory: $FileDir$
     # Note: $FileName$ and $FileDir$ is a macro inserted
     5) Leave rest of settings as default and click `OK` on Edit Tool
  4) Click `OK` on Settings
  5) Click right on the file or code
  6) Select External Tools/pylint
  7) pylint voilations should run inside pyCharm
```
### Microsoft Visual Studio
### To run pylint inside Visual Studio, follow the steps.
```
  1) Tools/External Tools...
  2) Click Add button
  3) Fill in the arguments
     1) Title: pylint
     2) Command: C:\Python27\Scripts\pylint.exe
     3) Arguements: --rcfile ...\mantid\tools\Pylint\pylint.cfg $(ItemFileName)
     # Note: Insert full path instead of ...\mantid\tools\Pylint\pylint.cfg 
     4) Initial directory: $(ItemDir)
     # Note: $(ItemFileName) and $(ItemDir) is a macro inserted
     5) Uncheck`Close on exit` and check`Use Output window`
     5) Leave rest of settings as default and click `OK` on External Tools
  5) Open python file
  6) Select Tools/pylint 
  7) pylint violations should run inside Visual Studio
  ```
### pylint will not work if the file has been opened with the 'visual-studio' batch file
### To Disable
### To disable a violations locally inside your file
```
  1) Identify your violation which you would like to disable
  2) Search by error code on the following page.. http://docs.pylint.org/features.html
  # Useful detailed description is provided, which may even help you fix the violation
  3) Copy the violation comment e.g: too-many-instance-attributes
  4) Inside the working file, on top type in '# pylint: disable = ' followed by the disable comment, e.g:
     1) # pylint: disable = too-many-instance-attributes
```
### You may disable pylint on block level or line level, for more details: http://docs.pylint.org/faq.html#message-control