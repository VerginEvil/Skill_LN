# Communication with STP and CDAS
Infor Enterprise Server provides the following functions to enable the 4GL engine and external applications to retrieve and display DAL error messages:
- [dal.clear.error.messages()](../functions_message_handling/dal.clear.error.messages.md)
- [dal.count.error.messages()](../functions_message_handling/dal.count.error.messages.md)
- [dal.get.error.message()](../functions_message_handling/dal.get.error.message.md)
- [dal.get.first.error.message()](../functions_message_handling/dal.get.first.error.message.md)
- [dal.reset.error.messages()](../functions_message_handling/dal.reset.error.messages.md)
- [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](../functions_message_handling/dal.set.error.message.md)  You use *dal.set.error.message()* to specify a message to be displayed when the DAL returns an error (that is, a negative value). This function is called in the DAL script and not in the UI script.
You can call *dal.get.first.error.message()* or *dal.get.error.message()* to retrieve DAL messages.
The following example illustrates the use of these functions in a UI script:
```

    db.retry.point()

    nr.of.errors = dal.count.error.messages()
    if db.retry.hit()  then
        | Remove the error messages since the last commit
        dal.reset.error.messages(nr.of.errors)
    endif
    ...
    ...
    commit.transaction()
    nr.of.errors = dal.count.error.messages()
    ...
    commit.transaction()
    while dal.get.error.message(message) >= 0
        report.message(message)
    endwhile
```

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [UI, DAL, and STP interaction](dal_ui_and_stp_interaction.md)
- [Transition issues (BAAN IV to Infor Enterprise Server)](transition_issues_baan_iv_to_baanerp.md)
