namespace Domain
{
    public class RollDiceGame
    {
        private int playersCount;

        public void AddPlayer(Player player)
        {
            if (playersCount == 6)
            {
                throw new TooManyPlayersException();
            }
            playersCount++;
        }

        public void RemovePlayer(Player player)
        {
            playersCount--;
        }
    }
}