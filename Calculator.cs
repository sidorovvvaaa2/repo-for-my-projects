namespace SimpleCalculator
{
    public static class Calculator
    {
        public static double Add(double a, double b) => a + b;
        
        public static double Subtract(double a, double b) => a - b;
        
        public static double Multiply(double a, double b) => a * b;
        
        public static double Divide(double a, double b)
        {
            if (Math.Abs(b) < double.Epsilon)
                throw new DivideByZeroException("Cannot divide by zero");
            return a / b;
        }
        
        public static double Power(double a, double b) => Math.Pow(a, b);
        
        public static double SquareRoot(double a)
        {
            if (a < 0)
                throw new ArgumentException("Cannot calculate square root of negative number");
            return Math.Sqrt(a);
        }
    }
}