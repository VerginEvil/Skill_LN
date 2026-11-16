# Tree structures: example
#include <bic_event>
#include <bic_gc>
#include <bic_eis>
#define BUTN.ID.1 1
#define BUTN.ID.2 2
#define BUTN.ID.3 3
function main()
{
string tree.id(25)
string tree.title(80)
long process.id
tree.id = "exm"
tree.title = "Example Tree"
process.id = init.main.tree(tree.id, tree.title)
handle.event.loop()
exit.main.tree(process.id)
}
function long init.main.tree(string tree.id(25), string tree.title(80))
{
long process.id
|-- activate Tree Server
process.id = create.tree(tree.id, tree.title)
|-- create nodes
create.node(tree.id, "", "1", "Root", 1, process.id)
create.node(tree.id, "1", "1.1", "Root Child 1", 2, process.id )
create.node(tree.id, "1", "1.2", "Root Child 2", 2, process.id )
create.node(tree.id, "1", "1.3", "Root Child 3", 3, process.id )
create.node(tree.id, "1.1", "1.1.1", "Root Child 1.1", 3, process.id)
create.node(tree.id, "1.1", "1.1.2", "Root Child 1.2", 1, process.id)
create.node(tree.id, "1.2", "1.2.1", "Root Child 2.1", 1, process.id)
create.node(tree.id, "1.2", "1.2.2", "Root Child 2.2", 2, process.id)
create.node(tree.id, "1.3", "1.3.1", "Root Child 3.1", 1, process.id)
|-- create buttons
create.tree.button(tree.id, BUTN.ID.1, "Button 1", process.id)
create.tree.button(tree.id, BUTN.ID.2, "Button 2", process.id)
create.tree.button(tree.id, BUTN.ID.3, "Button 3", process.id)
|-- change default colors
set.tree.background(tree.id, RGB.WHITE, process.id)
set.tree.foreground(tree.id, RGB.BLACK, process.id)
set.node.class.color(tree.id, 1, RGB.GREEN, process.id)
set.node.class.color(tree.id, 2, RGB.YELLOW, process.id)
set.node.class.color(tree.id, 3, RGB.RED, process.id)
|-- show root node with 2 underlying levels
view.tree(tree.id, "1", 3, process.id)
|-- return new process id
return(process.id)
}
function void exit.main.tree(string tree.id(25), long process.id)
{
|-- kill Tree Server
destroy.tree(tree.id, process.id)
}
function void handle.event.loop()
{
long event(EVTMAXSIZE)
long process.id
long button.id
string node.id(25)
while ( TRUE )
next.event(event)
on case evt.type(event)
case EVTBUCKETMESSAGE:
on case evt.bms.command(event)
case MSG.PUSH.BUTTON:
get.tree.push.button(event, process.id, button.id,
node.id)
on case button.id
case BUTN.ID.1:
.
.
break
.
.
endcase
break
case MSG.NODE.PRESS:
get.tree.node.press(event, process.id, node.id)
.
.
break
case MSG.NODE.DPRESS:
get.tree.node.dpress(event, process.id, node.id)
.
.
break
default:
get.tree.default()
break
endcase
break
.
.
endcase
endwhile
}

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)
