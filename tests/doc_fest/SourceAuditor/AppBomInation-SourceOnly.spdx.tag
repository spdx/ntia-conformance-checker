SPDXVersion: SPDX-2.2
DataLicense: CC0-1.0
DocumentNamespace: http://www.sourceauditor.com/spdxdocs/appbomination-src/e3b71037-57de-44c9-8b7f-4e8a62f45311
DocumentName: SpdxDoc for App-BOM-ination
SPDXID: SPDXRef-DOCUMENT

## Creation Information
Creator: Person: Gary O'Neall
Creator: Tool: Source Auditor Open Source Console
Created: 2021-09-02T13:46:32Z
CreatorComment: <text>Created for SPDX DocFest Sept 2021</text>
LicenseListVersion: 3.14
## Relationships
Relationship: SPDXRef-DOCUMENT DESCRIBES SPDXRef-1

## Package Information
PackageName: App-BOM-ination
SPDXID: SPDXRef-1
PackageVersion: 1.0
PackageFileName: App-BOM-ination-1.0.zip
PackageSupplier: Organization: ACT Project
PackageOriginator: Person: Yevester
PackageDownloadLocation: https://github.com/act-project/App-BOM-ination/archive/refs/tags/1.0.zip
PackageVerificationCode: be2fb65c6b22b81f1b273442d70479a41a3093e7
PackageChecksum: SHA1: 498cebd51a4483d6e68c2fc62d27008252fa4f7b
PackageHomePage: https://github.com/act-project/App-BOM-ination
PackageSourceInfo: <text></text>
PackageLicenseConcluded: (LicenseRef-1 AND Apache-2.0)
## License information from files
PackageLicenseInfoFromFiles: LicenseRef-1
PackageLicenseInfoFromFiles: Apache-2.0
PackageLicenseInfoFromFiles: (LGPL-2.0-or-later OR WTFPL)
PackageLicenseDeclared: Apache-2.0
PackageLicenseComments: <text>Faust proprietary notice was found in one or more source files.  LGPL-2.0-or-later OR WTFPL was in a build configuration file and does not apply to the concluded license.</text>
PackageCopyrightText: <text>Copyright (c) 2016 Faust, Inc.</text>
PackageSummary: <text>A uniquely useless project with a cataclysmic software supply chain, to serve a test case for BOM solutions.</text>
PackageDescription: <text>A uniquely useless project with a cataclysmic software supply chain, to serve a test case for BOM solutions.</text>

## File Information
FileName: ./LICENSE
SPDXID: SPDXRef-7
FileType: OTHER
FileChecksum: SHA1: 92170cdc034b2ff819323ff670d3b7266c8bffcd
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-7 CONTAINED_BY SPDXRef-1

FileName: ./README.md
SPDXID: SPDXRef-10
FileType: OTHER
FileChecksum: SHA1: 15399fcbbe6f3ff84c82039d446d820ecbbc3ac6
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-10 CONTAINED_BY SPDXRef-1

FileName: ./build.gradle
SPDXID: SPDXRef-2
FileType: OTHER
FileChecksum: SHA1: 9c55f0e3bd70363a02377f729d139a5d91325d40
LicenseConcluded: (LGPL-2.0-or-later OR WTFPL)
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-2 METAFILE_OF SPDXRef-1

FileName: ./gradle/wrapper/gradle-wrapper.properties
SPDXID: SPDXRef-3
FileType: OTHER
FileChecksum: SHA1: 67174de726d5caae455cd22e9c4450e9c490ac6b
LicenseConcluded: (LicenseRef-1 AND Apache-2.0)
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>

FileName: ./gradlew
SPDXID: SPDXRef-4
FileType: OTHER
FileChecksum: SHA1: b86a8c3bab5a3ed0441b3fe3b1f6b31ec1ead901
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-4 CONTAINED_BY SPDXRef-5

FileName: ./gradlew.bat
SPDXID: SPDXRef-6
FileComment: <text>BOMNOTE:File|</text>
FileType: SOURCE
FileChecksum: SHA1: d841ffc9855dcc642901e8abf28dee20b0485864
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-6 CONTAINED_BY SPDXRef-5

FileName: ./logo.png
SPDXID: SPDXRef-9
FileType: BINARY
FileChecksum: SHA1: 340e8b696bc50d76cf50df943dbaf46591da9ef4
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-9 CONTAINED_BY SPDXRef-1

FileName: ./settings.gradle
SPDXID: SPDXRef-11
FileType: OTHER
FileChecksum: SHA1: 1458a5c5fb1189d2cc8212052975f39ae710d622
LicenseConcluded: Apache-2.0
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-11 CONTAINED_BY SPDXRef-1

FileName: ./src/main/java/com/github/appbomination/InsufficientKarmaException.java
SPDXID: SPDXRef-12
FileComment: <text>BOMNOTE:File|Matched Notice='Faust Proprietary Notice'|</text>
FileType: SOURCE
FileChecksum: SHA1: fd668bc0096794e4d8125a29f9a746c0ab1edc57
LicenseConcluded: LicenseRef-1
LicenseInfoInFile: NOASSERTION
FileCopyrightText: <text>Copyright Faust Inc. All, and I mean ALL, rights are reserved</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-12 CONTAINED_BY SPDXRef-13

FileName: ./src/main/java/com/github/appbomination/Main.java
SPDXID: SPDXRef-14
FileType: SOURCE
FileChecksum: SHA1: 2b7b936a3f185a53528724e4f4141030906963c2
LicenseConcluded: Apache-2.0
LicenseInfoInFile: Apache-2.0
LicenseComments: Seen licenses generated by Source Auditor Scanner.  Results should be manually verified.
FileCopyrightText: <text>NOASSERTION</text>
FileNotice: <text>NOASSERTION</text>
## Relationships
Relationship: SPDXRef-14 CONTAINED_BY SPDXRef-1

## Package Information
PackageName: Gradle
SPDXID: SPDXRef-5
PackageComment: <text>Package info generated from Source Auditor package database</text>
PackageDownloadLocation: NOASSERTION
PackageHomePage: https://gradle.org/
PackageLicenseConcluded: Apache-2.0
PackageLicenseDeclared: Apache-2.0
PackageCopyrightText: <text>NOASSERTION</text>
FilesAnalyzed: false

## Package Information
PackageName: Faust Proprietary File
SPDXID: SPDXRef-13
PackageComment: <text>Package info generated from Source Auditor package database</text>
PackageDownloadLocation: NOASSERTION
PackageHomePage: https://github.com/act-project/App-BOM-ination/blob/master/src/main/java/com/github/appbomination/InsufficientKarmaException.java
PackageLicenseConcluded: LicenseRef-1
PackageLicenseDeclared: LicenseRef-1
PackageCopyrightText: <text>NOASSERTION</text>
PackageSummary: <text>Files containing a Faust Proprietary Notice</text>
PackageDescription: <text>Files containing a Faust Proprietary Notice</text>
FilesAnalyzed: false


## License Information
LicenseID: LicenseRef-1
ExtractedText: <text>This file is licensed under the following license.
 
FAUST, INC. PROPRIETARY LICENSE:

FAUST, INC. grants you a non-exclusive right to use, modify, and distribute
the file provided that (a) you distribute all copies and/or modifications of
this file, whether in source or binary form, under the same license, and (b)
you hereby irrevocably transfer and assign the ownership of your soul to Faust, 
Inc. In the event the fair market value of your soul is less than $100 US, you
agree to compensate Faust, Inc. for the difference. 

Copyright (C) 2016 Faust Inc. All, and I mean ALL, rights are reserved.</text>
LicenseName: Faust Proprietary Notice

