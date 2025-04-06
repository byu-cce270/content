# Bonus Content: Using Python Locally

This semester we have been using Python in a Google Colab environment, which is a cloud-based platform. However, you can also run Python locally on your own machine. This can be useful for various reasons, such as working offline, using specific libraries, referencing your files directly without uploading them, or running larger projects. This document provides a brief overview of how to use Python locally, including installation, running scripts, and using virtual environments. We will also discuss some common IDEs (Integrated Development Environments) that can help you write and run Python code more efficiently.

## 1. Installing Python Locally

When you run Python in Google Colab, you are using a version of Python that is hosted on Google's servers. To run Python locally, you need to install it on your own machine. Here are the steps to do that:

### 1.1 Downloading Python

To install Python locally, you need to download the Python installer for your operating system. Follow these steps:

1. Go to the official Python website: [python.org](https://www.python.org/downloads/).
2. Download the latest version of Python for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH" during installation.

After installation, you can verify that Python is installed correctly by opening a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and typing the following command:

```bash
python --version
```
This should display the version of Python you installed. If you see an error message, it means Python is not installed correctly or not added to your PATH.

### 1.2 Installing pip

`pip` is a package manager for Python that allows you to install additional libraries and packages. It is usually included with Python installations, but you can check if it's installed by running:

```bash
pip --version
```
If you see an error message, you can install `pip` by following the instructions on the [pip installation page](https://pip.pypa.io/en/stable/installation/).

### 1.3 Installing Additional Libraries

You can install additional libraries using `pip` as well. For example, to install NumPy and Pandas, you can run:

```bash
pip install numpy pandas
```
You can install any other libraries you need for your projects in a similar way. Just replace `numpy pandas` with the names of the libraries you want to install.

## 2. Running Python Scripts Locally

Once you have installed Python and any necessary libraries, you can run Python scripts locally. Here are the steps to do that:

### 2.1 Creating a Python Script

You can create a Python script using any text editor (e.g., Notepad, Visual Studio Code, PyCharm). Just create a new file with a `.py` extension (e.g., `script.py`) and write your Python code in it. For example:

```python
# script.py
print("Hello, World!")
```
### 2.2 Running the Script

To run the script, open your terminal, navigate to the directory where the script is located, and run the following command:

```bash
python script.py
```

This will execute the script and display the output in the terminal. In this case, it should print "Hello, World!" to the console.

## 3. Using Virtual Environments

When working on Python projects, it's a good practice to use virtual environments. A virtual environment is an isolated environment that allows you to manage dependencies for different projects separately. This way, you can avoid conflicts between different versions of libraries. For example, if you have two projects that require different versions of the same library, using virtual environments allows you to keep them separate.

### 3.1 Creating a Virtual Environment

To create a virtual environment, navigate to your project directory in the terminal and run the following command:

```bash
python -m venv myenv
```

This will create a new directory called `myenv` that contains the virtual environment.

### 3.2 Activating the Virtual Environment

To activate the virtual environment, run the following command:

- On Windows:
```bash
myenv\Scripts\activate
```
- On macOS/Linux:
```bash
source myenv/bin/activate
```
Once activated, your terminal prompt will change to indicate that you are now working within the virtual environment.

### 3.3 Installing Packages in the Virtual Environment

When the virtual environment is activated, you can install packages using `pip`, and they will only be available within that environment. For example:

```bash
pip install numpy pandas
```

### 3.4 Deactivating the Virtual Environment

To deactivate the virtual environment and return to your system's default Python environment, simply run:

```bash
deactivate
```
This will return you to your system's default Python environment.

## 3. Using Conda for Package Management

In addition to using `pip` for package management, you can also use `conda`, which is a package manager that comes with the Anaconda distribution. Conda is particularly useful for managing dependencies and creating isolated environments. It can be used to install Python packages as well as non-Python packages, making it a versatile tool for data science and scientific computing.

If you prefer using `conda` for package management, you can install the Anaconda distribution, which includes Python and many popular libraries. Anaconda also provides a package manager called `conda`, which can be used to create virtual environments and manage dependencies. There is also a lightweight version called Miniconda, which includes only the `conda` package manager and Python.

### 3.1 Installing Miniconda

To install Miniconda, follow these steps:

1. Go to the Miniconda download page: [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Download the installer for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions.
4. Open a terminal and verify the installation by running:

```bash
conda --version
```
### 3.2 Creating a Conda Environment
To create a new conda environment, run the following command:

```bash
conda create --name myenv python=3.9
```
This will create a new conda environment named `myenv` with Python 3.9 installed.
### 3.3 Activating the Conda Environment
To activate the conda environment, run the following command:

```bash
conda activate myenv
```
### 3.4 Installing Packages in the Conda Environment

To install packages in the conda environment, use the following command:

```bash
conda install numpy pandas
```
This will install NumPy and Pandas in the active conda environment.

### 3.5 Deactivating the Conda Environment

To deactivate the conda environment, run the following command:

```bash
conda deactivate
```
This will return you to the base conda environment or your system's default Python environment.


## 4. Common IDEs for Python Development

There are several IDEs (Integrated Development Environments) that can help you write and run Python code more efficiently. An IDE provides features like code completion, debugging, and project management, making it easier to develop Python applications. Depending on your needs and preferences, you can choose from a variety of IDEs. Below are some popular options:

### 4.1 Visual Studio Code (VS Code)

Visual Studio Code is a lightweight and powerful code editor that supports Python development. It has a rich ecosystem of extensions, including support for Jupyter Notebooks, debugging, and version control. You can install the Python extension for VS Code to enhance your Python development experience.

Link: [Visual Studio Code](https://code.visualstudio.com/)

To install the Python extension, open VS Code, go to the Extensions view (Ctrl+Shift+X), and search for "Python". Install the extension provided by Microsoft. Once installed, you can create and run Python scripts directly within VS Code. It also has a built-in terminal, allowing you to run Python scripts and commands without leaving the editor.

VS Code also natively supports Co-pilot, an AI-powered code completion tool that can help you write code faster and more efficiently. You can install the Co-pilot extension from the Extensions view in VS Code. This works similarly to the AI feature in Google Colab, providing suggestions and code snippets as you type.

VS Code is free and open-source and it is available for Windows, macOS, and Linux. 

The VS Code user interface looks like this:

![VS Code Interface](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

### 4.2 PyCharm

PyCharm is a popular IDE specifically designed for Python development. It offers a wide range of features, including code completion, debugging, and version control integration. PyCharm has both a free Community edition and a paid Professional edition with additional features.

Link: [PyCharm](https://www.jetbrains.com/pycharm/)

The Community edition is free and open-source, while the Professional edition offers additional features for web development and database management. There is also a free educational version available for students.

To install PyCharm, go to the official website and download the version that suits your operating system. Once installed, you can create a new project and start writing Python code. PyCharm also supports virtual environments, allowing you to manage dependencies for different projects easily. PyCharm has a built-in terminal, so you can run Python scripts and commands without leaving the IDE. It also includes a powerful debugger that allows you to step through your code and inspect variables.PyCharm is available for Windows, macOS, and Linux.

PyCharm also has a built-in feature called "Code Intelligence," which provides code suggestions and autocompletion as you type. It also supports the use of GitHub Co-pilot, an AI-powered code completion tool that can help you write code faster and more efficiently. You can install the Co-pilot extension from the PyCharm marketplace. This works similarly to the AI feature in Google Colab, providing suggestions and code snippets as you type.

The PyCharm user interface looks like this:

![PyCharm Interface](https://resources.jetbrains.com/help/img/idea/2024.3/py_new_ui_light_theme.png)

### 4.3 Spyder

Spyder is an open-source IDE specifically designed for scientific programming in Python. It includes features like an interactive console, variable explorer, and integrated debugging tools. Spyder is part of the Anaconda distribution but can also be installed separately.

Link: [Spyder](https://docs.spyder-ide.org/current/)

You can install Spyder using `conda` as follows:

```bash 
conda install spyder
```

Once installed, you can launch Spyder by running `spyder` in the terminal. Spyder is particularly useful for data analysis and scientific computing, as it provides a MATLAB-like interface with support for inline plotting and data visualization.

The Spyder user interface looks like this:

![Spyder Interface](https://raw.githubusercontent.com/spyder-ide/spyder/5.x/img_src/screenshot.png)

### 4.4 Jupyter Notebook

Jupyter Notebook is a popular tool for writing and running Python code in an interactive environment. It allows you to create notebooks that can contain code, text, images, and more. You can use Jupyter Notebook to run Python code locally, similar to how you do it in Google Colab. If you want to use Jupyter Notebook locally, you can install it using pip. Open your terminal and run the following command:

```bash
pip install jupyter
```

Or you can install it using conda:

```bash
conda install jupyter
```

This will install Jupyter Notebook, which allows you to create and run notebooks similar to those in Google Colab. To launch Jupyter Notebook, run the following command in your terminal:

```bash
jupyter notebook
```

The interface to Jupyter Notebook will open in your web browser, and you can create new notebooks or open existing ones. You can write and run Python code in the cells, add text and images, and save your work as a notebook file.

The interface to Jupyter Notebook looks like this:

![Jupyter Notebook Interface](https://jupyter-notebook.readthedocs.io/en/latest/_images/notebook-running-code.png)

## Conclusion

Using Python locally can provide you with more flexibility and control over your projects. By following the steps outlined in this document, you can install Python, run scripts, and manage dependencies using virtual environments. Additionally, using an IDE can enhance your development experience and make it easier to write and run Python code. Whether you're working on small scripts or larger projects, having Python set up locally can be a valuable skill.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
- [PyCharm Documentation](https://www.jetbrains.com/pycharm/documentation/)
- [Spyder Documentation](https://docs.spyder-ide.org/current/)
- [Python Virtual Environments Documentation](https://docs.python.org/3/tutorial/venv.html)
- [Python pip Documentation](https://pip.pypa.io/en/stable/)
- [Python Installation Guide](https://realpython.com/installing-python/)
