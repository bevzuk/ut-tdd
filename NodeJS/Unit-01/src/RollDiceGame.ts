import { Player } from "./Player";
import { TooManyPlayersError } from "./TooManyPlayersError";

export class RollDiceGame {
    private _players: Player[] = [];

    addPlayer(player: Player) {
        if (this._players.length == 6) {
            throw new TooManyPlayersError();
        }
        this._players.push(player);
    }

    removePlayer(player: Player) {
        this._players = this._players.filter(p => p !== player);
    }

    play() {
        const winningScore = Math.floor(Math.random() * 6 + 1);
        this._players.forEach(player => {
            var bet = player.getBet();
            if (!bet) return;

            if (bet.score === winningScore) {
                player.win(bet.chips.multiply(6))
            }
            else {
                player.lose(bet.chips);
            };
        });
    }
}