import java.lang.Math;

public class JavaGenerator {

    public static void random_generator(int number_bits) {
        for (int i = 0; i < number_bits; i++) {
            int ran_num = (int)(Math.random()*2);
            System.out.print(ran_num);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int NUMBER_BITS = 128;
        random_generator(NUMBER_BITS);
    }
}