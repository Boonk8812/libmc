public class NullCheck {
    public static void main(String[] args) {
        try {
            Object obj = null;
            if (obj == null) {
                System.out.println("ERROR: NULL HAS BEEN DETECTED");
                Thread.sleep(3000);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
