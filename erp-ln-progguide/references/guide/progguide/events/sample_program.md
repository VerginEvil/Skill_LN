# Events sample program
```

long event(EVTMAXSIZE)

while TRUE
	next.event(event)

	on case evt.type(event)
	case EVTKEYPRESS:
		on case evt.keypress.key(event)
		case KEY_RETURN:
				....
		case KEY_ESC:
				....
				break
		endcase
		break

	case EVTCHANGEFOCUS:
		on case evt.focus.key(event)
		case KEY_TAB:
		case KEY_DOWN:
				| set focus on next field
		case KEY_BACKTAB:
		case KEY_UP:
				| set focus on previous field
		endcase
		break

	case EVTBUTTONSELECT:
		if ( evt.button.return(event) = ABORT.BUTTON ) then
			| ABORT.BUTTON is the return value of the button pressed
			return
		endif
		break
	endcase
endwhile
```

## Related topics
- [Events overview](overview.md)
- [Events synopsis](synopsis.md)
- [Event types](event_types.md)
- [Event array parameters](event_array_parameters.md)
- [Events sample program](sample_program.md)
