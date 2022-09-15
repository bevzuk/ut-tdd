import { RollDiceGame } from "./RollDiceGame";

export class Player {
    _isInGame = false;

    enter(game: RollDiceGame) {
        if (this._isInGame) {
            throw new TypeError("Unable to enter another game");
        }
        this._isInGame = true;
    }

    leaveGame() {
        if (!this._isInGame) {
            throw new TypeError("Unable to leave the game before entering");
        }
        this._isInGame = false;
    }

    isInGame(): boolean {
        return this._isInGame
    }
}