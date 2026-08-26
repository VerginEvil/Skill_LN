# Public Layer
Methods in this library can be called from the outside world via the Baan Openworld. These methods will take care of the XML handling of the incoming messages and are therefore set oriented. The methods in the protected library are called for the actually retrieval/update of data.
The Public Layer is generated completely by the system, therefore the script is read-only.
The data communication between the layers is based on the getter/setter concept. This means that the 'calling' layer uses getter/setter functions from the 'called' layer to retrieve/send data.

## Related topics
- [Business Object Layer](overview.md)
- [Interface Conversion Public Layer](sc_layer.md)
- [Protected Layer](st_layer.md)
- [Interface Conversion Protected Layer](sm_layer.md)
- [Specific Methods Library](sf_layer.md)
