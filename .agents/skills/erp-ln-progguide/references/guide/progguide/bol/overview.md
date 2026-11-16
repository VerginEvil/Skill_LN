# Business Object Layer

## BOL Overview
Business Objects are the main building blocks of Infor LN. Only the Business Objects will handle all communication from other applications with Infor LN.
A Business Object is an object understandable by the Business (i.e. Purchase Order, Organizational Unit)

- It has information stored in the Business Object Attributes (i.e. Purchase Order Number, Organizational Unit Name)

- It has a set of actions, Business Object Methods, which can manipulate the Business Object Attributes (i.e. Create Purchase Order, List Organizational Units)

In order to model and store all this information the Business Object Repository is developed.
Besides the Business Object entities (Public Attributes, Public Methods and its Arguments, Protected Attributes, Protected Methods and its Arguments) the Business Object Repository stores the relation of these entities with the existing Baan 3GL objects (Table fields, DLL functions and sessions).
In this way it supports wrapping the database with a Business oriented layer.
For each Business Object two Business Object Interfaces can be defined: a Public Interface and a Protected Interface.
The Public Interface is targeted for integrators that use external non-Infor LN applications that communicate with Infor LN.
The Protected Interface is targeted for internal Infor LN integrations.
The BOL architecture can be found in the picture below.
The BOL can be split into 5 separated parts (DLLs):

- [Public Layer](sb_layer.md)

- [Interface Conversion Public Layer](sc_layer.md)

- [Protected Layer](st_layer.md)

- [Interface Conversion Protected Layer](sm_layer.md)

- [Specific Methods Library](sf_layer.md)

## Related topics
- [Business Object Layer](overview.md)
