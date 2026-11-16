# Getting started
This topic gives the first few steps to build a main application from scratch.
The most important things the API provides are: creating activities, creating resources and assigning resources to activities. The view (or chart if you like) that gives a time-lined overview of the activities is called the *Gantt view*. The view that gives a time-lined overview of the activities per resource is called the *Schedule view*

## Minimal steps to create a Plan Chart
- In the include section of the main application, add the following: `#include <bic_plcm> | all PLan Chart Manager defines.`

- In the main function (or where appropriate) call *plcm.init()*

- Create the PLan Chart by using the different plcm.* functions.

- Call *plcm.start()* to start the Plan chart on the client.

## Related topics
- [Synopsis](synopsis.md)

- [Getting started](getting_started.md)

- [Example](example.md)
