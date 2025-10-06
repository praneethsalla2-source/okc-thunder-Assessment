/**
 * TypeScript interfaces for player summary data
 */

export interface Shot {
  loc: [number, number]; // [x, y] coordinates in feet relative to offensive basket
  points: number;
}

export interface Pass {
  startLoc: [number, number]; // [x, y] coordinates in feet relative to offensive basket
  endLoc: [number, number]; // [x, y] coordinates in feet relative to offensive basket
  isCompleted: boolean;
  isPotentialAssist: boolean;
  isTurnover: boolean;
}

export interface Turnover {
  loc: [number, number]; // [x, y] coordinates in feet relative to offensive basket
}

export interface ActionTypeStats {
  totalShotAttempts: number;
  totalPoints: number;
  totalPasses: number;
  totalPotentialAssists: number;
  totalTurnovers: number;
  totalPassingTurnovers: number;
  shots: Shot[];
  passes: Pass[];
  turnovers: Turnover[];
}

export interface PlayerSummary {
  name: string;
  playerID: number;
  totalShotAttempts: number;
  totalPoints: number;
  totalPasses: number;
  totalPotentialAssists: number;
  totalTurnovers: number;
  totalPassingTurnovers: number;
  pickAndRollCount: number;
  isolationCount: number;
  postUpCount: number;
  offBallScreenCount: number;
  pickAndRoll: ActionTypeStats;
  isolation: ActionTypeStats;
  postUp: ActionTypeStats;
  offBallScreen: ActionTypeStats;
  // Rankings
  totalShotAttemptsRank?: number;
  totalPointsRank?: number;
  totalPassesRank?: number;
  totalPotentialAssistsRank?: number;
  totalTurnoversRank?: number;
  totalPassingTurnoversRank?: number;
  pickAndRollCountRank?: number;
  isolationCountRank?: number;
  postUpCountRank?: number;
  offBallScreenCountRank?: number;
}

export interface PlayerSummaryResponse {
  endpoint: string;
  apiResponse: PlayerSummary;
}
