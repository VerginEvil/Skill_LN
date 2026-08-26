# Appendix B - StpCreatdll

This appendix illustrates the use of the Create Session DLL (ttstpcreatdll) session, which represents a tool for making a session DLL from a script of AFS functions calls.

The first three input fields,Package,Module, andSession,specify the session for which the Function Server DLL must be generated. Based on this information, a default name for the DLL is generated. This name is the full session code followed by anf. If you selected theAdd Package and Module to Function Name   check box, the DLL name includes the package and module of the session, for example, dtfsa2500m000. If you did not select this check box, the name does not include the names of the package and the module name, for example, 2500m000.

The generated functions of the session DLL always start with the name of this dll. Normally, a function must always start with a letter. However, if the DLL name does not start with a letter, this general convention is overruled and a function will start with a number.

After you generate a session DLL, you can find this DLL in the Maintain Scripts/Libraries session.
