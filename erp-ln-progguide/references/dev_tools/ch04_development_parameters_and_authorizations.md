# Chapter 4: Development Parameters and Authorizations

## Development parameters and authorizations

To maintain or create software components, a developer requires default development settings and
parameters and authorization to at least one package VRC.
### Development Parameters

The settings and parameters a developer needs, are defined in a Development Parameters template.
Parameters are available for the following:
- Automatic compilation to the run-time data dictionary after changes to forms or menus
- Actions to be performed automatically after the Copy to Current Package VRC option
- The parameters that the editor can use to develop software
To create the Development Parameters template, you must use the Development Parameters Template
(ttams1150m000) session. On the session's appropriate menu, click Convert Changes To Runtime
DD to convert the changes to the runtime data dictionary.
The template contains data a group of users share. However, the template is linked to individual users.
To link the template to a user, you must use the User Data (ttaad2500m000) session. Do not forget to
convert the changes to the runtime data dictionary. You must log off and log on again to make all changes
effective.
For more information, refer to the Infor Web Help.
> [!NOTE]
For every LN user, the data in this template is dumped to LN ’s run-time data dictionary in the User
Application Parameters (ttadv010) table.
### Developer Authorizations

A developer needs authorization for at least one package VRC.
To define developer authorizations for a user, you can:
- Link the user to a Developer Authorization template.
- Give authorization for all package VRCs.
Developer Authorization Template
The VRCs a developer is authorized for are defined in a Developer Authorization template.
You can use this template to define some of the authorizations for developers who must customize LN
software components.
In this template, you can specify:
- The package VRC(s) for which the developer must be authorized to customize and develop
- The languages and modules of the specified package VRC for which the developers must be
software components. This specific package VRC overrides the Auth for all Package VRCs
check box in the User Data (ttaad2500m000) session.
authorized to customize and develop software components.
To create the developer’s authorization template, you must use the Developer Authorization Template
(ttams1151m000) session. This session is password-protected. You can only use this session if you
have system administrator’s rights. Points of attention:
- If you select the All Modules and All Languages check boxes in this template, the users who
are linked to the template are authorized to maintain and develop software components in all
modules in LN and in all languages. If the check boxes are cleared, you must specify the
specific modules and languages for which the user must be authorized.
- If you select the Authorization for Components of other Developer check box in this
- On the session's appropriate menu, click Convert Changes To Runtime DD to convert the
template, the user is authorized to maintain the software components that are created by other
users. This option is helpful, for example, for a senior application developer.
changes to the runtime data dictionary.
The template contains data a group of users share. However, the template is linked to individual users.
To link the template to a user, you must use the User Data (ttaad2500m000) session. Do not forget to
convert the changes to the runtime data dictionary. You must log off and log on again to make all changes
effective.
For more information, see the Infor Web Help.
> [!NOTE]
The data in this template is dumped to LN ’s run-time data dictionary for each individual LN user to the
Version Authorizations by User (ttadv041) table.
Authorization for all package VRCs
Some users, for example an application administrator, require authorization for all package VRCs.
To give authorization for all VRCs, start the User Data (ttaad2500m000) session and modify the user
data as follows:
- Select the Auth for all Package VRCs check box.
- Ensure the Developer Authorizations field is blank.
Convert the changes to the runtime data dictionary, and log off and log on again to make the changes
effective.
> [!NOTE]
If you link the user to a Developer Authorization Template, the user will no longer be authorized for all
package VRCs, but only for the VRCs defined in the template.
