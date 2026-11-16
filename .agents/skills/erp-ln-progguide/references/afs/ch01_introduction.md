# Chapter 1 Introduction

This document is designed to serve as a Reference Guide for the Application Function Server (AFS). This document covers both the architecture of, and programming with, the AFS. After reading this document, the reader will have the necessary knowledge to modify existing AFS code and to create new AFS code.

This document also describes the restrictions for Baan 4GL application sessions, which the user must bear in mind during the development and maintenance of these Baan 4GL application sessions. For this reason, you must also use this document when you build new (standard) applications, even if it is not clear yet that the AFS is going to be used together with those new applications.

## Scope

This document is intended for experienced Infor ERP programmers only. No attempt is made to explain Baan 4GL programming or Infor ERP architecture outside of what is required for the AFS.

The document applies to ERP Baan IV, ERP Baan5.x, and ERP Enterprise (LN)1 in general. However, the implementation and the use of the AFS can differ. When applicable, these differences are noted in the text.

## Definitions, acronyms, and abbreviations

Term             Description

AFS Application Function Server: Not to be confused with the DDC, or Distributed Data Collection, Function Servers, this is another type of technology.

Because the AFS is related to the Tools version, this document applies to the Tools versions B40c (for Baan IV), B50b, 7.1a and 7.3a (for ERP Baan), and Infor Enterprise Server (LN). For future versions and releases this document may need modifications. Term             Description

AFS-DLL An Infor ERP DLL that contains the calls to the API-handler for a specific Baan 4GL application session.

API Application Programming Interface.

API-handler The program that serves outside the application to call the functionality of the Baan 4GL application sessions.

BCBE Baan Connection Basic Edition: This technology is replaced by OpenWorldX, which is now called the Open Architecture Adapter Suite.

BOI Business Object Interface.

DAL Data Access Layer (DAL): The software layer in Infor ERP systems that contains all data manipulation rules, such as the authorization for modifying, removing, or adding data, and all related constraints. This software layer also includes all rules required to maintain data consistency.

ERP Enterprise Resource Planning (ERP) is a business management system that integrates all aspects of the business, including planning, manufacturing, sales, and marketing.

FS Function Server: This term is sometimes used to refer to AFS.

Infor ERP Infor ERP is a generic term for the following ERP systems of Inforl: Infor ERP Baan IV, Infor ERP Baan5.x, and Infor  ERP Enterprise (LN).
