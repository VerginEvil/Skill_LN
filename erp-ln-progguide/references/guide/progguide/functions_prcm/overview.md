# Process Change Manager overview
The Process Change Manager (PRCM) offers a generic mechanism that allows a 3GL process to notify one or more other 3GL processes about a certain state change.
A good example would be one or more sessions that should refresh their data as soon as another session has done updates in a certain database table. The session that performs these table updates, has to inform the others about this in one way or another. PRCM allows you to do this.
PRCM is very useful in the following cases:
- A change in one process requires changing others, but you don't know how many processes need to be informed.
- When a process should be able to notify other processes without having to know these processes.   In the example above, the session that notifies the other sessions does not have to know which sessions should be notified. It also does not have to know how many sessions have to be notified.

## Design and implementation
PRCM is based on the so-called Observer Design Pattern (also known as Publish-Subscribe). It works as follows:
Processes can have an Observer role, and/or a Subject role. Observers register (i.e. subscribe) themselves for a certain Subject. By registering themselves, Observers indicate that they want to be informed about state changes in the Subject. If a Subject changes, it will notify all interested Observers about that change. Observers then decide whether and how they react on the notification.
PRCM is implemented in such a way that Observers and Subjects do not communicate with each other directly, but via a so-called Change Manager. This Change Manager keeps track of all registrations and peforms the notification of all Observers on behalf of the Subject.

## Automatic notification of maintable updates
Informing other sessions about updates done on the maintable is perhaps the most obvious application of the Process Change Manager functionality. For this reason, the 4GL engine automatically notifies sessions when the maintable has been updated via choice UPDATE.DB. (In case the session performs updates directly on the maintable then the session should notify other session itself).
The 4GL engine notifies other sessions by calling [prcm.notify()](prcm.notify.md), passing the main table code to it, e.g. prcm.notify("tccom100") for Business Partners. Sessions that are interested in changes in the maintable, have to register themselves in order to be notified. For implementation details see the [Process Change Manager Code Examples](examples.md) section.
Note  Do not call [prcm.notify()](prcm.notify.md) for the maintable in the *after.update.db.commit* section or the [after.commit.transaction()](../functions_dal/after.commit.transaction.md) hook of the DAL of the maintable, as this interferes with the automatic notification of the 4GL engine.

## Related topics
- [Process Change Manager synopsis](synopsis.md)
- [Process Change Manager Code Examples](examples.md)
