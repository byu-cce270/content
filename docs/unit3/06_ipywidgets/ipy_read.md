# Reading: ipywidgets

A graphical user interface , or GUI (pronounced “GOOEY”) is the buttons and text boxes and pictures and stuff that a user of a computer program interacts with.

For example, when you start Instagram on your phone, or print a document from Word, or even when you open Learning Suite, you are looking at and interacting with a graphical user interface. Look at this image and consider the various types of interactive components in each of these GUI’s.

As we’ve discussed previously, Google’s Colaboratory Python Notebook environment is only ONE of MANY different ways to write Python code.
And…Python is only ONE of DOZENS of different programming languages.
And…we are going to use ‘ipywidgets’ to build graphical user interfaces for your code. But realize that this is only ONE of MANY different tools for making GUI’s in a Python notebook. It is a pretty handy one though, and the principles we learn here are transferable to all of the other tools, Python environments, and programming libraries. 

**NOTE:** ipywidgest won’t let us build complex GUI’s like the ones pictures above, but we can actually do quite a lot with it. We can make buttons, sliders, checkboxes, text inputs, dropdown boxes and so much more.

ipywidgets are just one method to create this powerful tool in python. Primarily used in Google Colab or Jupyter notebooks. They can be used to create interactive visualizations, dashboards, and more. In this reading, we will learn how to use ipywidgets to create interactive widgets in Jupyter notebooks.

## Installation

To install ipywidgets, you can use the following command:

```python
!pip install ipywidgets
```
**NOTE:** When using Google Colab, you don't need to install it. You only need to install ipywidgets once. If you have already installed it, you can skip this step.

## Importing

To use ipywidgets, you need to import it. You can do this by using the following command:

```python
import ipywidgets as widgets
```

## Creating Widgets
