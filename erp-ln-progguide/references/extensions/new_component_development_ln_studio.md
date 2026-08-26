# New Component Development with Infor LN Studio

## Studio

You can create new components and new modules within the Infor LN application. The development of new components is done in Infor LN Studio.

See these guides:

- Application Development Guide Infor LN Studio

- Integration Development Guide Infor LN Studio

The topics that are described are relevant for developing extensions and specific configurations.

Before you start to use LN Studio for new component development in combination with Extensibility, read Configuration specifics on page 153.

## Infor LN Studio

Infor LN Studio is the Eclipse based development environment for Infor LN. Within the Extensions (tx) package you can create new components such as tables, sessions, messages, etc. The development of components in the tx packages does not differ from the normal Infor LN development. For extensions to be ready for the cloud, some restrictions apply.

This table shows the component types that can be developed:

| Component Type Remark |  |
|---|---|
| Session | Including the UI-script that handles the screen events. |
| Report | LN native reports can be developed, but no layouts can be defined. This report is a container of data: the report input fields define the fields that are available to be sent to Infor Reporting. The design of the report design is made in Infor Reporting ’s Report Studio . |
| Table | This is including the DAL that handles the table events. For the table fields standard domains can be used, but also new domains can be created. |
| Domain |  |
| Library |  |

Component Type Remark

Function

Menu

Label

Message

Question

Additional File

Business Object With an Integration Project.

For more information about Infor LN Studio and component development see these guides:

- Application Development Guide Infor LN Studio

- Integration Development Guide Infor LN Studio

## Configuration specifics

If you use LN Studio for the development of new components to be used in your extensions, the configuration should be done by the Extension Modeler. This applies to the configuration of the Base VRC, Development Environment, Application and Project. When you create the first activity in the Extension Modeler, the setup of a Base VRC, Development Environment, Application and Project are automatically done. Those are the ones you must also use in LN Studio.

This table shows the names of the various configuration items that are generated:

| Configuration | Name | Remark |
|---|---|---|
| Base VRC | B61O_a_ext | This is the default Base VRC generated in PMC. If you specify another VRC code during Initialize Extensibility, this VRC code is used as Base VRC. |
| Development Envi- EXT ronment |  | This value cannot be changed. |
| Application | EXT<package com- This value cannot be changed. bination> |  |
| Project | EXT<package com- This value cannot be changed. bination> |  |

This configuration applies to the Extensions package (tx) only. To combine classic customizations development (customization VRCs for the standard Infor LN packages) and extensibility. Specify a different VRC code for the Extensions package with a separate Base VRC. The classic customizations are in a separate Application and Project. By setting Activity Context you can link the activity for the Extensions and the activity for the classic customization. In LN Studio define Related Software Projects.

In LN UI go to Options > Debug and Profile 4GL
