################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init
-include compile.mk
RM := rm -rf

# All of the sources participating in the build are defined here


ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
-include Project_Settings/Startup_Code/subdir.mk
-include ./board/subdir.mk
-include ./generate/src/subdir.mk
-include ./RTD/src/subdir.mk
-include ./src/subdir.mk


SECONDARY_SIZE += \
S32K3_M7_0_0.siz \


# All Target
all: S32K3_M7_0_0.elf secondary-outputs

dependents:
	-cd ./build && $(MAKE) clean all

# Tool invocations
S32K3_M7_0_0.elf: $(OBJS) ../Project_Settings/Linker_Files/linker_flash_c0_s32k358.ld $(USER_OBJS) 
	@echo 'Building target: $@'
	@echo 'Invoking: Standard S32DS C Linker'
	${TC_CC} -o "S32K3_M7_0_0.elf" "@S32K3_M7_0_0.args"  $(USER_OBJS)
	@echo 'Finished building target: $@'
	@echo ' '

S32K3_M7_0_0.siz: S32K3_M7_0_0.elf
	@echo 'Invoking: Standard S32DS Print Size'
	${TC_SIZE} --format=berkeley S32K3_M7_0_0.elf
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
MK_RMDIR=$(if ${1}, del  ${1} )
MK_PATHTOWIN=$(subst /,\,${1})
.PHONY : clean
clean:
	$(call MK_RMDIR, $(call MK_PATHTOWIN, ${OBJS} $(USER_OBJS) ))

secondary-outputs: $(SECONDARY_SIZE)

.PHONY: all clean dependents
./S32K3_M7_0_2.elf:

-include ../makefile.targets
