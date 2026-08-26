# Message handling overview and synopsis

## Overview
Use these functions for handling status messages, error messages, and other messages that are output to the screen or to a log file.
4GL programs (except type 4 programs) usually display a status area consisting of several status fields. 4GL programs can display messages in the first field (see the *status.mess()* function below).

## Synopsis

## Statusfield messages
Use these functions to handle message display in the first status field of the statusbar.
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [status.del()](status.del.md) | `( )` |
|  | [status.mess()](status.mess.md) | `( string strg(15) )` |

## Statusbar messages
Use these functions to handle message display in the statusbar.
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [clean.mess()](clean.mess.md) | `( )` |
|  | [mess()](mess.md) | `( string messcode(14), long separate_window [, arg, ...] )` |

## Displaying messages
Use these functions to display messages in a separate window.
```
void
```
```
void
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [mess()](mess.md) | `( string messcode(14), long separate_window [, arg, ...] )` |
|  | [message()](message.md) | `( string mess_str [, arg, ...] )` |
|  | [set.input.error()](set.input.error.md) | `( string mess.or.code [, ...] )` |
|  | [show.dal.messages()](show.dal.messages.md) | `( [long i.type] )` |

## Dal messages
Use these functions to set and retrieve DAL messages.
```
void
```
```
long
```
```
boolean
```
```
boolean
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
long
```
```
long
```
```
string
```
```
long
```
```
long
```
```
string
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [dal.clear.messages()](dal.clear.messages.md) | `( long i.type )` |
|  | [dal.count.messages()](dal.count.messages.md) | `( long i.type )` |
|  | [dal.get.last.message()](dal.get.last.message.md) | `( long i.type, ref string o.code, ref string o.text, [ref long o.type] )` |
|  | [dal.get.first.message()](dal.get.first.message.md) | `( long i.type, ref string o.code, ref string o.text, [ref long o.type] )` |
|  | [dal.peek.message()](dal.peek.message.md) | `( long i.type, long i.index, ref string o.code, ref string o.text, [ref long o.type] )` |
|  | [dal.reset.messages()](dal.reset.messages.md) | `( long i.type, long i.count )` |
|  | [dal.set.message()](dal.set.message.md) | `( long type, const string i.mess.or.code [, arg, ...] )` |
|  | [dal.set.messages.off()](dal.set.messages.off.md) | `( )` |
|  | [dal.set.messages.on()](dal.set.messages.on.md) | `( )` |
|  | [dal.clear.error.messages()](dal.clear.error.messages.md) | `( )` |
|  | [dal.count.error.messages()](dal.count.error.messages.md) | `( )` |
|  | [dal.get.error.message()](dal.get.error.message.md) | `( ref string o.text )` |
|  | [dal.get.error.msgcode()](dal.get.error.msgcode.md) | `( )` |
|  | [dal.get.first.error.message()](dal.get.first.error.message.md) | `( ref string o.text, ref string o.code )` |
|  | [dal.peek.error.message()](dal.peek.error.message.md) | `( long i.index )` |
|  | [dal.peek.error.msgcode()](dal.peek.error.msgcode.md) | `( long i.index )` |
|  | [dal.reset.error.messages()](dal.reset.error.messages.md) | `( long i.count )` |
|  | [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](dal.set.error.message.md) | `( const string i.mess.or.code [, arg ...] )` |

## General
Use this function to retrieve a message from the Data Dictionary.
```
string
```
| | | |
|---|---|---|
|  | [form.text$()](form.text.md) | `( string messcode(14) [, string language code] )` |
Use this function to add an extra button to a message/question
```
long
```
| | | |
|---|---|---|
|  | [add.message.button()](add.message.button.md) | `( string messcode(14), string buttonLabel, string library, string function )` |
