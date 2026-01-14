using NUnit.Framework;

namespace SimpleCalculator.Tests
{
    [TestFixture]
    public class CalculatorTests
    {
        [Test]
        public void Add_TwoPositiveNumbers_ReturnsCorrectSum()
        {
            // Arrange
            double a = 5;
            double b = 3;
            
            // Act
            double result = Calculator.Add(a, b);
            
            // Assert
            Assert.AreEqual(8, result);
        }
        
        [Test]
        public void Add_NegativeAndPositiveNumber_ReturnsCorrectSum()
        {
            double result = Calculator.Add(-5, 3);
            Assert.AreEqual(-2, result);
        }
        
        [Test]
        public void Subtract_TwoNumbers_ReturnsCorrectDifference()
        {
            double result = Calculator.Subtract(10, 4);
            Assert.AreEqual(6, result);
        }
        
        [Test]
        public void Multiply_TwoNumbers_ReturnsCorrectProduct()
        {
            double result = Calculator.Multiply(7, 6);
            Assert.AreEqual(42, result);
        }
        
        [Test]
        public void Multiply_ByZero_ReturnsZero()
        {
            double result = Calculator.Multiply(5, 0);
            Assert.AreEqual(0, result);
        }
        
        [Test]
        public void Divide_TwoNumbers_ReturnsCorrectQuotient()
        {
            double result = Calculator.Divide(10, 2);
            Assert.AreEqual(5, result);
        }
        
        [Test]
        public void Divide_ByZero_ThrowsDivideByZeroException()
        {
            Assert.Throws<DivideByZeroException>(() => Calculator.Divide(5, 0));
        }
        
        [Test]
        public void Divide_ZeroByNumber_ReturnsZero()
        {
            double result = Calculator.Divide(0, 5);
            Assert.AreEqual(0, result);
        }
        
        [Test]
        public void Power_NumberToExponent_ReturnsCorrectValue()
        {
            double result = Calculator.Power(2, 3);
            Assert.AreEqual(8, result);
        }
        
        [Test]
        public void Power_ToZeroPower_ReturnsOne()
        {
            double result = Calculator.Power(5, 0);
            Assert.AreEqual(1, result);
        }
        
        [Test]
        public void SquareRoot_PositiveNumber_ReturnsCorrectValue()
        {
            double result = Calculator.SquareRoot(16);
            Assert.AreEqual(4, result);
        }
        
        [Test]
        public void SquareRoot_Zero_ReturnsZero()
        {
            double result = Calculator.SquareRoot(0);
            Assert.AreEqual(0, result);
        }
        
        [Test]
        public void SquareRoot_NegativeNumber_ThrowsArgumentException()
        {
            Assert.Throws<ArgumentException>(() => Calculator.SquareRoot(-4));
        }
        
        [TestCase(2, 3, 5)]
        [TestCase(0, 0, 0)]
        [TestCase(-5, 10, 5)]
        [TestCase(2.5, 3.5, 6)]
        public void Add_VariousCases_ReturnsCorrectResult(double a, double b, double expected)
        {
            double result = Calculator.Add(a, b);
            Assert.AreEqual(expected, result, 0.0001);
        }
    }
}