# Using a Progress Indicator
Using a [Progress indicators overview and synopsis](../functions_progress_indicators/overview_and_synopsis.md)) for session activities which can last more than 5 seconds to complete is strongly recommended. The benefits of a progress indicator are twofold:
- Improved user experience: the end used al least gets feedback that the command is being executed; in addition, the progress indicator may be updated to show the amount of work completed and remaining.
- Avoiding communication errors: in LN UI, not using a progress indicator may trigger the browser's receive timeout and subsequent error message "Connection with web server broken".
