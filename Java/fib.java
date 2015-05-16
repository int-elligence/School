public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
       System.out.print("enter n");
       int n=input.nextInt();
       int count=1;
        int c=1,b=1,a=0;
       while(count<=n){
      
           c=b+a;
      System.out.print(c);
       a=b;
       b=c;
        
       count++;}
        }
    }
