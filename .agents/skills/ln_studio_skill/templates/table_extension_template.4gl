|*******************************************************************************
|* Extension Script for Table {target}
|* Author: {author}
|* Generated: {date}
|* Target Session: ttext1500m000 (Extension Modeler)
|* Note: Maintained in local Git repo. Do not edit in LN Studio SCM.
|*******************************************************************************

| Hook declarations
#context_on "declarations"
table   t{target}
#include <bic_dal2>
#include <bic_tableext>

| Common module-level declarations
#context_off

| Hook functions
#context_on "functions"
| Common validation and calculation helper functions
function extern boolean validate_custom_rule_{target}()
{
    return(true)
}
#context_off

| Hook method.is.allowed
#context_on "method.is.allowed"
function extern boolean method.is.allowed(long method)
{
    on case method
    case DAL_NEW:
        break
    case DAL_UPDATE:
        break
    case DAL_DESTROY:
        break
    endcase
    return(true)
}
#context_off

| Hook before.save.object
#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    | Business logic executed before saving object
    return(0)
}
#context_off

| Hook after.save.object
#context_on "after.save.object"
function extern long after.save.object(long mode)
{
    | Business logic executed after saving object
    return(0)
}
#context_off

| Hook before.destroy.object
#context_on "before.destroy.object"
function extern long before.destroy.object()
{
    | Business logic executed before deleting object
    return(0)
}
#context_off

| Hook after.destroy.object
#context_on "after.destroy.object"
function extern long after.destroy.object()
{
    | Business logic executed after deleting object
    return(0)
}
#context_off
