import { RollDiceGame } from "./RollDiceGame";

export class Player {
    _isInGame = false;

    enter(game: RollDiceGame) {
        this._isInGame = true;
    }

    isInGame(): boolean {
        return this._isInGame
    }
}