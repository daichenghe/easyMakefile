  
# Automatically-generated file. Do not edit!  
  
C_SRCS += \
    .././generate/src/Clock_Ip_Cfg.c \
    .././generate/src/Igf_Port_Ip_Cfg.c \
    .././generate/src/OsIf_Cfg.c \
  
OBJS += \
    ./generate/src/Clock_Ip_Cfg.o \
    ./generate/src/Igf_Port_Ip_Cfg.o \
    ./generate/src/OsIf_Cfg.o \
  
C_DEPS += \
    ./generate/src/Clock_Ip_Cfg.d \
    ./generate/src/Igf_Port_Ip_Cfg.d \
    ./generate/src/OsIf_Cfg.d \

./generate/src/%.o: .././generate/src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Standard S32DS C Compiler'
	${TC_CC} "@./generate/src/default.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '
