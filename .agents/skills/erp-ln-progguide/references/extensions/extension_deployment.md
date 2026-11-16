# Extension Deployment

After extensions are developed, they can be exported from one environment and imported in another environment.

The same procedure must be used when extensions must be copied from one package combination to another package combination.

The Product Maintenance and Control (PMC) module must be used to create PMC solutions with the extensions. Use also PMC to install those solutions in the other environment.

See the Infor Enterprise Server Administration Guide.

## Exporting extensions

1 If not present, create a Base VRC with the Base VRC's (ttpmc0110m000) session that has your VRC for the extensions as Export VRC. 2 Create a PMC solution with the Solutions (ttpmc1100m000) session. 3 Add your component(s) to the PMC solution. If you add an extension script as a component, the extension data is added. 4 Generate dependencies. 5 Validate the solution. 6 View the report to see whether error messages are printed. If required, take corrective actions and repeat the previous step. Note that extensions that are being modified in an activity are reported as warnings. The committed versions of those extensions are exported. 7 Follow the standard PMC process to export and release the solution.

## Importing extensions

1 If not present, define an Update VRC with the Update VRC's (ttpmc2140m000) session for the Extensions package (tx). 2 Scan the PMC dump that was created with the export procedure. 3 Run the Check to Install from Process Solutions (ttpmc2101m000) session. 4 Check to install reports errors in case the extensions that are to be installed are being modified in the recipient environment. Warnings are reported for extensions that are changed in the recipient environment since the previous PMC install. 5 Complete the installation with the normal PMC process and execute the post-installation instructions.
