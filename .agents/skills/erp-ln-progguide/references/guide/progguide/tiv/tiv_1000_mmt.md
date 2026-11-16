# MMT Session
To support MMT (Multi-Main-Table) Sessions, the format of the compiled form has been changed for both the controller and the satellite form. The new compiled form can only be executed if the 4GL Engine supports TIV 1000 or higher. This also means that the TIV of the form needs to be 1000 or higher. At the moment the TIV of the form cannot be set directly. Instead you must set the TIV of the script attached to the session. If the session needs to be executed by an older version of the 4GLE the TIV number should not be set (TIV=0).

## Related topics
- [Tools Interface Version (TIV)](tiv_overview.md)

- [TIV level 1000](tiv_1000.md)
