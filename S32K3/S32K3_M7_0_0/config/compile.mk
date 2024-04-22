################################################################################
# compile.mk
# 
# HISTORY
# 17/06/2021  |                                             | Daich
################################################################################


ifndef COMPILER
	COMPILER=ARM_GCC
endif

ifeq "$(COMPILER)" "IAR"
TC_CC:= iccarm.exe
TC_CPP:= iccarm.exe
TC_ASM:= iasmarm.exe
TC_LINK:= ilinkarm.exe
TC_AR:= iarchive.exe
endif


ifeq "$(COMPILER)" "ARMCC"
TC_CC:= armcc.exe
TC_CPP:= armcc.exe
TC_ASM:= armasm.exe
TC_LINK:= armlink.exe
TC_AR:= armar.exe
endif


ifeq "$(COMPILER)" "ARM_GCC"
TC_CC:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-gcc.exe
TC_CPP:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-g++.exe
TC_ASM:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-as.exe
TC_LINK:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-ld.exe
TC_AR:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-ar.exe
TC_SIZE:= D:/soft_install/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-size.exe

$(info ------------------------------------------------------ ${TC_SIZE} )


endif


