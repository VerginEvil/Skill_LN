# Chapter 3: Data Dictionaries

## Data dictionaries

A data dictionary is a collection of descriptions about a data model or system. LN uses two unique data
dictionaries: the Runtime Data Dictionary and the Application Data Dictionary.
This section describes the purpose of the Runtime Data Dictionary, the purpose of the Application Data
Dictionary, and how you convert data from the Application Data Dictionary to the Runtime Data Dictionary.
### The Runtime Data Dictionary

The Runtime Data Dictionary (RTDD) refers to the files and data that are used to run the system, hence
the term “runtime”. The purpose of the RTDD is two-fold:
- Provides configuration information to the technical architecture. This is also called the runtime
- Provides optimized application information when the application is running.
environment.
Configuration Information
The RTDD is necessary because the system is configurable in its technical architecture. If this
configuration information were stored in a database, the system would not know how to get this
information, or from what database to get it. The system would not know the language to present any
messages, or the programs it should start to support the system. To address these issues, information
is available from the application server’s operating system during the bshell startup procedure.
Optimized Application Information
The application repeatedly requires a lot of information about the application components that are
running. While this information could come from a database, because the information may be required
frequently, and changes are infrequent, it is faster and more efficient to pre-process this information and
store it in a compressed and optimized way. Examples of this type of information are date formats,
menus, toolbar texts, menus and forms. Application components like forms, form fields, and labels are
stored in a database. To gather all the information from a database when it is needed by a running
system would slow down the system. Therefore, the system uses a convert function to compile this
information into an optimized format.
### The Application Data Dictionary

While the runtime data dictionary is stored in the application server’s operating system and some
Enterprise Server tables, the Application Data Dictionary (APDD) is data stored in tables. The APDD
data is accessed by sessions.
By having the APDD stored as data and accessible in the sessions, this allows administrators to easily
administer the system using sessions, and allows developers to easily develop applications in the system.
In this way, the application administration environment and application development environment are
fundamentally the same as the application execution environment.
The APDD data is stored in company number 000.
### Convert to Runtime Data Dictionary

After the application data dictionary data is maintained in the sessions, the information intended for the
RTDD must be extracted from the APDD, reformatted or optimized and made available in the runtime
data dictionary. This process is called “Convert to Runtime”.
The optimized information is in one of these formats:
- File on the operating system.
- Compressed data in a table.
- Directly Available: A conversion step is not necessary because the system will access the
- Convert (to Runtime): This type of conversion takes information out of the APDD, and creates
- Compile or Dump: Usually performed by programmers, this type of conversion takes information
The categories of making the APDD available at runtime include:
data directly from the APDD.
files in the application server’s operating system.
out of tables and script files, and stores them in an optimized and encrypted format, called an
object or component, at the operating system level.
How do you know when a convert to runtime is required? This can be a difficult question. The most
effective way is to see if the session has a convert to runtime button or a pull down menu item under
the Specific menu. A convert to runtime is required, for example, for Package Combinations, Tables
and Domains.
Other entities require a compile step to make the APDD information available for use. Usually, compile
steps do not require signing out of the system (a change to the users start menu is a notable exception).
Compilation is required, for example, for:
- Menus
- Labels
- Sessions and Forms
- Reports
- Scripts and libraries
Convert to Runtime Sessions
There is a number of Convert to Runtime sessions that is used during software development. Usually,
you can initiate a convert to runtime for an entity from the Specific menu in the session that maintains
that entity.
When more than one entity requires conversion, or when more than one element in an entity changes,
you can use a conversion session that is accessible from the menu browser. For example:
Session
Description
### Convert to Runtime Data Dictionary

(ttadv5215m000)
The convert to runtime data dictionary in Application
Development performs specific processing on the
Table Definition and Domain files associated with
the Package Combination. The table and domain
definition files contain information about the table’s
fields and data types. If this format changes, a field
is added to a table and the table definition changes.
However, the physical table that has data needs to
adhere to this definition. Because of the requirement
that the definition and physical table be in sync with
each other, a reconfiguration process (`crdd`) performs the
changes on the physical table.
The system knows what table definitions have
changed because the table definitions session adds
an indicator entry in a table called Conversion Indicators (ttadv500). When a new table definition replaces an existing table definition, the change is
actually pending until a table reconfiguration process is done. A table reconfiguration process is
known to the system by an entry in the Reconfiguration Indicators (ttadv501) table.
The convert to runtime process will look at the indicators table to determine what tables to convert.
This session will not convert session data.
Create Runtime Data Dictionary (ttadv5210m000 )This session performs the same task as the Convert to Runtime Data Dictionary (ttadv5215m000)
session, with these notable differences:
- The session creates table/domain definition
files even if no changes have been made.
Therefore, the indicator table is not checked
as in the Convert to Runtime Data Dictionary (ttadv5215m000) session.
- The session creates session entries in the
runtime data dictionary table (ttadv999). This
table is accessed when a session starts up.
This session is used after changes affecting the
system such as importing data dictionary. The import data dictionary function is able to import application data dictionary components, and is a way to
move components from one system, such as a development server, to another server.
