import { RollDiceGame } from "./RollDiceGame";

export class Player {
    private _isInGame = false;
    private _game: RollDiceGame;

    enter(game: RollDiceGame) {
        if (this._isInGame) {
            throw new TypeError("Unable to enter another game");
        }
        game.join(this);
        this._game = game;
        this._isInGame = true;
    }

    leaveGame() {
        if (!this._isInGame) {
            throw new TypeError("Unable to leave the game before entering");
        }
        this._game.leave(this);        
        this._isInGame = false;
    }

    isInGame(): boolean {
        return this._isInGame
    }
}