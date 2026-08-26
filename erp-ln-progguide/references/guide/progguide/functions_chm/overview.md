# Chart manager overview
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use the chart functions in the Programmable Dialogs API.
The Business Chart Manager is a tool that displays data graphically, in charts. The Business Chart Manager supports a variety of chart types, including, pie, line, symbol, high-low, and layer. The input can consist of data from a database, a file, or some other appropriate source.
In this document, the term *graph* refers to a chart drawn within a coordinate system with two or more axes. The term *pie* refers to a circular chart, divided into segments, which illustrates the quantitative relationship between different groups of data.

## Example
This example illustrates how the Business Chart Manager builds a chart.

## Source data
The following figures represent the quantity of goods sold per month by three different companies.
| | | | |
|---|---|---|---|
|  | Company 1 | Company 2 | Company 3 |
| Jan | 40 | 30 | 10 |
| Feb | 20 | 25 | 15 |
| Mar | 20 | 40 | 10 |
| ... | ... | ... | ... |
| Dec | 30 | 35 | 20 |
The Business Chart Manager organizes this data into twelve categories (one for each month) and three series (one for each company). The data value for a particular data category and data series can be represented as a data point in a chart.

## Axis-oriented graph
The sample data illustrated above can be plotted on a single axis-oriented graph. In the Business Chart Manager, a graph can has up to four axes, as follows:
category axis – x-axis
data axis – y-axis
series axis – z-axis
data axis II – second y-axis
The x-axis represents the data categories (in this case, the months) against which each data value is plotted. The y-axis represents the value scale against which each data value is plotted. The values for each data series (in this case, the different companies), are differentiated in a variety of ways, depending on the chart type used. In a line graph, a line joins the data values for a particular series. The various series can be differentiated by using different line types and/or colors. On a bar graph, a vertical or horizontal bar represents each data value. Bars representing the same series have the same color, pattern, and width.
The data axis II is used in combination with data axis I when two (or more) different series must be drawn on different scales in order to facilitate comparison.

## Pie Chart
A pie chart can represent only a single data series. The sample data illustrated above can be represented by either twelve or three pie charts, depending on whether the data is sorted by category or series:
| | |
|---|---|
| Sorted by category |  Each pie chart illustrates the relationship between the different series (that is, the companies) for one category. This results in twelve pie charts, one for each category (that is, month). Each diagram has three segments, representing the three data series. The size of each segment is proportional to the value of the data point in relation to the total in the category (month). This option facilitates comparison of the three companies for each month.  |
| Sorted by series |  Each pie chart illustrates the different category values within one series (that is, a company). This results in three pie charts, one for each company. Each diagram has twelve segments, representing the twelve categories. The size of the segments depends on the data value of each category as a percentage of the total of all data values in the series.  |

## Related topics
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
