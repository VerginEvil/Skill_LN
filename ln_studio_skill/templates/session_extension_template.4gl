|*******************************************************************************
|* Extension Script for Session {target}
|* Author: {author}
|* Generated: {date}
|* Target Session: ttext1500m000 (Extension Modeler)
|* Note: Maintained in local Git repo. Do not edit in LN Studio SCM.
|*******************************************************************************

| Hook declarations
#context_on "declarations"
#include <bic_sessionext>

| Common module-level declarations
#context_off

| Hook functions
#context_on "functions"
| Common helper functions for session commands
function extern void helper_action_{target}()
{
}
#context_off

| Hook function.custom.action.is.enabled
#context_on "function.custom.action.is.enabled"
function extern boolean function.custom.action.is.enabled()
{
    return(true)
}
#context_off

| Hook function.custom.action.before.command
#context_on "function.custom.action.before.command"
function extern void function.custom.action.before.command()
{
    | Logic executed before command runs
    | Call choice.again() to cancel command execution
}
#context_off

| Hook function.custom.action.after.command
#context_on "function.custom.action.after.command"
function extern void function.custom.action.after.command()
{
    | Logic executed after command completes
}
#context_off
