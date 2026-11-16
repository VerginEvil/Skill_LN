# Colors overview
Use the *rgb()* function to compose colors by specifying their red, green, and blue intensities. You can then use these colors, for example, when creating graphical objects such as windows, push buttons, labels, and so on. Use the other functions to retrieve the red, green, or blue intensity of an existing color.
On a monochrome display, colors are converted to fill patterns. On a 16-color display, the closest match to the composed color is used. Use [get.display.data()](../functions_system_and_user_information/get.display.data.md) to check the number of colors available on the display.
In addition to composing your own colors, you can use the following predefined colors:
| | | |
|---|---|---|
| RGB.BLACK | RGB.BLUE | RGB.YELLOW |
| RGB.MAGENTA | RGB.GREEN | RGB.GRAY |
| RGB.RED | RGB.WHITE | RGB.CYAN |
You can also use the function [color.dialog()](../functions_client_file_access/color.dialog.md) to let the user select a color.

## Related topics
- [Colors overview](overview.md)

- [Colors synopsis](synopsis.md)
