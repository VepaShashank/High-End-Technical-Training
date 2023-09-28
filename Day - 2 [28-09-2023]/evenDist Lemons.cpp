#include <stdio.h>
int main() {
    int tl,rem,rl,lpp,tp;
    printf("Enter the no of priests: ");
    scanf("%d",&tp);
    printf("Enter the total no of lemons: ");
    scanf("%d",&tl);
	lpp=tl/tp;
    rem=tl%tp;
    if (rem==0) {
        printf("Each priest will receive %d lemons.\n",tl/tp);
    } else {
    	if(rem==1){
    		printf("Each priest will receive %d lemons, %d lemon left.\n",lpp,rem);
		}else{
			printf("Each priest will receive %d lemons, %d lemons left.\n",lpp,rem);
		}
        rl=tl+(tp-rem);
        printf("For equal distribution, you should buy %d lemons.\n",rl);
    }
    return 0;
}
