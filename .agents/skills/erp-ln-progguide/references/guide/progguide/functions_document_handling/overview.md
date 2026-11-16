# DMS Document handling API
The DMS Document handling API defines the functions that can be used by extensions to query a DMS for documents, to download documents, to upload documents or even to delete documents. Documents can be handled via the Document Hub or directly in IDM. For each route a different set of functions is available.

## Document Hub setup
The Document Hub hides the DMS details from the extension. Before using the Document Hub it must be configured. To configure execute the following steps

- Start session Document Mapping (ttdms3550m100)

- Go to Application named infor.ln.ext. When no applications are present execute the form command named Initialize Document Hub.

- The documents to be handled must be related to an LN table. Add the table in the top left session called Application Tables.

- Select the added table and add a document type in the bottom left session called Document Types.

- Set the download and/or upload flag of the document type.

- In the Attribute Mapping session on the right, a default mapping is filled. Check this mapping. Now document handling for the selected table via the Document Hub is available for extensions.

The API will be exposed via include bic_dms which must be included in the declaration hook of the extension with #include <bic_dms>
Two sets of functions are available, one for document handling via the Document Hub and one directly with IDM.

## Related topics
- [Document handling via Document Hub synopsis](dochub_synopsis.md)

- [Document handling in IDM synopsis](idm_synopsis.md)
