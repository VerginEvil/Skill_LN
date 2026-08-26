# Monitoring errors.
All monitor functions return a long. When this result is greater than or equal to zero, the function succeeded. When it is less than zero the function failed. Possible error codes are:
-  *monitor_not_enabled*
The current configuration will not send any messages to the monitoring system. No event/interval class has been created.
-  *monitor_error_invalid_class_name*
The name provided contains characters which are not allowed.
-  *monitor_error_unknown_class*
The event/interval class id doesn’t identify a valid class.
-  *monitor_error_invalid_tag_name*
The name provided contains characters which are not allowed.
-  *monitor_error_invalid_tag_value*
The string value provided contains characters which are not allowed.
-  *monitor_error_invalid_field_name*
The name provided contains characters which are not allowed.
-  *monitor_error_invalid_field_type*
The type provided isn’t one of the defined monitor field types.
-  *monitor_error_invalid_field_value*
The value provided can’t be used, e.g. a string value containing a newline character.
-  *monitor_error_unknown_interval*
The interval id doesn’t identify a valid interval.
-  *monitor_error_unknown_field*
The metric name provided in an event is unknown for the monitor event class.
-  *monitor_error_missing_field_value*
The argument providing the metric value is missing.
-  *monitor_error_field_value_of_wrong_type*
The type of the value provided doesn’t correspond to the type specified for this metric.
-  *monitor_general_error*
Function failed, see logs/traces for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)
