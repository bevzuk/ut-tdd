import { RollDiceGame } from "./RollDiceGame";

export class Player {
    private _currentGame: RollDiceGame;

    enter(game: RollDiceGame) {
        if (this.isInGame()) {
            throw new TypeError("Unable to enter another game");
        }
        game.join(this);
        this._currentGame = game;
    }

    leaveGame() {
        if (!this.isInGame()) {
            throw new TypeError("Unable to leave the game before entering");
        }
        this._currentGame.leave(this);
        this._currentGame = null;    
    }

    isInGame(): boolean {
        if (this._currentGame) return true;
        else return false;
    }
}