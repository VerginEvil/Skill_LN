# Introduction

The main goal of extensibility is to develop the last-mile functionality for your organization without changing the core standard software components. You use only the public interfaces of the standard application.

In this way, you can develop the extensions separate from the standard components. This leads to a situation that upgrading the standard software does not result in additional costs for upgrading customizations. Extensions “survive” the upgrades.

This table shows the types of extensibility in Infor LN:

| Type | Features | Tool |
|---|---|---|
| Personalize | Hide/unhide fields, add customer-defined fields, conditional LN standard, coloring, personalize menus and forms, suppress dialog boxes / through User Inter- messages, set defaults face. |  |
| Tailor | Add fields and logic to existing forms / BODs / web services; add LN Extension Mod- field hooks and commands to existing tables and forms; add eler secondary table to existing forms; add customer defined fields to existing IR push reports. |  |
|  | Note: Not all features are available in Infor LN 10.5.1. |  |
| Extend | Create new tables, domains, labels, screens, sessions, modules, LN Studio libraries, messages, etc. |  |
| Integrate | Create new BODs and web services, and call SOAP web services LN Studio from extensions |  |

## Supported LN versions

The extensibility concept is available with LN 10.5 or later, and with some limitations*) it is also available for LN 10.3 and 10.4.x if Enterprise Server 10.5 (Tools) is installed.

*) Limitations extensibility in 10.3 and 10.4.x:

- LN reports must be copied to own VRC, TIV-number must be increased to at Report extensibility: Native least 2020 and the report must be recompiled.

- Session extensibility: (Easy) filtering on additional form fields is not possible.

- BOD extensibility: The BODs must be on 10.5 level to be able to extend them. Check KB 22945150. The related KBs with “Extension Modeler” in the description are the ones that must be applied.

## Licensing

To use the full Extensibility features of LN the development license (product ID 10146) is required.

Without this development license, you cannot create new tables, domains and script components.
