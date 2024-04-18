  
# Automatically-generated file. Do not edit!  
  
C_SRCS += \
    .././board/Siul2_Port_Ip_Cfg.c \
    .././board/Tspc_Port_Ip_Cfg.c \
  
OBJS += \
    ./board/Siul2_Port_Ip_Cfg.o \
    ./board/Tspc_Port_Ip_Cfg.o \
  
C_DEPS += \
    ./board/Siul2_Port_Ip_Cfg.d \
    ./board/Tspc_Port_Ip_Cfg.d \

./board/%.o: .././board/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Standard S32DS C Compiler'
	${TC_CC} "@./board/default.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '
