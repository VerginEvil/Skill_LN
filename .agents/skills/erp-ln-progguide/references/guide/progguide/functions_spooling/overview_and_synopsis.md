# Spooling overview and synopsis

## Overview
Use these functions to handle printer devices and printing.

## Synopsis
| | | |
|---|---|---|
| `long` | [spool.buf()](spool.buf.md) | `( const string buffer(.), long length )` |
| `void` | [spool.close()](spool.close.md) | `( )` |
| `long` | [spool.line()](spool.line.md) | `( )` |
| `long` | [spool.open()](spool.open.md) | `( string reportname(15), string device(14), long mode )` |
| `boolean` | [spool.restore.variables()](spool.restore.variables.md) | `( [long brp.id] )` |

## Predefined variables
The following predefined variables are available for use with the spooler functions:
| | | |
|---|---|---|
| `long` | spool.date | Date to print. |
| `long` | spool.fontnumber | Font number: 1 LARGE 2 SMALL 3 MIDDLE |
| `long` | spool.id | Spooler ID. |
| `long` | spool.left.mrg | Left margin. |
| `long` | spool.pr.copies | Number of copies. |
| `long` | spool.pg.length | Length of page. |
| `long` | spool.pg.width | Width of page, including left margin. |
| `long` | spool.time | Time to print. |
| `long` | spool.view.rtl | Specifies whether the report is in a bidirectional language: true bidirectional language false non-bidirectional language |
| `string` | spool.device(14) | Name of spooler device. |
| `string` | spool.fileout(100) | Path name for spooler output file. |
| `string` | spool.paper.type(6) | Type of paper. |
| `string` | spool.pr.line(300) | Line to print. |
| `string` | spool.report(20) | Report to be printed. |
| `string` | spool.main.report(20) | The name of the report that must be used as main report. |
| `long` | spool.crn | Print to Production Reporting Services (if not 0). |
| `boolean` | spool.docman | Print to a Document Output Management device. |
| `long` | spool.orientation | Orientation of the paper type: 1 Portrait 2 Landscape |
| `long` | spool.pr.from | Print from page. |
| `long` | spool.pr.to | Print to page. |
| `long` | spool.preview | Show a preview of the print: 1 yes 2 no |
| `boolean` | spool.ssrs | Print to Microsoft SQL Server for Reporting Services. |
| `long` | spool.xml | Write an intermediate file in XML format (if not 0). |

## See also
[Reports overview and synopsis](../functions_reports/overview_and_synopsis.md)
