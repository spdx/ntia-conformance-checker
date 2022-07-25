SPDXVersion: SPDX-2.2
DataLicense: CC0-1.0
SPDXID: SPDXRef-DOCUMENT
DocumentName: build
DocumentNamespace: https://swinslow.net/plugfest2-sboms/charge-controller-firmware/spdx/build
Creator: Tool: Zephyr SPDX builder
Created: 2021-06-08T01:29:31Z

ExternalDocumentRef: DocumentRef-zephyr https://swinslow.net/plugfest2-sboms/charge-controller-firmware/spdx/zephyr SHA1: 26b050b60103ee9c4f3a8ad0c219fae24f6efed5

Relationship: SPDXRef-DOCUMENT DESCRIBES SPDXRef-zephyr-final

##### Package: ..__modules__hal__stm32__stm32cube

PackageName: ..__modules__hal__stm32__stm32cube
SPDXID: SPDXRef-..--modules--hal--stm32--stm32cube
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: Apache-2.0
PackageLicenseInfoFromFiles: Apache-2.0
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: fe795c253cb987821258be9757222a191b65aa4d

Relationship: SPDXRef-..--modules--hal--stm32--stm32cube HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-..--modules--hal--stm32--stm32cube HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-..--modules--hal--stm32--stm32cube HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-..--modules--hal--stm32--stm32cube HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./modules/stm32/stm32cube/lib..__modules__hal__stm32__stm32cube.a
SPDXID: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a
FileChecksum: SHA1: cd7096be3419dca7af61597a4c38ea0949d3485a
FileChecksum: SHA256: c62be251e0eaba5e69c72890959661a88065fc63943558717b096938e1b68923
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-rcc.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-spi.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-tim.c
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-utils.c

FileName: ./zephyr/dev_handles.c
SPDXID: SPDXRef-File-dev-handles.c
FileChecksum: SHA1: 3397de05298c3ddbcbdbba4433482653ce7c6594
FileChecksum: SHA256: fa40f00ceec07245fc874e0aa165b533ac9d81108cb53518683c968e0083e707
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/isr_tables.c
SPDXID: SPDXRef-File-isr-tables.c
FileChecksum: SHA1: c5aa2163474afb3cd13cb5c05a4d28b9f0f375d5
FileChecksum: SHA256: 766635260869a72830b4d47dd0609d40b69d78bb0a28daa0448942b41d2277e8
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/misc/generated/configs.c
SPDXID: SPDXRef-File-configs.c
FileChecksum: SHA1: d0dbe39c3477fd588f7f82265d44a0f5d58d1a60
FileChecksum: SHA256: 1889dad1d781c2886a015abf33014e2f949abddcfe19d182f6e91218b440a592
LicenseConcluded: Apache-2.0
LicenseInfoInFile: Apache-2.0
FileCopyrightText: NOASSERTION

##### Package: app

PackageName: app
SPDXID: SPDXRef-app
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 9101f2ddeb664226efee5e7ddb576b2148972ddb

Relationship: SPDXRef-app HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-app HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-app HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-app HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./app/libapp.a
SPDXID: SPDXRef-File-libapp.a
FileChecksum: SHA1: fc944071c034a018acf1cdefa32d0ad06323616a
FileChecksum: SHA256: 1a59a91de47038ee22f77195ad30cec6fd2cf32582fd9d1a84772c041ee84a0c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

##### Package: arch__arm__core__aarch32

PackageName: arch__arm__core__aarch32
SPDXID: SPDXRef-arch--arm--core--aarch32
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 72ade45611c7b0c284e7784c8885001d4de04701

Relationship: SPDXRef-arch--arm--core--aarch32 HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-arch--arm--core--aarch32 HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-arch--arm--core--aarch32 HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-arch--arm--core--aarch32 HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/arch/arch/arm/core/aarch32/libarch__arm__core__aarch32.a
SPDXID: SPDXRef-File-libarch--arm--core--aarch32.a
FileChecksum: SHA1: 94472e54d2d45ddda8cd48631f054d8df12b4ead
FileChecksum: SHA256: c3e9351ad18c1af633adb211625f4417ea812976e95fcfb95655f6ac44de020c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-swap.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-swap-helper.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-manage.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu-idle.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi-on-reset.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-prep-c.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-isr-wrapper.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---aeabi-atexit.c

##### Package: arch__arm__core__aarch32__cortex_m

PackageName: arch__arm__core__aarch32__cortex_m
SPDXID: SPDXRef-arch--arm--core--aarch32--cortex-m
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 09c0c73a16c177997138afa921e56201abc22c1c

Relationship: SPDXRef-arch--arm--core--aarch32--cortex-m HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--cortex-m HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--cortex-m HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--cortex-m HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/arch/arch/arm/core/aarch32/cortex_m/libarch__arm__core__aarch32__cortex_m.a
SPDXID: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a
FileChecksum: SHA1: 31fec1f4bdec78c287fa245ca358360fd8ad3d3d
FileChecksum: SHA256: 5b2bb7a1f9a843bf3489ae3836a260922f4b4e1a9526ec5a4a4e598f75049785
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-vector-table.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-reset.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fault-s.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fault.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc-exit.S
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-scb.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-init.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-abort.c

##### Package: arch__arm__core__aarch32__mpu

PackageName: arch__arm__core__aarch32__mpu
SPDXID: SPDXRef-arch--arm--core--aarch32--mpu
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 7b35fa87e505ee93076718acd632c0a8054afeac

Relationship: SPDXRef-arch--arm--core--aarch32--mpu HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--mpu HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--mpu HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-arch--arm--core--aarch32--mpu HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/arch/arch/arm/core/aarch32/mpu/libarch__arm__core__aarch32__mpu.a
SPDXID: SPDXRef-File-libarch--arm--core--aarch32--mpu.a
FileChecksum: SHA1: 68d83f18b86a35e4e8c69de931d28fc3baa9350a
FileChecksum: SHA256: 673b5e339704b24f3cdfc3558f0db8fcf4aed2166b1c4fe3f395b579016cc27a
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-core-mpu.c
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.c

##### Package: arch__common

PackageName: arch__common
SPDXID: SPDXRef-arch--common
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 8ea1e362fbc5652a53370bdaca061ccdc5b583d2

Relationship: SPDXRef-arch--common HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-arch--common HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-arch--common HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-arch--common HAS_PREREQUISITE SPDXRef-zephyr-generated-headers
Relationship: SPDXRef-arch--common HAS_PREREQUISITE SPDXRef-isr-tables

FileName: ./zephyr/arch/common/libarch__common.a
SPDXID: SPDXRef-File-libarch--common.a
FileChecksum: SHA1: 7a8cc8c3f103c0cdae0728428444fdb073aefdd1
FileChecksum: SHA256: b9917b9893163a38190c744ea434060a655f286c07d24062ed6311feccca42fe
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-common.c
Relationship: SPDXRef-File-libarch--common.a STATIC_LINK SPDXRef-File-libisr-tables.a

##### Package: asm

PackageName: asm
SPDXID: SPDXRef-asm
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: attach

PackageName: attach
SPDXID: SPDXRef-attach
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: bintools

PackageName: bintools
SPDXID: SPDXRef-bintools
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: boards

PackageName: boards
SPDXID: SPDXRef-boards
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: code_data_relocation_target

PackageName: code_data_relocation_target
SPDXID: SPDXRef-code-data-relocation-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: compiler

PackageName: compiler
SPDXID: SPDXRef-compiler
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: compiler-cpp

PackageName: compiler-cpp
SPDXID: SPDXRef-compiler-cpp
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: config-twister

PackageName: config-twister
SPDXID: SPDXRef-config-twister
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: debug

PackageName: debug
SPDXID: SPDXRef-debug
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: debugserver

PackageName: debugserver
SPDXID: SPDXRef-debugserver
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: driver_validation_h_target

PackageName: driver_validation_h_target
SPDXID: SPDXRef-driver-validation-h-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-driver-validation-h-target HAS_PREREQUISITE SPDXRef-parse-syscalls-target

##### Package: drivers__flash

PackageName: drivers__flash
SPDXID: SPDXRef-drivers--flash
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: ff2e500198e69b4521bb349183da976066f3eadb

Relationship: SPDXRef-drivers--flash HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-drivers--flash HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-drivers--flash HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-drivers--flash HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/drivers/flash/libdrivers__flash.a
SPDXID: SPDXRef-File-libdrivers--flash.a
FileChecksum: SHA1: 3e23765705bcc1be4cb808b2b6fbabbd69155166
FileChecksum: SHA256: 14e7915a5bf01c4539278d47e3d7a99c5ea4e23f42f56a3e6973cb91800eee1c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi-nor.c
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash-page-layout.c
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-jesd216.c

##### Package: drivers__gpio

PackageName: drivers__gpio
SPDXID: SPDXRef-drivers--gpio
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 8bc896eaf1e8a820b8db8889c060c1675daf1c97

Relationship: SPDXRef-drivers--gpio HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-drivers--gpio HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-drivers--gpio HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-drivers--gpio HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/drivers/gpio/libdrivers__gpio.a
SPDXID: SPDXRef-File-libdrivers--gpio.a
FileChecksum: SHA1: 0a198a6028bd3370a2eeb38c6c62c0aad5aaa87c
FileChecksum: SHA256: 2c427c419752d9bdc5d6daafab02b5501ca890f3cdf6128a00b346a6c7b73324
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio-stm32.c

##### Package: drivers__pwm

PackageName: drivers__pwm
SPDXID: SPDXRef-drivers--pwm
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: d48dfccbbaee3590c1f3cf364396993f6d2411a7

Relationship: SPDXRef-drivers--pwm HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-drivers--pwm HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-drivers--pwm HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-drivers--pwm HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/drivers/pwm/libdrivers__pwm.a
SPDXID: SPDXRef-File-libdrivers--pwm.a
FileChecksum: SHA1: 3730c730b3d6ccfafab1889f80dbfc54e99f2df0
FileChecksum: SHA256: 9dd6307b6b1d245088f2c5f2df88081ee6a755b51fe14a1e6a375b20dfca344f
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwm-stm32.c

##### Package: drivers__serial

PackageName: drivers__serial
SPDXID: SPDXRef-drivers--serial
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 99de2d87de99c594d36e101aa529f197bacc4996

Relationship: SPDXRef-drivers--serial HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-drivers--serial HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-drivers--serial HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-drivers--serial HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/drivers/serial/libdrivers__serial.a
SPDXID: SPDXRef-File-libdrivers--serial.a
FileChecksum: SHA1: 5d30b815f1d16c306a6e5782b7900714c02d732a
FileChecksum: SHA256: 2b50e852626f2d1ead6a58431c86dabc592db54e16cc12acddcd2eba4c14c1d6
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart-stm32.c

##### Package: drivers__spi

PackageName: drivers__spi
SPDXID: SPDXRef-drivers--spi
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 48ed44ecea6a428feff6d9a45ed4e59b8ca26385

Relationship: SPDXRef-drivers--spi HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-drivers--spi HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-drivers--spi HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-drivers--spi HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/drivers/spi/libdrivers__spi.a
SPDXID: SPDXRef-File-libdrivers--spi.a
FileChecksum: SHA1: a6f7431b06cc178b5d3c5c94bc835d204fd85c41
FileChecksum: SHA256: 889ce178cd1db7ddf3dd803b786f5b8b6304ebd5537474eabadfbf724f8e8e4b
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi-ll-stm32.c

##### Package: flash

PackageName: flash
SPDXID: SPDXRef-flash
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: guiconfig

PackageName: guiconfig
SPDXID: SPDXRef-guiconfig
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: hardenconfig

PackageName: hardenconfig
SPDXID: SPDXRef-hardenconfig
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: isr_tables

PackageName: isr_tables
SPDXID: SPDXRef-isr-tables
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: e691a866db703ebda0291fe7358fe202c7304096

Relationship: SPDXRef-isr-tables HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-isr-tables HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-isr-tables HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-isr-tables HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/arch/common/libisr_tables.a
SPDXID: SPDXRef-File-libisr-tables.a
FileChecksum: SHA1: 1b7aa893a4846be40982d73b72ee72d307e809b9
FileChecksum: SHA256: 09de3b3853582e6f47ed23cb11d84887c6d8fdcc87b4dcfcdd21e54279d6ecaf
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-isr-tables.c

##### Package: kernel

PackageName: kernel
SPDXID: SPDXRef-kernel
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 09b48617eefcb7cf65e3e5d05b644a004bf664a1

Relationship: SPDXRef-kernel HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-kernel HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-kernel HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-kernel HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/kernel/libkernel.a
SPDXID: SPDXRef-File-libkernel.a
FileChecksum: SHA1: 5fe57cca591dafab8f0804fb609e4ea372f2e0c5
FileChecksum: SHA256: 599483d9b797454bd5fb0458b4149fd1336fd98cc7ca5b55b9ddfd0b8bffadbe
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-banner.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-errno.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.c-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kheap.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-slab.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.c-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-version.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-idle.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mailbox.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-msg-q.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mutex.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pipes.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-queue.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sem.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-work-q.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-work.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-condvar.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-xip.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timer.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-poll.c
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool.c

##### Package: kobj_types_h_target

PackageName: kobj_types_h_target
SPDXID: SPDXRef-kobj-types-h-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-kobj-types-h-target HAS_PREREQUISITE SPDXRef-parse-syscalls-target

##### Package: lib__libc__newlib

PackageName: lib__libc__newlib
SPDXID: SPDXRef-lib--libc--newlib
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 8a618962a4a3105cce96b4c0106e811633496840

Relationship: SPDXRef-lib--libc--newlib HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-lib--libc--newlib HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-lib--libc--newlib HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-lib--libc--newlib HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/lib/libc/newlib/liblib__libc__newlib.a
SPDXID: SPDXRef-File-liblib--libc--newlib.a
FileChecksum: SHA1: 1d2339a8489407a59cb391de9474cf0d20e12d28
FileChecksum: SHA256: 448f075313e5d8ff1d3e11472b8664ddb474f628f074944ab3fa8bcde12d1e65
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-libc-hooks.c

##### Package: lib__posix

PackageName: lib__posix
SPDXID: SPDXRef-lib--posix
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 2d90e29adc78323d71246724c9dac2b2ae7ccf91

Relationship: SPDXRef-lib--posix HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-lib--posix HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-lib--posix HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-lib--posix HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/lib/posix/liblib__posix.a
SPDXID: SPDXRef-File-liblib--posix.a
FileChecksum: SHA1: 9a214448150c8d1dcc5f2d54ff1e622824aaafc1
FileChecksum: SHA256: 456c1c5a672d101e49debddecaf6dbfee0517f468eb78ebfce5a49c8300e0507
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pthread-common.c
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nanosleep.c

##### Package: linker

PackageName: linker
SPDXID: SPDXRef-linker
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: linker_zephyr_final_script_target

PackageName: linker_zephyr_final_script_target
SPDXID: SPDXRef-linker-zephyr-final-script-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-linker-zephyr-final-script-target HAS_PREREQUISITE SPDXRef-zephyr-generated-headers
Relationship: SPDXRef-linker-zephyr-final-script-target HAS_PREREQUISITE SPDXRef-zephyr-prebuilt

##### Package: linker_zephyr_prebuilt_script_target

PackageName: linker_zephyr_prebuilt_script_target
SPDXID: SPDXRef-linker-zephyr-prebuilt-script-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-linker-zephyr-prebuilt-script-target HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

##### Package: menuconfig

PackageName: menuconfig
SPDXID: SPDXRef-menuconfig
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: offsets

PackageName: offsets
SPDXID: SPDXRef-offsets
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 0b3d65779879825ab1d4cb961fee7b13303c98e6

Relationship: SPDXRef-offsets HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-offsets HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-offsets HAS_PREREQUISITE SPDXRef-kobj-types-h-target

FileName: ./zephyr/CMakeFiles/offsets.dir/arch/arm/core/offsets/offsets.c.obj
SPDXID: SPDXRef-File-
FileChecksum: SHA1: 198818231c4030a3cc2182a126b0d469669193d5
FileChecksum: SHA256: 8f3e436488d1e3404cdb7243b77d4ab97fbd80087d2e569171f58c10e4686f7e
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-offsets.c

##### Package: offsets_h

PackageName: offsets_h
SPDXID: SPDXRef-offsets-h
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-offsets-h HAS_PREREQUISITE SPDXRef-offsets

##### Package: parse_syscalls_target

PackageName: parse_syscalls_target
SPDXID: SPDXRef-parse-syscalls-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: pristine

PackageName: pristine
SPDXID: SPDXRef-pristine
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: ram_report

PackageName: ram_report
SPDXID: SPDXRef-ram-report
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-ram-report HAS_PREREQUISITE SPDXRef-zephyr-final

##### Package: rom_report

PackageName: rom_report
SPDXID: SPDXRef-rom-report
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-rom-report HAS_PREREQUISITE SPDXRef-zephyr-final

##### Package: run

PackageName: run
SPDXID: SPDXRef-run
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: runners_yaml_props_target

PackageName: runners_yaml_props_target
SPDXID: SPDXRef-runners-yaml-props-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: shields

PackageName: shields
SPDXID: SPDXRef-shields
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: soc__arm__common__cortex_m

PackageName: soc__arm__common__cortex_m
SPDXID: SPDXRef-soc--arm--common--cortex-m
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: a16a070e446756c4bda7fa98e5a872dd1694d7af

Relationship: SPDXRef-soc--arm--common--cortex-m HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-soc--arm--common--cortex-m HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-soc--arm--common--cortex-m HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-soc--arm--common--cortex-m HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/soc/arm/common/cortex_m/libsoc__arm__common__cortex_m.a
SPDXID: SPDXRef-File-libsoc--arm--common--cortex-m.a
FileChecksum: SHA1: 1374dc43692c9731f9d9913640dd6e411f8e44af
FileChecksum: SHA256: 489f5d2f2482e84ce88a8348fbbb11f8558fdae4ff5469f7771ce460bae15ffb
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-regions.c

##### Package: subsys__canbus__isotp

PackageName: subsys__canbus__isotp
SPDXID: SPDXRef-subsys--canbus--isotp
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 42d6b2438397f045ea3f5c26782f0a7b54949ef4

Relationship: SPDXRef-subsys--canbus--isotp HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-subsys--canbus--isotp HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-subsys--canbus--isotp HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-subsys--canbus--isotp HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/subsys/canbus/isotp/libsubsys__canbus__isotp.a
SPDXID: SPDXRef-File-libsubsys--canbus--isotp.a
FileChecksum: SHA1: 070c21b99bc7eb98244420523c8374221daf005e
FileChecksum: SHA256: 4e480adc8bc3bcfdf0599676bc161002f2afe4dc8b580d086159061afa6827ae
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-isotp.c

##### Package: subsys__net

PackageName: subsys__net
SPDXID: SPDXRef-subsys--net
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 176371db4c4983b4c711fe8035caa92d04c92d12

Relationship: SPDXRef-subsys--net HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-subsys--net HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-subsys--net HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-subsys--net HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/subsys/net/libsubsys__net.a
SPDXID: SPDXRef-File-libsubsys--net.a
FileChecksum: SHA1: 5dd683980396712ef66104905f94d338356f42d9
FileChecksum: SHA256: 26acf1b133a5c8e70ec3b98c11de370d8c705d35272bfb0f3994181a1704c647
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-buf.c

##### Package: syscall_list_h_target

PackageName: syscall_list_h_target
SPDXID: SPDXRef-syscall-list-h-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-syscall-list-h-target HAS_PREREQUISITE SPDXRef-parse-syscalls-target

##### Package: usage

PackageName: usage
SPDXID: SPDXRef-usage
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

##### Package: zephyr

PackageName: zephyr
SPDXID: SPDXRef-zephyr
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 9855b52bb8e1ecb9c65e8312e27fb0fe67aa9d7e

Relationship: SPDXRef-zephyr HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-zephyr HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-zephyr HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-zephyr HAS_PREREQUISITE SPDXRef-zephyr-generated-headers

FileName: ./zephyr/libzephyr.a
SPDXID: SPDXRef-File-libzephyr.a
FileChecksum: SHA1: d02d3a8f0a78983c898f4279386978166338f065
FileChecksum: SHA256: c975ec8d1179157f849eeebc323f8302235cd90a9fe1c85b823b5dcc29f37a48
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-packaged.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc32c-sw.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc32-sw.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc16-sw.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc8-sw.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc7-sw.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dec.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fdtable.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-hex.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-notify.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-onoff.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sem.c-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-entry.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeutil.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-heap.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-heap-validate.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-bitarray.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-complete.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-reboot.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-configs.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32cube-hal.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc-config.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-minimal.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tty.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-getchar.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-init-array.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-ctors.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-dtors.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-virtual.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-vtable.cpp
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpp-new.cpp
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvs.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-utils.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-task-wdt.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-none.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart-console.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-intc-exti-stm32.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-stm32-ll-common.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-stm32g4.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wdt-iwdg-stm32.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-common.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-stm32fd.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-mcan.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-hwinfo-weak-impl.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-hwinfo-stm32.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash-stm32.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash-stm32g4x.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock-init.c
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cortex-m-systick.c

##### Package: zephyr_final

PackageName: zephyr_final
SPDXID: SPDXRef-zephyr-final
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: 5e427cd71caa8fabc4098ff0f8742e1ebcc3a864

Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-app
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-zephyr
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-linker-zephyr-final-script-target
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-zephyr-prebuilt
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-isr-tables
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-arch--common
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32--cortex-m
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32--mpu
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-lib--libc--newlib
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-lib--posix
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-soc--arm--common--cortex-m
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-subsys--net
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-subsys--canbus--isotp
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-drivers--gpio
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-drivers--pwm
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-drivers--spi
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-drivers--flash
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-drivers--serial
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-..--modules--hal--stm32--stm32cube
Relationship: SPDXRef-zephyr-final HAS_PREREQUISITE SPDXRef-kernel

FileName: ./zephyr/zephyr.elf
SPDXID: SPDXRef-File-zephyr.elf
FileChecksum: SHA1: 559f49694ff5d8f2ec57ec35c7307f0a22f97f44
FileChecksum: SHA256: 785955e748f1e35e96a0b5767d20a3ab4a13fa05a31ebb830482ac0b05f5d040
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-empty-file.c
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-isr-tables.c
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-dev-handles.c
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libapp.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libzephyr.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-zephyr-prebuilt.elf
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libisr-tables.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libarch--common.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32--mpu.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-liblib--libc--newlib.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-liblib--posix.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libsoc--arm--common--cortex-m.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libsubsys--net.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libsubsys--canbus--isotp.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libdrivers--gpio.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libdrivers--pwm.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libdrivers--spi.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libdrivers--flash.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libdrivers--serial.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a
Relationship: SPDXRef-File-zephyr.elf STATIC_LINK SPDXRef-File-libkernel.a

##### Package: zephyr_generated_headers

PackageName: zephyr_generated_headers
SPDXID: SPDXRef-zephyr-generated-headers
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

Relationship: SPDXRef-zephyr-generated-headers HAS_PREREQUISITE SPDXRef-offsets-h

##### Package: zephyr_prebuilt

PackageName: zephyr_prebuilt
SPDXID: SPDXRef-zephyr-prebuilt
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: true
PackageVerificationCode: c4a6a37201ab2ab8eeeb665de51fbad1f0fbd009

Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-app
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-syscall-list-h-target
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-zephyr
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-driver-validation-h-target
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-kobj-types-h-target
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-offsets
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-linker-zephyr-prebuilt-script-target
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-isr-tables
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-arch--common
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32--cortex-m
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-arch--arm--core--aarch32--mpu
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-lib--libc--newlib
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-lib--posix
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-soc--arm--common--cortex-m
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-subsys--net
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-subsys--canbus--isotp
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-drivers--gpio
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-drivers--pwm
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-drivers--spi
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-drivers--flash
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-drivers--serial
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-..--modules--hal--stm32--stm32cube
Relationship: SPDXRef-zephyr-prebuilt HAS_PREREQUISITE SPDXRef-kernel

FileName: ./zephyr/zephyr_prebuilt.elf
SPDXID: SPDXRef-File-zephyr-prebuilt.elf
FileChecksum: SHA1: da17b5b25cc7c9b452a956bb3a3dec2ac51d7bf5
FileChecksum: SHA256: 3f9d5636a15554c9354fdb59cb446d79c69c883f794a66e89fe3df7b68714db2
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

Relationship: SPDXRef-File-zephyr-prebuilt.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-empty-file.c
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libapp.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libzephyr.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libisr-tables.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libarch--common.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libarch--arm--core--aarch32--mpu.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-liblib--libc--newlib.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-liblib--posix.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libsoc--arm--common--cortex-m.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libsubsys--net.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libsubsys--canbus--isotp.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libdrivers--gpio.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libdrivers--pwm.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libdrivers--spi.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libdrivers--flash.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libdrivers--serial.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a
Relationship: SPDXRef-File-zephyr-prebuilt.elf STATIC_LINK SPDXRef-File-libkernel.a

##### Package: zephyr_property_target

PackageName: zephyr_property_target
SPDXID: SPDXRef-zephyr-property-target
PackageDownloadLocation: NOASSERTION
PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageCopyrightText: NOASSERTION
FilesAnalyzed: false
PackageComment: Utility target; no files

