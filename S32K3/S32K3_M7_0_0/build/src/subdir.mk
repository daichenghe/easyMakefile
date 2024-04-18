  
# Automatically-generated file. Do not edit!  
  
C_SRCS += \
    .././src/main.c \
  
OBJS += \
    ./src/main.o \
  
C_DEPS += \
    ./src/main.d \

./src/%.o: .././src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Standard S32DS C Compiler'
	${TC_CC} "@./src/default.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '
