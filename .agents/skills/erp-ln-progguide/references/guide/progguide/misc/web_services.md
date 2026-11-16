# Web Services from Infor Enterprise Server
Using a Web Service from Infor Enterprise Server comprises two steps: first generate an Infor Enterprise Server library that provides functions to invoke the Web Service. Then, write your own functions to use these functions from the generated library.

## Generate Infor Enterprise Server library code
In Application Studio (build 8.6.0.0178 or later), you can generate Infor Enterprise Server library code from a WSDL (Web Service Description Language) file. In the editor, select option "Generate Source from WSDL" with the right mouse button. Select the WSDL file and the Infor Enterprise Server library code is generated.

## Use the generated Infor Enterprise Server library code
To use the generated Infor Enterprise Server library, you need to call the following functions from that library to carry out the following steps:

- Instantiate service

- Build the request data

- Execute the service

- Get the response data

- Cleanup

This is illustrated by the following code example for a simple WSDL (Currency Convertor from http://www.webservicex.net):
```

long    service     | XML
long    request     | XML
long    response    | XML
long    retval
double  rate
string  err.mess(100)

| instantiate the service
service = CurrencyConvertor.New()
CurrencyConvertor.SetCredentials(service, "john" "Ek5%aPy") | user and password

| build up request
request = ConversionRate.parameter.New()
ConversionRate.parameters.SetFromCurrency(request, Currency.EUR()) | uses generated wrapper for Enum domain Currency
ConversionRate.parameters.SetToCurrency(request, Currency.USD())

| executes the operation via SOAP
retval = CurrencyConvertor.ConversionRate(service, request, response)

| gets the values from response
rate = ConversionRateResponse.parametersResponce.GetConversionRateResult(response)

| if an error occurs:
err.mess = CurrencyConvertor.GetErrorMessage(service)

| cleanup
ConversionRate.parameters.Delete(request)
ConversionRateResponse.parametersResponse.Delete(response)
CurrencyConvertor.Delete(service)
```

## Complex structures
For a more sophisticated WSDL, functions are generated to build up XML structures to be used in the request and functions to read XML structures from the response. The generated Infor Enterprise Server library contains sections "Functions to create XML object" and "Functions to retrieve properties from XML object".

## Create XML Object
To create an XML object to use it in the request (or as property for another XML object), do the following:

- Call the constructor

- Sets the properties

Code example:
```

long    param   | XML
param = ParameterValue.New()
ParameterValue.SetName(param, "Age")
ParameterValue.SetValue(param, "17")
```
For collections, do the following:

- Call the constructor

- Call the Add function for every instance to be added

Code example:
```

long param.coll | XML
param.coll = Parameters.New()
Parameters.AddParameterValue(param.coll, param) | adds the parameter from the previous example
```
It is not needed to include the cleanup in your code, because the XML object is automatically deleted when the request for which it is used is cleaned up.

## Retrieve from XML Object
To retrieve data from an XML object from the response (or from another XML object), call the getter for every property that is needed. The getter has name *Objectname*.Get *Property*, e.g. ValidValue.GetLabel. The getter functions come in two flavors:

- For mandatory fields, it only has the XML object as argument and returns the property value.

- For optional fields, it has the XML object as input argument and the property value as output argument. It returns a boolean indicating if the property is present within the XML structure.

Code example:
```

long     value      | XML containing a ValidValue
string   name(100)
string   label(100)
name = ValidValue.GetName(value) | Name is mandatory
if ValidValue.GetLabel(value, label) then | Label is optional
        ... | do something with label
endif
```
For collections:

- Call the get first function: this will retrieve the first element from the collection

- Call the get next function repeatedly until the return value = 0

Code example
```

long    response    | XML containing the response from ReportExecutionService
long    value.coll  | XML
long    value

if ReportExecutionService.GetArrayOfValidValue(response, value.coll) then
        value = ArrayOfValidValue.GetFirstValidValue(value.coll)
        while value <> 0
                ... | do something with 'value'
	              value = ValidValue.GetNextValidValue(value)
        endwhile
endif
```
It is not needed to include the cleanup in your code, because the XML object is automatically deleted when the response for which it is used is cleaned up.
