package javastart1;

public class hometask2 {
    public static void main(String[] args) {
        System.out.println("Вот все простые числа до 1000: ");
        for (int i=2;i<1000;i++){
        if(check(i))
            System.out.print("_"+ i);
    }
}

public static boolean check(int i){
    if (i<=1)
        return false;
    else if (i <=3)
        return true;
    else if (i%2==0 || i %3 ==0)
        return false;
    int n = 5;
    while (n*n <=i){
        if (i % n ==0 || i % (n+2) == 0)
            return false;
        n=n+6;
    }
    return true;
}
}
