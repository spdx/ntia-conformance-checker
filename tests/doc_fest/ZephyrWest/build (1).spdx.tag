SPDXVersion: SPDX-2.2
DataLicense: CC0-1.0
SPDXID: SPDXRef-DOCUMENT
DocumentName: build
DocumentNamespace: https://swinslow.net/plugfest2-sboms/charge-controller-firmware/spdx-with-headers/build
Creator: Tool: Zephyr SPDX builder
Created: 2021-06-08T01:32:35Z

ExternalDocumentRef: DocumentRef-sdk https://swinslow.net/plugfest2-sboms/charge-controller-firmware/spdx-with-headers/sdk SHA1: 1a25205432b8df5aa4dadf93243e246b98dada62
ExternalDocumentRef: DocumentRef-zephyr https://swinslow.net/plugfest2-sboms/charge-controller-firmware/spdx-with-headers/zephyr SHA1: 46d4964f37547c587ef3b5d2c3a604a3da943eb0

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
PackageVerificationCode: 4bbd1b9c79398be50c0040f7baec54ab283bfff6

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
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-bus.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-pwr.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-rcc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-spi.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-system.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-tim.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-utils.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-lib..--modules--hal--stm32--stm32cube.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

FileName: ./zephyr/dev_handles.c
SPDXID: SPDXRef-File-dev-handles.c
FileChecksum: SHA1: 3397de05298c3ddbcbdbba4433482653ce7c6594
FileChecksum: SHA256: fa40f00ceec07245fc874e0aa165b533ac9d81108cb53518683c968e0083e707
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/autoconf.h
SPDXID: SPDXRef-File-autoconf.h
FileChecksum: SHA1: c6c3c0b5f0b258f5993da7c8cba158d41f686b91
FileChecksum: SHA256: 36fb94d89e55b29c9788635f3872ba725b2a1f7bbd2fe239caa457d3cefb9f70
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/device_extern.h
SPDXID: SPDXRef-File-device-extern.h
FileChecksum: SHA1: f311b83ab077774067ab7cb99b6f9bdae33483fb
FileChecksum: SHA256: e3591eb45ecaa2957127b70b88cf93603cbfb0e59308829e08f6f9ac7afcf106
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/devicetree_fixups.h
SPDXID: SPDXRef-File-devicetree-fixups.h
FileChecksum: SHA1: 39994be50dcfa32c367a29a57a642cebf88c519b
FileChecksum: SHA256: 83a17e01e8fbe531930f236711581f6cc72d751cca908156e21bc967a4555c8e
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/devicetree_unfixed.h
SPDXID: SPDXRef-File-devicetree-unfixed.h
FileChecksum: SHA1: 71a8b5ea522b2c85cec45b311d14d40a3fc2b311
FileChecksum: SHA256: f12c4a3551be93d838a87a2df4534945022e8fdc20f902a181f3333869c87a2c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/kobj-types-enum.h
SPDXID: SPDXRef-File-kobj-types-enum.h
FileChecksum: SHA1: 2597b6f4497ef79493fc992505dbac3374d656bc
FileChecksum: SHA256: 83c5b6e6b0ddab267dbaa77104d27a6cb4f2a0cd5c6bb560fe762ca07a6d7521
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/offsets.h
SPDXID: SPDXRef-File-offsets.h
FileChecksum: SHA1: 88748f677d33c57ce9b921822355d4b4f99a0a60
FileChecksum: SHA256: daedf3fb5fb02b02a9cf9e0cf6b7dbc31cd6739d7b1890e5630044d865fee692
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscall_list.h
SPDXID: SPDXRef-File-syscall-list.h
FileChecksum: SHA1: 5c557da524ce26a7b8351667aa9491e863d1a66a
FileChecksum: SHA256: 027b584568f22cfe2efe7327c6ac78b57189baf3f813f421b376b49191a97943
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/can.h
SPDXID: SPDXRef-File-can.h
FileChecksum: SHA1: 524ec6860799110598022f22bbfbd1e67d81b27c
FileChecksum: SHA256: 45cb7e53f564788714bc83b53046b97400633739abe9cc3ca52126203c66ad9c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/device.h
SPDXID: SPDXRef-File-device.h
FileChecksum: SHA1: 00b6aa6426e402ede8a12e581f3721a1da69312d
FileChecksum: SHA256: 5fb8614f60097807c597c6af0ef70922edae3ef90b058304c67f717073a9591f
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/entropy.h
SPDXID: SPDXRef-File-entropy.h
FileChecksum: SHA1: 938d5d73d585644af849ce1a33c163a388156db4
FileChecksum: SHA256: 65f1486ce2a49bcfdfef1c09866de4a2b42dbe7240a06de4099929013b81d3cc
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/errno_private.h
SPDXID: SPDXRef-File-errno-private.h
FileChecksum: SHA1: 6124680479942d954e1b3d9e7ec6a802abacb53a
FileChecksum: SHA256: 240cf54a3c8d4b63cd31731c2e8aa1129a4f27e9d05f8c4703cac7680d053fca
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/flash.h
SPDXID: SPDXRef-File-flash.h
FileChecksum: SHA1: a534c314dc0040ec764ff08c8085d33f5a9fe031
FileChecksum: SHA256: 3437eb30f64727189be7ae35ac64a28f85efad9e9a051ccaf10644125c19784d
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/gpio.h
SPDXID: SPDXRef-File-gpio.h
FileChecksum: SHA1: fb20ddcf2066f277eb93f7b32414c23f2f178789
FileChecksum: SHA256: 5e69d6a7af64863bb2c014d4fc5cbab41560ab316166ae63780f06fa8ce636a8
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/hwinfo.h
SPDXID: SPDXRef-File-hwinfo.h
FileChecksum: SHA1: 6772d7858dabc38de75bb79cf441cc0ba9d17e34
FileChecksum: SHA256: 595c93c775641b711eded7dae47f3a5e1dc8c2c40a5f247004e57199fc3c0147
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/kernel.h
SPDXID: SPDXRef-File-kernel.h
FileChecksum: SHA1: 9cb7e3cec56cb4ab4516d850cc6a915c9390592f
FileChecksum: SHA256: 764be3ae45cd4558bb7db1b265b6d57cd2ba24b0e5650dce115f49b36d1e8482
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/kobject.h
SPDXID: SPDXRef-File-kobject.h
FileChecksum: SHA1: ca8faf86434adc9119714ef1612aa950db681eef
FileChecksum: SHA256: b648a44a84de8998507ddc562ccce1c7bb8711f192bdf9152bc07c0563603223
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/libc-hooks.h
SPDXID: SPDXRef-File-libc-hooks.h
FileChecksum: SHA1: c8e65698a402e2ad7629c8dc12e2f79560f88f4f
FileChecksum: SHA256: 5b5b8934b41ee1065cfc141f2db2c0bd680844de5200807e22ad12dee28e44df
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/log_core.h
SPDXID: SPDXRef-File-log-core.h
FileChecksum: SHA1: 03b7f7ef6930696112265f507391af11acc8b8a3
FileChecksum: SHA256: 987104ff2776b38c30da123cc4d8c18918bf0928aef04b5e73a7a4527297932c
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/log_ctrl.h
SPDXID: SPDXRef-File-log-ctrl.h
FileChecksum: SHA1: 32949656f0fbf42f41bce44fb10e244e3a5aef66
FileChecksum: SHA256: 08a7cb37f9279ca28ea637d88bcbdad52b8cb1ba26d48276688ef13dfa0b27c8
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/log_msg2.h
SPDXID: SPDXRef-File-log-msg2.h
FileChecksum: SHA1: a87ce7f2f91ce21be3492e04600a44868f5c05f9
FileChecksum: SHA256: 2f1ac6b0ae3237e0329ff2c3943cd6e063b506570652b0ab15f07b9777b71801
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/mem_manage.h
SPDXID: SPDXRef-File-mem-manage.h
FileChecksum: SHA1: e80aeb707eeb0f60658f3f5ea7f99bd3f9bbddc4
FileChecksum: SHA256: a8ae1417b93425c78a4de79d8f848f675d69d4eb22380d9656809ca7ed6ad0f7
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/pwm.h
SPDXID: SPDXRef-File-pwm.h
FileChecksum: SHA1: 05d43086bf7cc7b0029ef491d67ba6d873512d8c
FileChecksum: SHA256: 748c75a2cb451daeaf80b97fee5900d7f83600cdf07537782411ce35ff0efcac
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/rand32.h
SPDXID: SPDXRef-File-rand32.h
FileChecksum: SHA1: 1a9684cdf0268f3abe0862cbeb86d527989257c6
FileChecksum: SHA256: 7ccb3f55760fe3900b0883bee7c8aa7cc391ea8becf1b72b95440713e66d120d
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/spi.h
SPDXID: SPDXRef-File-spi.h
FileChecksum: SHA1: b2b1867c380972e3a832dc5a8b5b0375f7f49daf
FileChecksum: SHA256: b778a24135a7dec0e089b8fddcc9a3155aa64a14e68d1f988a94eaba9958f3ad
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/time.h
SPDXID: SPDXRef-File-time.h
FileChecksum: SHA1: 3de833d84a414a3bbf436f2b5325c00911b27e65
FileChecksum: SHA256: 01f0d6fff6ffbc1b07a2c2ef2259305565a9b0507a88582104503dd2b1320a01
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/uart.h
SPDXID: SPDXRef-File-uart.h
FileChecksum: SHA1: 75d6092a3840d3238d0ffc1fd056da473289a56d
FileChecksum: SHA256: 0b1cc8a6f9253bbc180e5236b9db47e8998ca8a2710b275c29d353a5dbfbf4ae
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/syscalls/watchdog.h
SPDXID: SPDXRef-File-watchdog.h
FileChecksum: SHA1: 009d8c5a603c96262474948415fa6fd319aad802
FileChecksum: SHA256: ce64bf1458e99e91bc6c8d9948acc7bbb33758ecab4597343b28d814d2570528
LicenseConcluded: NOASSERTION
LicenseInfoInFile: NONE
FileCopyrightText: NOASSERTION

FileName: ./zephyr/include/generated/version.h
SPDXID: SPDXRef-File-version.h
FileChecksum: SHA1: b1e889c7ab7fcdd459336a1635db4de136510bad
FileChecksum: SHA256: 275495ffbda9659d235b0ecfa28b598eb47f85f7873a0f809dde8b686b2bee4f
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

Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-adc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-bus.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-dac.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-dma.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-system.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-bus.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-dac.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-dma.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-dmamux.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-system.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM SPDXRef-File-pwm.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwm.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-3
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwm.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras-impl.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--timespec.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-3
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-timespec.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libapp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-offsets.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-linker-defs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pm.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-state.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-reboot.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout-q.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wait-q.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-interface.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ksched.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-offsets.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc-handle.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-linker-defs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout-q.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wait-q.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-interface.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ksched.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kswap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-core-mpu-dev.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-offsets.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-linker-defs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras-impl.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libarch--arm--core--aarch32--mpu.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libarch--common.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h
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
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-flash.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash-priv.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-jesd216.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi-nor.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-3
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-byteorder.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libdrivers--flash.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-bus.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-exti.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-gpio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-hsem.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-pwr.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-system.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-bus.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-gpio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-pwr.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-system.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio-stm32.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio-utils.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32g4x.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-control.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock-control.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exti-stm32.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-3
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl-common.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-runtime.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hsem.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libdrivers--gpio.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-rcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-tim.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-rcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-tim.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM SPDXRef-File-pwm.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32g4x.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-control.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock-control.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwm.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl-common.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwm.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras-impl.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libdrivers--pwm.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-lpuart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-usart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-lpuart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM SPDXRef-File-uart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32g4x.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart-stm32.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-control.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock-control.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl-common.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libdrivers--serial.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-spi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-spi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32g4x.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi-context.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi-ll-stm32.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-control.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock-control.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-3
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl-common.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libdrivers--spi.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libisr-tables.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-offsets-short-arch.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-offsets-short-arch.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-offsets.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-entropy.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-log-ctrl.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-rand32.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM SPDXRef-File-version.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-coredump.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcov.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-entropy.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-timer.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-linker-defs.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-backend.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-ctrl.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pm.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-state.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rand32.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-check.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-math-extras-impl.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall-handler.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout-q.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timing.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wait-q.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-interface.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-internal.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ksched.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kswap.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-offsets-short.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libkernel.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-offsets.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-errno-private.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-libc-hooks.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-app-memdomain.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-linker-defs.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-errno-private.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-libc-hooks.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mutex.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sem.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall-handler.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--time.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--timespec.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--timeval.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stat.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-3
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h-3
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-timespec.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-liblib--libc--newlib.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-func.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM SPDXRef-File-time.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-posix-types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-signal.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout-q.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wait-q.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-interface.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-internal.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ksched.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--timespec.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-timespec.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-liblib--posix.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-offsets-aarch32.c
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stack.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-arch-data.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File- GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gen-offset.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-offsets.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File- GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-mem-cfg.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libsoc--arm--common--cortex-m.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-can.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-isotp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-buf.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeout-q.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-isotp-internal.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libsubsys--canbus--isotp.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-buf.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-byteorder.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-3
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libsubsys--net.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-bus.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-exti.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-gpio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-hsem.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-iwdg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-pwr.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-rcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-system.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-ll-utils.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-bus.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-gpio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-iwdg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-pwr.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-rcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-system.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-utils.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-autoconf.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-can.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-flash.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-hwinfo.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-uart.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM SPDXRef-File-watchdog.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-mcan.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-mcan-int.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can-stm32fd.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-stm32-ll-common.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash-stm32.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio-stm32.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux-stm32g4x.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-wdt-iwdg-stm32.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-console.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tty.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-can.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clock-control.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock-control.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-console.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart-console.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-flash.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-hwinfo.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exti-stm32.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pinmux.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-timer.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-uart.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-watchdog.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-clock.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h-3
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl-common.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-pinctrl.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fs-interface.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-core2.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-instance.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-log-msg2.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-runtime.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-bitarray.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-byteorder.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-cxx.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cbprintf-internal.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-check.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-crc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fdtable.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpsc-packet.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-notify.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-onoff.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-reboot.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sem.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-speculation.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-timeutil.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall-handler.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-task-wdt.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-heap.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hsem.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvs-priv.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ctype.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-fcntl.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ssp.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-fcntl.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--pthreadtypes.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--timespec.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-fcntl.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stat.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdio.h-3
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-string.h-3
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-timespec.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-types.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-time.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-libzephyr.a GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h

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
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-compiler.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-gcc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis-version.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-core-cm4.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mpu-armv7.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32-hal-legacy.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-adc-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-comp.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-conf.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cordic.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cortex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-crc-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-cryp.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dac-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-def.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-dma-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-exti.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fdcan.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-flash-ramfunc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-fmac.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-gpio-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-hrtim.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2c-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-i2s.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-irda-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-iwdg.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-lptim.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nand.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-nor.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-opamp-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pcd-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-pwr-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-qspi.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rcc-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rng.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-rtc-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sai-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smartcard-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-smbus.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-spi-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-sram.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-tim-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-uart-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-usart-ex.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-hal-wwdg.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-adc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-exti.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx-ll-usb.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g431xx.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stm32g4xx.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-system-stm32g4xx.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-device-extern.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-devicetree-fixups.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-devicetree-unfixed.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-kobj-types-enum.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-syscall-list.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-device.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-kernel.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-kobject.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-domain.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-inlines.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-asm-inline-gcc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cmsis.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-memory-map.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nvic.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-error.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-exc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-misc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arm-mpu-v7m.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-nmi.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-addr-types.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ffs.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-bitops.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-cpu.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-structs.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-devicetree.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-clocks.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dma.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fixed-partitions.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gpio.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-io-channels.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-ordinals.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-pwms.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spi.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-zephyr.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-fatal.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-init.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-irq-offload.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-thread-stack.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-includes.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-structs.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kernel-version.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-section-tags.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sections.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mempool-heap.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sched-priq.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-spinlock.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sw-isr-table.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File---assert.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-arch-interface.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-atomic-builtin.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-device-mmio.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-dlist.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-kobject.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-list-gen.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-mem-manage.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-printk.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-rb.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sflist.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-slist.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-heap.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-io.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-time-units.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-internal.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-loops.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-util-macro.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-sys-clock.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-syscall.h-3
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-toolchain.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-common.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-gcc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-tracing-macros.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-types.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-stdint.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-st-stm32-dt.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-zephyr:SPDXRef-File-soc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--ansi.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--newlib-version.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-inttypes.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--default-types.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-ieeefp.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-newlib.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--intsup.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--stdint.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File--types.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-cdefs.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-config.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-errno.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-features.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-lock.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-reent.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-limits.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-syslimits.h-2
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdarg.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdbool.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stddef.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint-gcc.h
Relationship: SPDXRef-File-zephyr.elf GENERATED_FROM DocumentRef-sdk:SPDXRef-File-stdint.h
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

