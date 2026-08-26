# Monitoring overview and synopsis

## Overview
Monitoring in LN allows for reporting events to the Infor Monitoring environment. An API is provided, which allows for specifying events and sending messages reporting these events to a url.
The messages send to the url are conform the *InfluxDb* line protocol, the datamodel used in the API is based upon the syntax of these messages.
The url the messages are send to is expected to be the http-listener of the locally installed *Telegraf*, but can belong to any proces which is able to handle *InfluxDb* line protocol (e.g. *InfluxDb*). When another proces is targeted, or when *Telegraf* listens on a different port, an alternative url can be configured. The messages are send unencrypted, when encryption is required this can be provided by *Telegraf*.
The messages are send asynchronously, so the flow of the session is not interrupted. Success of triggering an event indicates the message will be send. When the actual sending fails, a bshell message will be generated, but this falls outside the flow of the sending session. When messages are generated faster as they can be send, they will be combined into larger messages going to the same url.

## Monitoring Events
Monitoring events are prepared by defining an event class. Several types of attributes can be added to an event class:
-  Tags A tag is an identifying attribute of an event. It is always of type string. All events of a certain class have the same value for a tag. By default a number of tags are added to each event class, as defined by the *monitor_tags* resource.
-  Fields A field is a non-identifying attribute of an event. It can be of type string, long, boolean or double. All events of a certain class have the same value for a field.
-  Metrics A metric is a non-identifying attribute of an event. It can be of type string, long, boolean or double. For each event of a certain class the value for a metric must be provided. When no value for a defined metric is provided, the metric will not be represented in the message send to the monitoring system.    After a class has been prepared, events of this class can be triggered. The values for the metrics to be represented in the message generated, have to be provided.

## Monitoring Intervals
Monitoring intervals are a special type of monitoring events. In addition to the configured tags, fields and metrics an additional metric ( *duration*) is present. This duration is the time (in seconds with millisecond granularity) between the start of the interval and the actual creation of the message at the end of the interval. The value of this metric is generated automatically.

## Resources
Several resources are defined in lib/defaults/all.
| | | |
|---|---|---|
| name | default value | description |
| *monitor_enable* | 0 | When defined, switches monitoring on. By default, monitoring is off. |
| *monitor_trace* | 0 | When defined, switches tracing of monitoring messages on. By default, monitor tracing is off. |
| *monitor_url* | *localhost:8186* | The URL the events will be send to. |
| *monitor_tags* | "" | A comma seperated list of tags that will automatically be added to each monitoring event. Each tag will be declared as '<name>=<value>' The names of the tags must consist of printable 7-bit ascii characters, but may not contain a newline, a ',' or an '='. The values of the tags defined may contain environment variables, like '${BSE}'. These variables will be resolved when a monitor event/interval class is defined. They may not contain a newline or a ','. By default no tags are defined.  |

## Synopsis
In addition to the possible errors returned by these functions, they all can return monitor_general_error as well. This indicates a not monitor specific error and its exact nature may be examined by viewing logs and traces.
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [monitor_define_event_class](monitor_define_event_class.md) | `( const string event_class_name )` |
|  | [monitor_add_tag](monitor_add_tag.md) | `( long event_class_id, const string tag_name, const string tag_value )` |
|  | [monitor_add_field](monitor_add_field.md) | `( long event_class_id, const string field_name, void field_value )` |
|  | [monitor_add_metric](monitor_add_metric.md) | `( long event_class_id, const string metric_name, long metric_type )` |
|  | [monitor_event](monitor_event.md) | `( long event_class_id, ... )` |
|  | [monitor_remove_event_class](monitor_remove_event_class.md) | `( long event_class_id )` |
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [monitor_define_interval_class](monitor_define_interval_class.md) | `( const string interval_class_name )` |
|  | [monitor_start_interval](monitor_start_interval.md) | `( long interval_class_id )` |
|  | [monitor_stop_interval](monitor_stop_interval.md) | `( long interval_id[, ...] )` |
|  | [monitor_remove_interval](monitor_remove_interval.md) | `( long interval_id )` |
|  | [monitor_remove_interval_class](monitor_remove_interval_class.md) | `( long interval_class_id )` |

## Errors
A list with all valid error messages, that can be returned by monitoring functions, can be found in [Monitoring errors.](errors.md).
