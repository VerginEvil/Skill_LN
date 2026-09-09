# Typical usage
This topic describes the typical usage of the GBF.

## Initialization
The browser should be initialized with a function call. The application has to call the function [gbf.init()](gbf.init.md) of the framework.
The developer has the possibility to define the menu structure they want to use. There he can specify which action can be taken on an object. The menu structure should be specified in the function [gbf.set.menu.head()](gbf.set.menu.head.md) and [gbf.set.menu.item()](gbf.set.menu.item.md) in the application. It is also possible to set a default icon for possible parents, open and closed, selected and not selected and children, selected and not selected. This can be done with the functions gbf.set.interior.icon() and [gbf.set.resource()](gbf.set.resource.md) in the application.
The initialization phase ends with a [gbf.start()](gbf.start.md) function call which puts the GBF in control.

## Filling the toplevel of the data structure
The browser asks for information on the top level to be displayed. This is done with a call of a function with a fixed name: the function [gbf.get.top.level()](gbf.get.top.level.md). In that function the application must store the required data in the data structure of the browser with a function of the framework. This must be done with [gbf.add.object()](gbf.add.object.md). The developer must indicate within this call whether the object can have children. This is necessary for the browser to determine which actions should be taken at which time. The developer can also specify the icon and description of the object. This gives many possibilities to the developer to give the desired look to the browser. When no icon is specified the default icon is used. This way the data structure of the framework is filed.

## Actions

## To change the(number of) objects
The actions that follow are dependent of the actions of the user and the type of the object. When an object is a possible parent, the children must be displayed in case of a double click or a comparable event. The framework then calls the function [gbf.get.children()](gbf.get.children.md) in the application. This function must give the children of the parent object and store them in the data structure with the function gbf.add.object()of the framework. When an action is required on a possible parent object, the object has to be selected and the required action taken from the menu. When an object can only be a child, the double click or comparable event should perform the required default action.
The developer can use the function gbf.update.object() to change the icon or description of an object. To remove an object from the browser the function [gbf.set.drop.function()](gbf.set.drop.function.md) of the framework can be used. To insert an object the function gbf.add.object() of the framework can be used.

## Refresh
There are three possible ways to refresh the displayed objects:

- The developer can use the function [gbf.set.refresh.strategy()](gbf.set.refresh.strategy.md) of the framework to get a time based refresh

- A refresh can be performed as the result of a return value of a user function, see for example [gbf.menu.selected()](gbf.menu.selected.md)/P>

- A refresh can be done via a menu item and/or keystroke, see also gbf.init()

The refresh will execute gbf.get.top.level() and then gbf.get.children() of all open parents. Now not-existing objects will be removed from the browser and new objects will be displayed. This will keep the browser up to date with the database. Note that objects are matched ONLY by their object.key (see gbf.add.object()), as all other attributes of the object, such as object.description, object.value and obj.type, may have changed since this attribute change may have been what caused this refresh in the first place. The functions gbf.get.first.child() andgbf.get.next() should be avoided during a refresh, since that would lead to unpredictable results.

## User actions
When a menu option is chosen the framework calls the function gbf.menu.selected() in the application. The frameworks gives the code of the option and the object(s) that was/were marked so the application can execute the required function. The return value of gbf.menu.selected() is an indication for the framework which action should be performed (for example a refresh or a gbf.get.children() on the object).

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
