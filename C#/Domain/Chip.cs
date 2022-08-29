namespace Domain
{
    public class Chip
    {
        private readonly int amount;

        public Chip(int amount)
        {
            this.amount = amount;
        }

        public static bool operator >=(Chip a, Chip b)
        {
            return a.amount >= b.amount;
        }

        public static bool operator <=(Chip a, Chip b)
        {
            return a.amount <= b.amount;
        }
    }
}