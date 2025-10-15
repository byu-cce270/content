# Reading: ipywidgets

A graphical user interface , or GUI (pronounced “GOOEY”) is the buttons, text boxes, pictures, and stuff that a user of a computer program interacts with. For example, when you start Instagram on your phone, or print a document from Word, or even when you open Learning Suite, you are looking at and interacting with a graphical user interface. Look at this image and consider the various types of interactive components in each of these GUI’s. Here are a couple of examples of GUI’s:

![Window's GUI](images/windows_gui.png){width=500}

![gui_print_dialog.png](images/gui_print_dialog.png){width=700}

One of the ways we can make our Python code more user-friendly is by adding a GUI to it. Early in the semester, you learned how to use the Python `input()` statement to prompt the user to enter a text string or number. That is a simple type of GUI. Another popular GUI that is designed especially for use in notebooks is **Jupyter Widgets**. Jupyter widgets are implemented through a Python library called **ipywidgets**. These widgets allow the user to interact with your code in a more intuitive way, rather than just typing in commands and reading the output. 

You can access the full documentation for ipywidgets [here](https://ipywidgets.readthedocs.io/en/latest/index.html){target='blank'}. In the following sections, we will learn how to use ipywidgets to create interactive widgets in Colab notebooks.

## Importing

To use ipywidgets, you first need to import it. You can do this by using the following command:

```python
import ipywidgets as widgets
```

Note that ipywidgets comes pre-installed on Google Colab. If you are running in another environment, you may need to install it first.

## Overview

Widgets are a graphical way for a user to interact with your code. In general, when a user interacts with a widget, an event is triggered. For example, when a user clicks a button, a click event is triggered. You can handle these events in your code to perform actions based on the user's input. When using widgets, you need to structure your code in a way that allows you to handle these events.

To use ipywidgets, you need to follow these steps:

1. Create a widget
2. Set the properties of the widget
3. Handle events for the widget
4. Display the widget

In the following sections, we will learn how to create widgets, set widget properties, handle widget events, and display widgets.

## Creating Widgets

There are many different types of widgets that you can create using ipywidgets. Some of the most common widgets include:

 - Button
 - Checkbox
 - Dropdown
 - FloatSlider and IntSlider (for sliders)
 - RadioButtons and Select (for dropdowns)
 - SelectMultiple (for dropdowns that allow multiple selections)
 - Text and Textarea (for text inputs)
 - ToggleButton and ToggleButtons (for buttons that can be toggled on and off)
 - HBox and VBox (to arrange widgets horizontally or vertically)
 - HTML (to display HTML)
 - Image (to display images)
 - DatePicker (to select dates)
 - And many more

To create a widget, you can use the following command:
    
```python
widget = widgets.WidgetName()
```

For example, to create a button widget, you can use the following command:
    
```python
button = widgets.Button(description='Click me')
```

For a full list of widgets, you can refer to the [ipywidgets documentation - Widget List](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html){target='blank'}.


## Setting Widget Properties

You can set the properties of a widget by using the following command:

```python
widget.property = value
```

For example, to set the description of a button widget, you can use the following command:

```python
button.style = 'warning'
```

For a full list of properties, please refer to: [ipywidgets documentation - Widget List](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html){target='blank'}<br>
To learn more about styling widgets, see: [ipywidgets documentation - Styling of Jupyter widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html){target='blank'}

## Handling Widget Events

You can handle events for a widget by using the following command:

```python
def on_event_name(event):
    # code to handle event

widget.on_event_name(on_event_name)
```

For example, to handle the click event for a button widget, you can use the following command:

```python
def on_button_click(event):
    print('Button clicked')
    
button.on_click(on_button_click)
```

The function controls what happens when the button is clicked. The `event` parameter is passed to the function and contains information about the event (which may be useful in some cases). The `button.on_click` method in the code above associates the `on_button_click` function with the click event of the button widget.

For more details about widget events, you can refer to the [ipywidgets documentation - Widget Events](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Events.html){target='blank'}.

## Displaying Widgets

To display a widget, you can use the following command:

```python
display(widget)
```

For example, to display a button widget, you can use the following command:

```python
display(button)
```

You can also use the `widgets.VBox` and `widgets.HBox` widgets to arrange widgets vertically or horizontally. For example, to arrange two widgets vertically, you can use the following command:

```python
vbox = widgets.VBox([widget1, widget2])
display(vbox)
```

For more details about widget layout, you can refer to the [ipywidgets documentation - Widget Layout](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Layout.html){target='blank'}.

## Sample Use Cases

Let's create a simple example to demonstrate how to use ipywidgets. In this example, we will create a button widget that displays a message when clicked.

```python
import ipywidgets as widgets

# Create a button widget
button = widgets.Button(description='Click me')

# Define a function to handle the click event
def on_button_click(event):
    print('Button clicked')

# Handle the click event for the button widget
button.on_click(on_button_click)

# Display the button widget
display(button)
```
When you run this code, you will see a button widget displayed in the output cell. When you click the button, the message "Button clicked" will be printed in the output cell, like this:

![button_click.png](images/button_click.png)

Here is another example where we create a slider widget that displays the value of the slider when it is changed.

```python
import ipywidgets as widgets

# Create a slider widget
slider = widgets.IntSlider(value=0, min=0, max=100, description='Value')

# Define a function to handle the change event
def on_slider_change(event):
    print('Slider value:', event['new'])
    
# Handle the change event for the slider widget
slider.observe(on_slider_change, names='value')

# Display the slider widget
display(slider)
```
Here is another example where we create a dropdown widget that displays the selected value when it is changed.

```python
import ipywidgets as widgets

# Create a dropdown widget
dropdown = widgets.Dropdown(options=['Option 1', 'Option 2', 'Option 3'], value='Option 1', description='Value')

# Define a function to handle the change event
def on_dropdown_change(event):
    print('Selected value:', event['new'])

# Handle the change event for the dropdown widget
dropdown.observe(on_dropdown_change, names='value')

# Display the dropdown widget
display(dropdown)
```

## Conclusion

Widgets are a fun way to make your code more interactive and user-friendly. It can also make your code more visually appealing and engaging. You may find some ways to add widgets to your final project in this class.

For more information, you can refer to the [ipywidgets documentation](https://ipywidgets.readthedocs.io/en/latest/index.html){target='blank'}.

# Pre-Class Quiz Challenge

Open a new Colab notebook and do the following:

1. Rename the notebook to "(Your_Name)_HW_ipywidgets.ipynb".
2. Create two different widgets:
      - One should be a button. Try to change the description, style (color), and tooltip of the button. 
      - The other can be any widget of your choice. Try to changing some properties of the widget.
2. Display the widgets.
3. Try adding an event to one of the widgets. For example, you can add an event to the button that prints a message when the button is clicked.
4. Arrange the widgets vertically using `widgets.VBox` and display them.
5. Run the code and test the widgets to make sure they work as expected.
6. As a challenge, try adding making it so that when the button is clicked, the other widget changes its properties. For example, if you have a slider, try changing the value of the slider when the button is clicked. You could even have the Button disable the other widget when clicked or print the value of the other widget when clicked.
7. Share the link to your Colab notebook via Learning Suite when you take the Pre Class Quiz.
