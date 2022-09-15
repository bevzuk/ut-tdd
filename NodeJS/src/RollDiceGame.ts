import { Player } from "./Player";

export class RollDiceGame {
    private _players: Player[] = [];

    join(player: Player) {
        if (this._players.length == 6) {
            throw new TypeError("Game can not accept more than 6 players");
        }
        this._players.push(player);
    }

    leave(player: Player) {
        this._players = this._players.filter(p => p !== player);
    }
    
}